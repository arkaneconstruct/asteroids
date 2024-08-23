CURRENT_SCORE = 0
HIGH_SCORE = 0
SCORE_FILE = 'score.txt'

def Score():
    global HIGH_SCORE 
    global SCORE_FILE
    f = open(SCORE_FILE,"r")
    HIGH_SCORE += int(f.read())
    f.close()
    
def EndScore():
    if CURRENT_SCORE > HIGH_SCORE:
        f = open(SCORE_FILE,"w")
        f.write(str(CURRENT_SCORE))
        f.close()
    return