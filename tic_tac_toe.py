# TIC TAC TOE


mat = [[1,2,3],[4,5,6],[7,8,9]]
import os
def table():
    os.system('clear')
    for i in range(3):
        print(" | ",end = "")
        for j in range(3):
            print(mat[i][j],end =" | ")
        print(" ")

def win(x):
    os.system('clear')
    if x == 'x':
        return "player1 is Winner"
    elif x == 'o':
        return "player2 is Winner"
    else:
        return 'draw'

def win_pattern(mat):
    for i in range(3):
        j=0
        if mat[i][j] == mat[i][j+1] == mat[i][j+2]:
            return win(mat[i][j])
            break
    i=0
    for j in range(3):
        if mat[i][j] == mat[i+1][j] == mat[i+2][j]:
            	return win(mat[i][j])
            	break
    if mat[0][0] == mat[1][1] == mat[2][2]:
        return win(mat[i][j])
    if mat[2][0] == mat[1][1] == mat[0][2]:
        return win(mat[2][0])
'''
def choice(mat,x):
    n = int(input("enter your position: "))
    try:
        if (n/3)<=1:
            mat[0][mat[0].index(n)] = x[]
            table()
            win_pattern(mat)
        elif ((n/3)>1) or ((n/3) == 2):
            mat[1][mat[1].index(n)] = x[]
            table()
            win_pattern(mat)
        elif ((n/3)>2) or ((n/3) == 3):
            mat[2][mat[2].index(n)] = x[]
            table()
            win_pattern(mat)        
    except:
        print("input error")
        n = int(input("enter your position: "))
        continue
'''

def choice(mat,x):
    w = []
    for i in range(10):
        #print(i)
        #print(w)
        if ('player1 is Winner' in w) or ('player2 is Winner' in w):
            print("%s"%w.pop())
            break
        n = int(input("enter your position: "))
        try:
            print("continueing")
            if (n/3)<=1:
                mat[0][mat[0].index(n)] = x[i]
                table()
                w.append(win_pattern(mat))
            elif ((n/3)>2) or ((n/3) == 3):
                mat[2][mat[2].index(n)] = x[i]
                table()
                w.append(win_pattern(mat))   
            elif ((n/3)>1) or ((n/3) == 2):
                mat[1][mat[1].index(n)] = x[i]
                table()
                w.append(win_pattern(mat))
        except:
            print("input error")
            i=i-1
'''

def choice(mat,x):
    w = []
    s= ''
    for i in range(10):
        if s == 'exc':
            i=i-1
        try:
            if ('player1 is Winner' in w) or ('player2 is Winner' in w):
                print("%s"%w.pop())
                break
            n = int(input("enter your position: "))
            if (n/3)<=1:
                mat[0][mat[0].index(n)] = x[i]
                table()
                w.append(win_pattern(mat))
            elif ((n/3)>2) or ((n/3) == 3):
                mat[2][mat[2].index(n)] = x[i]
                table()
                w.append(win_pattern(mat))   
            elif ((n/3)>1) or ((n/3) == 2):
                mat[1][mat[1].index(n)] = x[i]
                table()
                w.append(win_pattern(mat))
            s = ''
        except:
            s="exc"
            print(s)
            print("input error")
            print(i)
            continue
'''
          
table()
y=['x','o','x','o','x','o','x','o','x']
x=y
choice(mat,x)
