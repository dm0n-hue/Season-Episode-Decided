import random

def getSeason(Season):
    Season = random.randint(1,3)
    return Season

answerSeason = 0
answerSeason = getSeason(answerSeason)
print('Season ' + str(answerSeason))

def getEp(Ep):
    Ep = random.randint(1,21)
    return Ep

answerEp = 0
answerEp = getEp(answerEp)
print('Episode ' + str(answerEp))
