import AI

# constants
MessagesPerDay = 50
MessageCount = 0
MessagesForDate =  250
LovePoints = 0

def main():

    Tutorial()
    MessageCount = 0    
    gameover = False
    
    while (gameover is False): #the actual game loop itself
        for days in range(1,6): #the days loop, goes through day 1 to 5
            print(days)
            while(prompt != "s" or  MessagesPerDay > MessageCount): #the messages the user gets per day dictated by the constant
                prompt = input("Enter message here: ")
                message = AI.AIPrint(prompt) #what the Ai says
                LovePointsFinder(message)
                MessageCount += 1
        
        if(LovePoints == 80):
            while(prompt != "s" or  MessagesForDate > MessageCount): #the messages the user gets per day dictated by the constant
                prompt = input("Enter message here: ")
                message = AI.AIPrint(prompt) #what the Ai says
                LovePointsFinder(message)
                MessageCount += 1



        gameover = True


def Tutorial():
    print('Welcome to rizzler university, your goal? rizz up the ai. you have 5 days to get a date gl')
    nameCharacter = input("What is the name of your crush?")


def LovePointsFinder(message):

    wordList = str(message).split

    for word in wordList:

        relativePath = "../textfiles/goodwords" #path for the good words
        goodwords = open(relativePath, "r") #opens the goodwords file
        for goodline in goodwords:
            if (goodline == word):
                LovePoints += 1
        goodwords.close()

        relativePath = "../textfiles/badwords" #path for the bad words
        badwords = open(relativePath, "r") #opens the badwords file
        for badline in badwords:
            if (badline == word):
                LovePoints -= 1
        badwords.close() #closes the file
