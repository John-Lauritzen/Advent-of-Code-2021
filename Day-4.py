# Test Data
testcalls = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
testcalls2 = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24]
testcards = [
    [[22, 13, 17, 11, 0], 
     [8, 2, 23, 4, 24],
     [21, 9, 14, 16, 7],
     [6, 10, 3, 18, 5],
     [1, 12, 20, 15, 19]],
    [[3, 15, 0, 2, 22],
     [9, 18, 13, 17, 5],
     [19, 8, 7, 25, 23],
     [20, 11, 10, 24, 4],
     [14, 21, 16, 12, 6]],
    [[14, 21, 17, 24, 4],
     [10, 16, 15, 9, 19],
     [18, 8, 23, 26, 20],
     [22, 11, 13, 6, 5],
     [2, 0, 12, 3, 7]]]
#End Test Data

def loadcalls (day4callsfile):
    day4calls = open(day4callsfile, "r")

    rawcalls = day4calls.read()
    rawcalllist = rawcalls.split(',')
    calllist = [int(val) for val in rawcalllist]

    day4calls.close()
    return calllist


def loadcards (day4cardsfile):
    day4cards = open(day4cardsfile, "r")
    cardlist = []
    tempcard = []
    for line in day4cards:
        rawcards = line.strip()
        if rawcards == '':
            cardlist.append(tempcard[:])
            tempcard.clear()
        else:
            rawcardrow = rawcards.split(' ')
            for i in rawcardrow:
                if i == '':
                    rawcardrow.remove('')
            intcardrow = [int(val) for val in rawcardrow]
            tempcard.append(intcardrow)
    day4cards.close()
    return cardlist

def checkRowBingo (calls, cardlist, card, row):
    matchcount = 0
    for col in range(len(cardlist[card][row])):
        if cardlist[card][row][col] in calls:
            matchcount += 1
    if matchcount == len(cardlist[card][row]):
        return True
    else:
        return False

def checkColBingo (calls, cardlist, card, col):
    matchcount = 0
    for row in range(len(cardlist[card])):
        if cardlist[card][row][col] in calls:
            matchcount += 1
    if matchcount == len(cardlist[card]):
        return True
    else:
        return False

def checkforBingo (calls, cardlist, card):
    bingo = False
    maxrows = len(cardlist[card])
    maxcols = len(cardlist[card][0])
    currentrow = 0
    currentcol = 0
    while bingo is False and currentrow < maxrows and currentcol < maxcols:
        bingo = checkColBingo(calls, cardlist, card, currentcol)
        if bingo is False:
            bingo = checkRowBingo(calls, cardlist, card, currentrow)
        currentrow += 1
        currentcol += 1
    return bingo

def scoreBingo (calls, currentcall, cardlist, card):
    score = 0
    for row in range(len(cardlist[card])):
        for value in range(len(cardlist[card][row])):
            if cardlist[card][row][value] not in calls:
                score += cardlist[card][row][value]
    return score * currentcall

def runBingo (calllist, cardlist):
    callnumber = 0
    currentcall = 0
    cards = len(cardlist)
    calls =[]
    bingo = False
    while bingo is False:
        currentcall = calllist[callnumber]
        calls.append(currentcall)
        callnumber += 1
        card = 0
        while bingo is False and card in range(cards):
            bingo = checkforBingo(calls, cardlist, card)
            if bingo is True:
                score = scoreBingo(calls, currentcall, cardlist, card)
                print('The winner is card', card, 'with a score of', score)
                return card
            card += 1

def findLastBingo(calllist, cardlist):
    if len(cardlist) == 1:
        print('The last winning card!')
        runBingo(calllist, cardlist)
    else:
        winner = runBingo(calllist, cardlist)
        remainingcards = cardlist[:]
        del remainingcards[winner]
        findLastBingo(calllist, remainingcards)



#print(checkforBingo(testcalls2, testcards, 2))
#print(scoreBingo(testcalls2, 24, testcards, 2))
#runBingo(testcalls, testcards)

callfile = "Day4-Calls.txt"
cardfile = "Day4-Cards.txt"

calllist = loadcalls(callfile)
cardlist = loadcards(cardfile)

runBingo(calllist, cardlist)

findLastBingo(calllist, cardlist)