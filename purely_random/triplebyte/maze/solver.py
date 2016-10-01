"""
next steps:
   make into A* incorporate manhattan distance

"""


import sys
import Queue



OFFSETS = [(-1, 0), (1, 0), (0, 1), (0, -1)]


class Maze:
    def __init__(self, maze_file):
        self.maze_array = self.parse_file(maze_file)
        self.start, self.end = self.find_points()

    def parse_file(self, filename):
        file = open(filename)
        maze = [[char for char in line.strip()] for line in file]
        return maze

    def find_points(self):
        points = {}
        for r, row in enumerate(self.maze_array):
            for c, x in enumerate(row):
                if x == 'X':
                    points['start'] = (r, c)
                elif x == 'O':
                    points['end'] = (r, c)
        return points['start'], points['end']

    
    def solve(self):
        """ finds path from start => end """
        path = self.__bfs(self.start, self.end)
        return path

    def __get_neighbors(self, coord, visited):
        candidates = []
        for offset in OFFSETS:
            candidates.append( tuple(sum(pair) for pair in zip(offset, coord) ) )
        return [c for c  in candidates if self.__valid(c, visited)]


    def __valid(self, c, visited):
        # c is off edge of map
        if c[0] < 0 or c[0] >= len(self.maze_array):
            return False
        if c[1] < 0 or c[1] >= len(self.maze_array[0]):
            return False
        # c is a wall
        if self.maze_array[c[0]][c[1]] == '#':
            return False
        # we've already visited c
        if c in visited:
            return False
        # good to go!
        return True


    def get(self, pt):
        return self.maze_array[pt[0]][pt[1]]
    
    def __bfs(self, start, end):
        q = Queue.Queue()
        q.put( (start, [start]) )
        visited = [start]
        while not q.empty():
            pt, cur_path = q.get()
            if self.maze_array[pt[0]][pt[1]] == 'O':
                self.print_path(cur_path)
                return cur_path
            neighbors = self.__get_neighbors(pt, visited)
            for neighbor in neighbors:
                cur_path.append(neighbor)
                visited.append(neighbor)
                q.put( (neighbor, cur_path[:]) )
        return None

    def print_path(self, path):
        maze_copy = [row[:] for row in self.maze_array]
        for pt in path:
            maze_copy[pt[0]][pt[1]] = '+'
        print '\n'.join(''.join(c for c in row) for row in maze_copy)
                      
    




if __name__ == '__main__':
    maze = Maze(sys.argv[1])
    path = maze.solve()
    print path
