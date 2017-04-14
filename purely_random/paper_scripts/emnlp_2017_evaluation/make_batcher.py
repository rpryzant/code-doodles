

dirs = open('DIRS.txt')

for i, d in enumerate(dirs):
    machine = str(i + 10)
    d = d.strip()
    print "ssh jude%s 'sh /scr/rpryzant/evaluation/run_job.sh %s > OUT%s 2>ERR%s &" % (machine, d, machine, machine)
