import AI

def main():
    relativePath = "../GoodWords.txt"
    Tutorial()    
    gameover = False
    while (gameover is False): #the actual game loop itself
        for days in range(1,6): #the days loop, goes through day 1 to 5
            print(days)
            for messages in range(1,AI.MessagesPerDay): #the messages the user gets per day dictated by the constant
                prompt = input("Enter message here: ")
                message = AI.AIPrint(prompt)
                    
        gameover = True
        #f = AIPrint("say yo mama")
        #print(f)
        
        #print(gameover)


def Tutorial():
    print('Welcome to rizzler university, your goal? rizz up the ai. you have 5 days to get a date gl')
    nameCharacter = input("What is the name of your crush?")


def LovePoints():

    meter = 0

    prompt = "fuiagfa"


def Reader(relativePath):

    f = open(relativePath, "r")
    
    print(f.readline())