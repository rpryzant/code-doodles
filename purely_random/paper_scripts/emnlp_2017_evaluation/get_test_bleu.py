
"""
python get_test_bleu.py [dir with tokenized dev files] [dev labels] [test labels] [bleu script]
"""

import sys
from joblib import Parallel, delayed
import os
from tqdm import tqdm
import re
import subprocess


#data_root = sys.argv[1]
#dev_labels = sys.argv[2]
#test_labels = sys.argv[2]
bleu_script = sys.argv[1]

'results/fr_labels//test.europarl.bpe.fr.tok'
'results/fr_labels//test.opensubtitles.bpe.fr.tok'

'results/zh_labels/test.ted.bpe.zh.tok'
'results/zh_labels/test.news.bpe.zh.tok'

LABEL_MAPPINGS = {
#'small_data//fr/small_data_discriminator/data_fr_europarl_opensubtitles.train_combined_eval_europarl.model_lossmul_10_reversegrad_0/eval/eval/small_data_discriminator.eval_fr_europarl_dev.data_fr_europarl_opensubtitles.train_combined_eval_europarl.model_lossmul_10_reversegrad_0'
'small_data//fr/small_data_discriminator/data_fr_europarl_opensubtitles.train_combined_eval_europarl.model_lossmul_10_reversegrad_0/eval/eval/small_data_discriminator.eval_fr_europarl_test.data_fr_europarl_opensubtitles.train_combined_eval_europarl.model_lossmul_10_reversegrad_0': 'results/fr_labels//test.europarl.bpe.fr.tok',
#'small_data//fr/small_data_discriminator/data_fr_europarl_opensubtitles.train_combined_eval_europarl.model_lossmul_10_reversegrad_0/eval/eval/small_data_discriminator.eval_fr_opensubtitles_dev.data_fr_europarl_opensubtitles.train_combined_eval_europarl.model_lossmul_10_reversegrad_0'
'small_data//fr/small_data_discriminator/data_fr_europarl_opensubtitles.train_combined_eval_europarl.model_lossmul_10_reversegrad_0/eval/eval/small_data_discriminator.eval_fr_opensubtitles_test.data_fr_europarl_opensubtitles.train_combined_eval_europarl.model_lossmul_10_reversegrad_0': 'results/fr_labels//test.opensubtitles.bpe.fr.tok',
#'small_data//fr/small_data_discriminator/data_fr_europarl_opensubtitles.train_combined_eval_europarl.model_lossmul_10_reversegrad_1/eval/eval/small_data_discriminator.eval_fr_europarl_dev.data_fr_europarl_opensubtitles.train_combined_eval_europarl.model_lossmul_10_reversegrad_1'
'small_data//fr/small_data_discriminator/data_fr_europarl_opensubtitles.train_combined_eval_europarl.model_lossmul_10_reversegrad_1/eval/eval/small_data_discriminator.eval_fr_europarl_test.data_fr_europarl_opensubtitles.train_combined_eval_europarl.model_lossmul_10_reversegrad_1': 'results/fr_labels//test.europarl.bpe.fr.tok',
#'small_data//fr/small_data_discriminator/data_fr_europarl_opensubtitles.train_combined_eval_europarl.model_lossmul_10_reversegrad_1/eval/eval/small_data_discriminator.eval_fr_opensubtitles_dev.data_fr_europarl_opensubtitles.train_combined_eval_europarl.model_lossmul_10_reversegrad_1'
'small_data//fr/small_data_discriminator/data_fr_europarl_opensubtitles.train_combined_eval_europarl.model_lossmul_10_reversegrad_1/eval/eval/small_data_discriminator.eval_fr_opensubtitles_test.data_fr_europarl_opensubtitles.train_combined_eval_europarl.model_lossmul_10_reversegrad_1': 'results/fr_labels//test.opensubtitles.bpe.fr.tok',
#'small_data//fr/small_data_target_token/data_fr_europarl_opensubtitles.train_combined_eval_europarl/eval/eval/small_data_target_token.eval_fr_europarl_dev.data_fr_europarl_opensubtitles.train_combined_eval_europarl'
'small_data//fr/small_data_target_token/data_fr_europarl_opensubtitles.train_combined_eval_europarl/eval/eval/small_data_target_token.eval_fr_europarl_test.data_fr_europarl_opensubtitles.train_combined_eval_europarl': 'results/fr_labels//test.europarl.bpe.fr.tok',
#'small_data//fr/small_data_target_token/data_fr_europarl_opensubtitles.train_combined_eval_europarl/eval/eval/small_data_target_token.eval_fr_opensubtitles_dev.data_fr_europarl_opensubtitles.train_combined_eval_europarl'
'small_data//fr/small_data_target_token/data_fr_europarl_opensubtitles.train_combined_eval_europarl/eval/eval/small_data_target_token.eval_fr_opensubtitles_test.data_fr_europarl_opensubtitles.train_combined_eval_europarl': 'results/fr_labels//test.opensubtitles.bpe.fr.tok',
#'small_data//zh/small_data_discriminator/data_zh_news_ted.train_combined_eval_news.model_lossmul_10_reversegrad_0/eval/eval/small_data_discriminator.eval_zh_news_dev.data_zh_news_ted.train_combined_eval_news.model_lossmul_10_reversegrad_0'
'small_data//zh/small_data_discriminator/data_zh_news_ted.train_combined_eval_news.model_lossmul_10_reversegrad_0/eval/eval/small_data_discriminator.eval_zh_news_test.data_zh_news_ted.train_combined_eval_news.model_lossmul_10_reversegrad_0': 'results/zh_labels/test.news.bpe.zh.tok',
#'small_data//zh/small_data_discriminator/data_zh_news_ted.train_combined_eval_news.model_lossmul_10_reversegrad_0/eval/eval/small_data_discriminator.eval_zh_ted_dev.data_zh_news_ted.train_combined_eval_news.model_lossmul_10_reversegrad_0'
'small_data//zh/small_data_discriminator/data_zh_news_ted.train_combined_eval_news.model_lossmul_10_reversegrad_0/eval/eval/small_data_discriminator.eval_zh_ted_test.data_zh_news_ted.train_combined_eval_news.model_lossmul_10_reversegrad_0': 'results/zh_labels/test.ted.bpe.zh.tok',
#'small_data//zh/small_data_discriminator/data_zh_news_ted.train_combined_eval_news.model_lossmul_10_reversegrad_1/eval/eval/small_data_discriminator.eval_zh_news_dev.data_zh_news_ted.train_combined_eval_news.model_lossmul_10_reversegrad_1'
'small_data//zh/small_data_discriminator/data_zh_news_ted.train_combined_eval_news.model_lossmul_10_reversegrad_1/eval/eval/small_data_discriminator.eval_zh_news_test.data_zh_news_ted.train_combined_eval_news.model_lossmul_10_reversegrad_1': 'results/zh_labels/test.news.bpe.zh.tok',
#'small_data//zh/small_data_discriminator/data_zh_news_ted.train_combined_eval_news.model_lossmul_10_reversegrad_1/eval/eval/small_data_discriminator.eval_zh_ted_dev.data_zh_news_ted.train_combined_eval_news.model_lossmul_10_reversegrad_1'
'small_data//zh/small_data_discriminator/data_zh_news_ted.train_combined_eval_news.model_lossmul_10_reversegrad_1/eval/eval/small_data_discriminator.eval_zh_ted_test.data_zh_news_ted.train_combined_eval_news.model_lossmul_10_reversegrad_1': 'results/zh_labels/test.ted.bpe.zh.tok',
#'small_data//zh/small_data_target_token/data_zh_news_ted.train_combined_eval_news/eval/eval/small_data_target_token.eval_zh_news_dev.data_zh_news_ted.train_combined_eval_news'
'small_data//zh/small_data_target_token/data_zh_news_ted.train_combined_eval_news/eval/eval/small_data_target_token.eval_zh_news_test.data_zh_news_ted.train_combined_eval_news': 'results/zh_labels/test.news.bpe.zh.tok',
#'small_data//zh/small_data_target_token/data_zh_news_ted.train_combined_eval_news/eval/eval/small_data_target_token.eval_zh_ted_dev.data_zh_news_ted.train_combined_eval_news'
'small_data//zh/small_data_target_token/data_zh_news_ted.train_combined_eval_news/eval/eval/small_data_target_token.eval_zh_ted_test.data_zh_news_ted.train_combined_eval_news': 'results/zh_labels/test.ted.bpe.zh.tok'


}

