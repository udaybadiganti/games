import random
import time
import os
def Players(n,players):
    print("Enter players Names: ")
    print("*********************")
    for i in range(n):
        players.append(input())
    return players
    
def put_Cards(x,y,cards,black,cards1):
    j=(x*len(y))   #sequence of cards
    some=[]
    for i in range(len(y)):
        print("********************")
        print("it's %s turn"%(y[i]))
        print("********************")
        print(black[i])
        for r in range(len(black[i])):
            print(black[i][r])
            if black[i][r]=='King' or black[i][r]=='Queen' or black[i][r]=='Jack':
                black[i][r]=1
            if black[i][r] == 'Ace':
                black[i][r] = 11    
        print("your sum: %d"%(sum(black[i])))
        sum_of_cards=sum(black[i])
        inp=input("you want to play (say 'yes or 1' or 'no or 0'): ")
        cards1=cards
        while(inp =='yes' or inp == '1'):
            print(cards1[j])
            if cards1[j]=='King' or cards1[j]=='Queen' or cards1[j]=='Jack':
                black[i].append(cards1[j])
                cards[j]=1
                sum_of_cards+=1
                if sum_of_cards > 21:
                    print("***********************")
                    print("%s you lose"%y[i])
                    print("***********************\n")
                    break
                if sum_of_cards == 21:
                    print("***********************")
                    print("%s you win"%y[i])
                    print("***********************\n")
                    break
            elif cards1[j] == 'Ace':
                black[i].append(cards1[j])
                cards[j] = 11 
                sum_of_cards+=11
                if sum_of_cards > 21:
                    print("***********************")
                    print("%s you lose"%y[i])
                    print("***********************\n")
                    j+=1
                    break
                if sum_of_cards == 21:
                    print("***********************")
                    print("%s you win"%y[i])
                    print("***********************\n")
                    break
            else:    
                black[i].append(cards1[j])
                sum_of_cards+=cards[j]
                if sum_of_cards > 21:
                    print("***********************")
                    print("%s you lose"%y[i])
                    print("***********************\n")
                    j+=1
                    break
                if sum_of_cards == 21:
                    print("***********************")
                    print("%s you win"%y[i])
                    print("***********************\n")
                    break
            j+=1
            if j == 52:
                print("cards are over please recollect thecards and shuffle it")
                s=int(input("Shuffle the cards 'X' times: "))
                cards = Shuffle(s,cards1)
            print("your sum: %d"%(sum_of_cards))
            inp=input("you want to play (say 'yes or 1' or 'no or 0'): ")
        some.append(sum_of_cards)
        if sum_of_cards == 21:
            for o in range(len(y)-1,len(y[i+1:]),-1):
                some.append(0)
            break;
    print("players cards= ",end='')
    print(black[:len(y)])
    print("players grand totals= ",end='')
    print(some)                    
    return some

def Shuffle(s,cards):
    for i in range(s):
        random.shuffle(cards)
    return cards    
       
def initial_Round(x,y,cards,black):
    l=0
    for j in range(len(y)):
        for i in range(x):
            black[i].append(cards[i+l])
        l+=x
        #print(black[j])

def winner(lis,y):
    #print(lis)
    winn=[ x if 18<= x <= 21 else 0 for x in lis ]
    #print(winn)
    s=winn.index(max(winn))
    if sum(winn) == 0:
        return "No one"
        print(s)
    else: 
        return y[s] 


#Ace,King,Queen,Jack = 11,1,1,1
print("***************************************************************************")
print("                          WEL COME TO LOCAL BLACK JACK                           ")
print("***************************************************************************")

os.system('clear')
cards = ['Ace','Ace','Ace','Ace','King','King','King','King','Queen','Queen','Queen','Queen','Jack','Jack','Jack','Jack',2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10]
cards1=cards
black=[[],[],[],[],[],[],[]]
try:
    n=int(input("Enter How many players(less than 7 is comfortable): "))
except:
    print("invalid entry")
y=Players(n,players=[])
print(y)
s=int(input("Shuffle the cards 'X' times: "))
cards=Shuffle(s,cards)
#print(cards)
x=int(input("How many cards you want to share in initial turn: "))
print("\n**************************************************")
print("IT's TIME TO PLAY")
print("**************************************************")
time.sleep(5)
print("share %d cards to all "%(x))
initial_Round(x,y,cards,black)
print("sharing is done")
time.sleep(3)
lis=put_Cards(x,y,cards,black,cards1)
print("**************************")
print("**************************")
print("     %s is winner"%(winner(lis,y)))
print("**************************")
print("**************************")


