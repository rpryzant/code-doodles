
"""
python batch_tokenize.py domain_adaptation tok_file.sh
"""

import sys
from joblib import Parallel, delayed
import os
from tqdm import tqdm
import re
import subprocess


data_root = sys.argv[1]
tokenizer = sys.argv[2]


PREDFILE_SUFFIX = '_pred'


def tokenize(f):
    """ tokenizes a file f
    """
    cmd = './%s %s' % (tokenizer, f)
    os.system(cmd)
    print cmd
    return f + '.tok'


def step_number(f):
    """ gets step number from prediction filename
    """
    try:
        return int(re.findall('\d+', f)[0])
    except:
        return -1


def gen_dev_runs(root):
    """ generates files for a run  from a root dir
    """
    for subdir, dirs, files in tqdm(os.walk(data_root)):
        if len(files) <= 1:
            continue
#        files = [f for f in files if '.tok' not in f]
        files = [f for f in files if '_pred' in f and '.tok' not in f]

        files = sorted(files, key=lambda x: step_number(x))[::-1]
        N = len(files)
        for file in tqdm(files):#[:N/2]):
            yield os.path.join(subdir, file)



Parallel(n_jobs=6)(delayed(tokenize)(run) for run in gen_dev_runs(data_root))
