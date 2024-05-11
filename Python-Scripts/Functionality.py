import AI

<<<<<<< HEAD
=======
# constants
MessagesPerDay = 11 
LovePoints = 0

>>>>>>> 796f56270138f021e3de41b0973079b98b598e8c
def main():
    relativePath = "../GoodWords.txt"
    Tutorial()    
    gameover = False
    while (gameover is False): #the actual game loop itself
        for days in range(1,6): #the days loop, goes through day 1 to 5
            print(days)
<<<<<<< HEAD
            for messages in range(1,AI.MessagesPerDay): #the messages the user gets per day dictated by the constant
                prompt = input("Enter message here: ")
                message = AI.AIPrint(prompt)
                    
=======
            for messages in range(1, MessagesPerDay): #the messages the user gets per day dictated by the constant
                prompt = input("Enter message here: ")
                message = AI.AIPrint(prompt)
                LovePointsFinder(message)

>>>>>>> 796f56270138f021e3de41b0973079b98b598e8c
        gameover = True


def Tutorial():
    print('Welcome to rizzler university, your goal? rizz up the ai. you have 5 days to get a date gl')
    nameCharacter = input("What is the name of your crush?")


def LovePointsFinder(message):

    wordList = str(message).split

    print(wordList)


<<<<<<< HEAD
def Reader(relativePath):

    f = open(relativePath, "r")
=======

#def Reader():

    #f = open("AIPrompt.txt", "r")
>>>>>>> 796f56270138f021e3de41b0973079b98b598e8c
    
    #print(f.readline())