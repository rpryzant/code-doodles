import numpy as np
import math
import sys
from copy import deepcopy
from scipy import ndimage
from scipy import misc
from pymongo import MongoClient
import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from os.path import expanduser
import time
import os


# ============================SETTINGS PARAMETERS===================================
#                  DISTANCE_THRESHOLD_MULTIPLYER                                   |
# -during the first selection pass, query pixels are compared to the target color  |
#     and the distance between the two is calculated. This is used to determine    |
#     whether the distance is small enough to be selected.                         |
#- bigger number => more pixels                                                    | 
#- smaller number => less pixels                                                   |
#                                                                                  |
#                       COMPONENT_FILTER_MULTIPLYER                                |
# -during the second selection pass, we identify connected components of selected  |
#     pixels. This is used to determine whether a component is big enough to be    |
#     passed forward                                                               |
#- bigger number => fewer, bigger components                                       |
#- smaller number => more, smaller components                                      |
# 
#                         PIXEL_MASK_MULTIPLYER                                    |
# -as part of the second selection pass, we mask away low-value pixels (pixels     |
#     close to [0,0,0]). this determines how close to [0,0,0] we want to mask away.|
#     We've already bifurcated the image into red (255,0,0) and black (0,0,0) pixels
#     so any masking threshold will do. basically DON'T CHANGE THIS                |

#===================================================================================

TARGETDIR = "%s/%s" % (os.path.abspath(os.path.dirname(__file__)), sys.argv[1])

def configure():
    settings = {}
    
    settings['water'] = {}
    settings['water']['target'] = [51, 64, 115]
    settings['water']['dtm'] = 0.8
    settings['water']['cfm'] = 2.2
    settings ['water']['pmm'] = 1
    settings['water']['rect'] = (0, 150, 330, 320)
    
    settings['yogurt'] = {}
    settings['yogurt']['target'] = [202, 97, 91]
    settings['yogurt']['dtm'] = .4
    settings['yogurt']['cfm'] = 1.6
    settings ['yogurt']['pmm'] = 1
    settings['yogurt']['rect'] = (370, 300, 540, 400)

    settings['juice'] = {}
    settings['juice']['target'] = [214, 181, 114]
    settings['juice']['dtm'] = .5
    settings['juice']['cfm'] = .9
    settings ['juice']['pmm'] = 1
    settings['juice']['rect'] = (450, 0, 640, 160)
    
    settings['cans'] = {}
    settings['cans']['target'] = [222, 85, 77]
    settings['cans']['dtm'] = 1.7
    settings['cans']['cfm'] = .9
    settings ['cans']['pmm'] = 1
    settings['cans']['rect'] = (0, 0, 350, 150)
    
    settings['carrots'] = {}
    settings['carrots']['target'] = [180, 133, 118]
    settings['carrots']['dtm'] = .3
    settings['carrots']['cfm'] = 2
    settings ['carrots']['pmm'] = 1
    settings['carrots']['rect'] = (0, 330, 60, 450)

    #mystery shelf: (400, 150, 570, 290)
    return settings

class NewPhotoHandler(FileSystemEventHandler):
    def __init__(self, client):
        self.client = client

    def on_any_event(self, event):
        img_file = event.src_path
        post = {
            "timestamp" : datetime.datetime.utcnow(),
            "items" : {}
            }
        db = self.client.fridge
        collection = db.fridge_contents

        settings = configure()
    
        for item, item_dict in settings.iteritems():
            item_image = Image(img_file, item_dict)
            target_color = item_dict['target']
            post['items'][item] = item_image.select_color_swath(target_color)
        
        db.posts.insert(post)
        print "posted to the db."
    