LABEL_MAPPINGS_FR = {
'results//fr_baselines/data_fr_europarl_opensubtitles.train_combined_eval_europarl/eval/eval/small_data_baselines.eval_fr_europarl_dev.data_fr_europarl_opensubtitles.train_combined_eval_europarl' : None,
'results//fr_baselines/data_fr_europarl_opensubtitles.train_combined_eval_europarl/eval/eval/small_data_baselines.eval_fr_europarl_test.data_fr_europarl_opensubtitles.train_combined_eval_europarl': 'results/fr_labels//test.europarl.bpe.fr.tok',
'results//fr_baselines/data_fr_europarl_opensubtitles.train_combined_eval_europarl/eval/eval/small_data_baselines.eval_fr_opensubtitles_dev.data_fr_europarl_opensubtitles.train_combined_eval_europarl': None,
'results//fr_baselines/data_fr_europarl_opensubtitles.train_combined_eval_europarl/eval/eval/small_data_baselines.eval_fr_opensubtitles_test.data_fr_europarl_opensubtitles.train_combined_eval_europarl': 'results/fr_labels//test.opensubtitles.bpe.fr.tok',
'results//fr_baselines/data_fr_europarl_opensubtitles.train_europarl_eval_europarl/eval/eval/small_data_baselines.eval_fr_europarl_dev.data_fr_europarl_opensubtitles.train_europarl_eval_europarl': 'results/fr_labels//dev.opensubtitles.bpe.fr.tok',
'results//fr_baselines/data_fr_europarl_opensubtitles.train_europarl_eval_europarl/eval/eval/small_data_baselines.eval_fr_europarl_test.data_fr_europarl_opensubtitles.train_europarl_eval_europarl': 'results/fr_labels//test.europarl.bpe.fr.tok',
'results//fr_baselines/data_fr_europarl_opensubtitles.train_europarl_eval_europarl/eval/eval/small_data_baselines.eval_fr_opensubtitles_dev.data_fr_europarl_opensubtitles.train_europarl_eval_europarl': None,
'results//fr_baselines/data_fr_europarl_opensubtitles.train_europarl_eval_europarl/eval/eval/small_data_baselines.eval_fr_opensubtitles_test.data_fr_europarl_opensubtitles.train_europarl_eval_europarl': 'results/fr_labels//test.opensubtitles.bpe.fr.tok',
'results//fr_baselines/data_fr_europarl_opensubtitles.train_opensubtitles_eval_europarl/eval/eval/small_data_baselines.eval_fr_europarl_dev.data_fr_europarl_opensubtitles.train_opensubtitles_eval_europarl': 'results/fr_labels//dev.opensubtitles.bpe.fr.tok',
'results//fr_baselines/data_fr_europarl_opensubtitles.train_opensubtitles_eval_europarl/eval/eval/small_data_baselines.eval_fr_europarl_test.data_fr_europarl_opensubtitles.train_opensubtitles_eval_europarl': 'results/fr_labels//test.europarl.bpe.fr.tok',
'results//fr_baselines/data_fr_europarl_opensubtitles.train_opensubtitles_eval_europarl/eval/eval/small_data_baselines.eval_fr_opensubtitles_dev.data_fr_europarl_opensubtitles.train_opensubtitles_eval_europarl': 'results/fr_labels//dev.opensubtitles.bpe.fr.tok',
'results//fr_baselines/data_fr_europarl_opensubtitles.train_opensubtitles_eval_europarl/eval/eval/small_data_baselines.eval_fr_opensubtitles_test.data_fr_europarl_opensubtitles.train_opensubtitles_eval_europarl': 'results/fr_labels//test.opensubtitles.bpe.fr.tok',
}
OTHER = {
'results//ja_experiments/baseline_v2/train_aspec_eval_aspec_0/eval/eval/eval_aspec_dev_train_aspec_eval_aspec_0': None,
'results//ja_experiments/baseline_v2/train_aspec_eval_aspec_0/eval/eval/eval_aspec_test_train_aspec_eval_aspec_0': 'results/ja_labels//test.aspec.bpe.ja.tok.kytea.txt',
'results//ja_experiments/baseline_v2/train_aspec_eval_aspec_0/eval/eval/eval_subtitles_dev_train_aspec_eval_aspec_0': None,
'results//ja_experiments/baseline_v2/train_aspec_eval_aspec_0/eval/eval/eval_subtitles_test_train_aspec_eval_aspec_0': 'results/ja_labels//test.subtitles.bpe.ja.tok.kytea.txt',
'results//ja_experiments/baseline_v2/train_combined_eval_aspec_0/eval/eval/eval_aspec_dev_train_combined_eval_aspec_0': None,
'results//ja_experiments/baseline_v2/train_combined_eval_aspec_0/eval/eval/eval_aspec_test_train_combined_eval_aspec_0': 'results/ja_labels//test.aspec.bpe.ja.tok.kytea.txt',
'results//ja_experiments/baseline_v2/train_combined_eval_aspec_0/eval/eval/eval_subtitles_dev_train_combined_eval_aspec_0': None,
'results//ja_experiments/baseline_v2/train_combined_eval_aspec_0/eval/eval/eval_subtitles_test_train_combined_eval_aspec_0': 'results/ja_labels//test.subtitles.bpe.ja.tok.kytea.txt',
'results//ja_experiments/baseline_v2/train_subtitles_eval_subtitles_0/eval/eval/eval_aspec_dev_train_subtitles_eval_subtitles_0': None,
'results//ja_experiments/baseline_v2/train_subtitles_eval_subtitles_0/eval/eval/eval_aspec_test_train_subtitles_eval_subtitles_0': 'results/ja_labels//test.aspec.bpe.ja.tok.kytea.txt',
'results//ja_experiments/baseline_v2/train_subtitles_eval_subtitles_0/eval/eval/eval_subtitles_dev_train_subtitles_eval_subtitles_0': None,
'results//ja_experiments/baseline_v2/train_subtitles_eval_subtitles_0/eval/eval/eval_subtitles_test_train_subtitles_eval_subtitles_0': 'results/ja_labels//test.subtitles.bpe.ja.tok.kytea.txt',
'results//ja_experiments/discriminator/model_lossmul_10_reversegrad_0_0/eval/eval/discriminator.eval_aspec_dev.model_lossmul_10_reversegrad_0_0': None,
'results//ja_experiments/discriminator/model_lossmul_10_reversegrad_0_0/eval/eval/discriminator.eval_aspec_test.model_lossmul_10_reversegrad_0_0': 'results/ja_labels//test.aspec.bpe.ja.tok.kytea.txt',
'results//ja_experiments/discriminator/model_lossmul_10_reversegrad_0_0/eval/eval/discriminator.eval_subtitles_dev.model_lossmul_10_reversegrad_0_0': None,
'results//ja_experiments/discriminator/model_lossmul_10_reversegrad_0_0/eval/eval/discriminator.eval_subtitles_test.model_lossmul_10_reversegrad_0_0': 'results/ja_labels//test.subtitles.bpe.ja.tok.kytea.txt',
'results//ja_experiments/discriminator/model_lossmul_10_reversegrad_0_0/eval/eval/discriminator_eval_aspec_dev_model_lossmul_10_reversegrad_0_0': None, 
'results//ja_experiments/discriminator/model_lossmul_10_reversegrad_0_0/eval/eval/discriminator_eval_aspec_test_model_lossmul_10_reversegrad_0_0': 'results/ja_labels//test.aspec.bpe.ja.tok.kytea.txt',
'results//ja_experiments/discriminator/model_lossmul_10_reversegrad_1_0/eval/eval/discriminator.eval_aspec_dev.model_lossmul_10_reversegrad_1_0': None,
'results//ja_experiments/discriminator/model_lossmul_10_reversegrad_1_0/eval/eval/discriminator.eval_aspec_test.model_lossmul_10_reversegrad_1_0': 'results/ja_labels//test.aspec.bpe.ja.tok.kytea.txt',
'results//ja_experiments/discriminator/model_lossmul_10_reversegrad_1_0/eval/eval/discriminator.eval_subtitles_dev.model_lossmul_10_reversegrad_1_0': None,
'results//ja_experiments/discriminator/model_lossmul_10_reversegrad_1_0/eval/eval/discriminator.eval_subtitles_test.model_lossmul_10_reversegrad_1_0': 'results/ja_labels//test.subtitles.bpe.ja.tok.kytea.txt',
'results//ja_experiments/discriminator/model_lossmul_10_reversegrad_1_0/eval/eval/discriminator_eval_aspec_dev_model_lossmul_10_reversegrad_1_0': None,
'results//ja_experiments/discriminator/model_lossmul_10_reversegrad_1_0/eval/eval/discriminator_eval_aspec_test_model_lossmul_10_reversegrad_1_0':  'results/ja_labels//test.aspec.bpe.ja.tok.kytea.txt',
'results//ja_experiments/target_token/train_combined_eval_aspec_0/eval/eval/target_token_eval_aspec_dev_train_combined_eval_aspec_0': None,
'results//ja_experiments/target_token/train_combined_eval_aspec_0/eval/eval/target_token_eval_aspec_test_train_combined_eval_aspec_0':  'results/ja_labels//test.aspec.bpe.ja.tok.kytea.txt',
'results//ja_experiments/target_token/train_combined_eval_aspec_0/eval/eval/target_token_eval_subtitles_dev_train_combined_eval_aspec_0': None,
'results//ja_experiments/target_token/train_combined_eval_aspec_0/eval/eval/target_token_eval_subtitles_test_train_combined_eval_aspec_0': 'results/ja_labels//test.subtitles.bpe.ja.tok.kytea.txt',
'results//ja_experiments/target_token_v2/train_combined_eval_aspec_0/eval/eval/target_token_v2.eval_aspec_dev.train_combined_eval_aspec_0': None,
'results//ja_experiments/target_token_v2/train_combined_eval_aspec_0/eval/eval/target_token_v2.eval_aspec_test.train_combined_eval_aspec_0': 'results/ja_labels//test.aspec.bpe.ja.tok.kytea.txt',
'results//ja_experiments/target_token_v2/train_combined_eval_aspec_0/eval/eval/target_token_v2.eval_subtitles_dev.train_combined_eval_aspec_0': None,
'results//ja_experiments/target_token_v2/train_combined_eval_aspec_0/eval/eval/target_token_v2.eval_subtitles_test.train_combined_eval_aspec_0':  'results/ja_labels//test.subtitles.bpe.ja.tok.kytea.txt',
'results//zh_baselines/data_zh_news_ted.train_combined_eval_news/eval/eval/small_data_baselines.eval_zh_news_dev.data_zh_news_ted.train_combined_eval_news': None,
'results//zh_baselines/data_zh_news_ted.train_combined_eval_news/eval/eval/small_data_baselines.eval_zh_news_test.data_zh_news_ted.train_combined_eval_news': 'results/zh_labels/test.news.bpe.zh.tok',
'results//zh_baselines/data_zh_news_ted.train_combined_eval_news/eval/eval/small_data_baselines.eval_zh_ted_dev.data_zh_news_ted.train_combined_eval_news': None,
'results//zh_baselines/data_zh_news_ted.train_combined_eval_news/eval/eval/small_data_baselines.eval_zh_ted_test.data_zh_news_ted.train_combined_eval_news': 'results/zh_labels/test.ted.bpe.zh.tok',
'results//zh_baselines/data_zh_news_ted.train_news_eval_news/eval/eval/small_data_baselines.eval_zh_news_dev.data_zh_news_ted.train_news_eval_news': None,
'results//zh_baselines/data_zh_news_ted.train_news_eval_news/eval/eval/small_data_baselines.eval_zh_news_test.data_zh_news_ted.train_news_eval_news': 'results/zh_labels/test.news.bpe.zh.tok',
'results//zh_baselines/data_zh_news_ted.train_news_eval_news/eval/eval/small_data_baselines.eval_zh_ted_dev.data_zh_news_ted.train_news_eval_news': None,
'results//zh_baselines/data_zh_news_ted.train_news_eval_news/eval/eval/small_data_baselines.eval_zh_ted_test.data_zh_news_ted.train_news_eval_news': 'results/zh_labels/test.ted.bpe.zh.tok',
'results//zh_baselines/data_zh_news_ted.train_ted_eval_news/eval/eval/small_data_baselines.eval_zh_news_dev.data_zh_news_ted.train_ted_eval_news': None,
'results//zh_baselines/data_zh_news_ted.train_ted_eval_news/eval/eval/small_data_baselines.eval_zh_news_test.data_zh_news_ted.train_ted_eval_news': 'results/zh_labels/test.news.bpe.zh.tok',
'results//zh_baselines/data_zh_news_ted.train_ted_eval_news/eval/eval/small_data_baselines.eval_zh_ted_dev.data_zh_news_ted.train_ted_eval_news': None, 
'results//zh_baselines/data_zh_news_ted.train_ted_eval_news/eval/eval/small_data_baselines.eval_zh_ted_test.data_zh_news_ted.train_ted_eval_news': 'results/zh_labels/test.ted.bpe.zh.tok',
}





