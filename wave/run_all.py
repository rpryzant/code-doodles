import os

names = ["warmth5", "jumper","binary",'biorhythm','clone','clone2','fortune','gcd','lfsr','maze','memory','pc-ccr','phase2','stm','phase2SIMPLE']
for n in names:
    os.system("testwave -w wave4.is -p pla2.po -t tests/%s.as" %n)
    
