

def top_bleu(f):
    max_bleu = -1
    max_path = None
    for l in open(f.strip()):
        [path, bleu] = l.strip().split()
        bleu = float(bleu)
        if bleu > max_bleu:
            max_bleu = bleu
            max_path = path
    return max_bleu, max_path



outs = open('OUTS_SMALL')



for file in outs:
    print top_bleu(file)