def parse_run_type(dir):
    """ parses run type from dir name, e.g. eval_aspec_dev_train_aspec_eval_aspec_0
    """
    try:
        run = os.path.basename(dir)
        run = run.split('_')
        dataset = run[1]
        type = run[2]
        return '%s_%s' % (type, dataset)
    except:
        print 'BROKE!!!!!!!!'
        print dir


def bleu(pred_file, label_file):
   try:
        cmd = './%s %s %s' % (bleu_script, label_file, pred_file)
        print cmd
        result = os.popen(cmd).read()
        print result
        bleu_score = float(result.split(',')[0].split()[2])
        return bleu_score
   except:
        print 'FAILED!!!! ', cmd
        return -1

def step_number(f):
    """ gets step number from prediction filename
    """
    try:
        return int(re.findall('\d+', f)[0])
    except:
        return -1


def get_test_predfile(dir, file):
    """ given a prediction file on the dev set, find the 
        closest test prediction file
    """
    dev_step_number = step_number(file)
    test_dir = dir.replace('dev', 'test')
    test_steps = map(lambda x: step_number(x), os.listdir(test_dir))
    test_predfile = str(min(test_steps, key=lambda(x): abs(dev_step_number - x))) + PREDFILE_SUFFIX
    return os.path.join(test_dir, test_predfile)
    

def get_bleus(root, labels):
    """ zips through a directory with tokenized prediction files and reports that
        with the best development BLEU score
    """
    bleus = {}
    for file in os.listdir(root):
        if not file.endswith('.tok'):
            continue
        file_path = os.path.join(root, file)
        bleus[bleu(file_path, labels)] = file_path

    print bleus



def score(target, labels, OUT):
    out = open(OUT, 'a')

    b = bleu(target, labels)
    out.write(target + ' ' + str(b) + '\n')
    print target + ' ' + str(b)


def gen_targets(root):
    for f in tqdm(os.listdir(root)):
        if f.endswith('.tok'):
            yield os.path.join(root, f)



for data_root in tqdm(LABEL_MAPPINGS.keys()):
    test_labels = LABEL_MAPPINGS[data_root]
    if test_labels is None: 
        continue
    OUT = os.path.join(data_root, 'bleus.out')
    Parallel(n_jobs=8)(delayed(score)(file, test_labels, OUT) for file in gen_targets(data_root))

