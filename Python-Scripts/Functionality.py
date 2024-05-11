import AI

# constants
MessagesPerDay = 11 
LovePoints = 0

def main():
    Tutorial()    
    gameover = False
    while (gameover is False): #the actual game loop itself
        for days in range(1,6): #the days loop, goes through day 1 to 5
            print(days)
            for messages in range(1, MessagesPerDay): #the messages the user gets per day dictated by the constant
                prompt = input("Enter message here: ")
                message = AI.AIPrint(prompt)
                LovePointsFinder(message)

        gameover = True


def Tutorial():
    print('Welcome to rizzler university, your goal? rizz up the ai. you have 5 days to get a date gl')
    nameCharacter = input("What is the name of your crush?")


def LovePointsFinder(message):

    wordList = str(message).split

    for word in wordList:
        for goodline in goodwords:
            if (goodline == word):
                LovePoints = LovePoints + 1
        for badline in badwords:
            if (badline == word):
                LovePoints = LovePoints - 1


#def Reader():

    #f = open("AIPrompt.txt", "r")
    
    #print(f.readline())