import random
import time

n = int(input("How many sets you want to play\n"))              ##setting number of games

countCPU = 0
countuser = 0
countdraw = 0

t = ('rock', 'paper','scissor')                                 ##CPU choosing
CPU = random.choice(t)

while n:
    print("Choose one of them:\nRock ,Paper, Scissor")          ##user choosing
    Input = input("You:")
    user = Input.lower()
    if user not in t:
        print("wrong input\n")
    else:
        
        print("CPU:",CPU)
        
    #data()

        if CPU == 'paper'and user == 'rock' or CPU == 'scissor'and user == 'paper'or CPU=='rock'and user =='scissor':
            print("CPU won")
            print("\n")             ####CPU WON
            time.sleep(1)
            countCPU+=1
        elif CPU == 'paper'and user == 'scissor' or CPU == 'rock'and user == 'paper'or CPU=='scissor'and user =='rock':
            print("You won")
            print("\n")             #####USER WON
            time.sleep(1)
            countuser+=1
        else:
            countdraw+=1
            print("draw")           #####DRAW
            print("\n")
            time.sleep(1)
    n-=1

                                    ##########OVERALL RESULT
print("*"*50)
print("CPU won:",countCPU,"times\n")
print("You won:",countuser,"times\n")
print("draws:", countdraw,"times\n")

                            #############FINAL RESULT

if countCPU>countuser:
    print("FINAL RESULT: CPU is the WINNER",end=" ")
elif countuser>countCPU:
    print("FINAL RESULT : YOU r WINNER",end=" ")
else: print("FINAL RESULT: Its a DRAW",end=" ")

print("*"*50)