def main():
    client = MongoClient()
    event_handler = NewPhotoHandler(client)
    observer = Observer()
    observer.schedule(event_handler, TARGETDIR, recursive = False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    
    client.close()

class Utils():
    @staticmethod
    def vector_add(a, b):
        return tuple(map(sum, zip(a, b)))

    @staticmethod
    def vector_sub(a,b):
        return tuple(map(sum, zip(a,Utils.vector_negate(b))))

    @staticmethod
    def vector_negate(a):
        return tuple(x * -1 for x in a)

    @staticmethod
    def vector_mul(a, b):
        return tuple(x * y for x, y in zip(a, b))

    @staticmethod
    def vector_dist(a, b):
        return np.linalg.norm(a - b)

    @staticmethod
    def get_rect(image, coords):
        x1, y1, x2, y2 = coords
        temp = image[y1:y2]
        out = []
        for row in temp:
            out.append(row[x1:x2])
        return np.array(out)

class Image(object):
    def __init__(self, filename, settings = None):
        self.raw_matrix = misc.imread(filename)
        
        if len(self.raw_matrix[0,0] > 3):
            self.rgb_matrix = self.__clean_arr(self.raw_matrix)
        else:
            self.rgb_matrix = self.raw_matrix

        coords = settings['rect']
        if coords is not None:
            self.rgb_matrix = Utils.get_rect(self.raw_matrix, coords)

        self.height = len(self.rgb_matrix)
        self.width = len(self.rgb_matrix[0])
        self.size = self.height * self.width

        # In this context, the standard deviation is a numerical value
        # representing the standard deviation of the "distances" between
        # all pixels
        self.std = np.std(self.raw_matrix)

        # Same as for standard deviation, uses the "distances" between
        # pixels.
        self.mean = np.mean(self.raw_matrix)

        self.distance_threshold_multiplyer = settings['dtm']
        self.component_filter_multiplyer = settings['cfm']
        self.pixel_mask_multiplyer = settings['pmm']

        self.settings = settings

    """
    Numpy will sometimes add a fourth parameter to the cells of the matrix.
    This method strips the fourth parameter in all cells.
    """
    def __clean_arr(self, in_matrix):
        out = []

        for row, _ in enumerate(in_matrix):
            row_tmp = []
            for col, _ in enumerate(in_matrix[row]):
                row_tmp.append(in_matrix[row,col][0:3])
            out.append(row_tmp)
        return np.array(out)

    def select_color_swath(self, color):
        # assuming the distribution of color distances is gaussian
        distance_threshold = self.std * self.distance_threshold_multiplyer
        #print "using distance thresh %f" % distance_threshold
        out = []
        selected_pixels = 0
        for row_i, row in enumerate(self.rgb_matrix):
            row_tmp = []
            for col_i, pixel in enumerate(row):
                if Utils.vector_dist(pixel, color) <= distance_threshold:
                    selected_pixels += 1
                    row_tmp.append([255,0,0])
                else:
                    row_tmp.append([0,0,0])
            out.append(row_tmp)
        out = np.array(out, dtype = 'uint8')
        print "%%  pixels in first selection pass: %f" %  self.__proportion_selected(out)
        return self.__kill_small_components(out)


    def __kill_small_components(self, image):
        # Create a new matrix where cells are effectively "true" if they are greater
        # than the mean times the multiplier, or "false" if they are not.
        mask = image > image.mean() * self.pixel_mask_multiplyer

        # Give each grouping of "true" values a unique identifier, and return the number of
        # groups detected.
        label_image, num_labels = ndimage.label(mask)

        # Get the size of each each component.
        component_sizes = ndimage.sum(mask, label_image, range(num_labels + 1))

        # Filter the componets by their size compared to the mean (times a multiplier)
        filtered_components = component_sizes < component_sizes.mean() * self.component_filter_multiplyer

        # This sets a variable to all of the pixels in the image which correspond to the groups that
        # were not considered large enough (from the last line)
        pixels_to_remove = filtered_components[label_image]

        # Zero these pixels
        image[pixels_to_remove] = 0
        #print "%%  pixels in second selection pass: %f" %  self.__proportion_selected(image)
        #return image
        return self.__proportion_selected(image)

    def __proportion_selected(self, image):
        return np.count_nonzero(image) / float(len(image) * len(image[0]))

if __name__ == "__main__":
    main()



