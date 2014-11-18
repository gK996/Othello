import random 
import turtle as t
import math


"""
Othello board game

Author: George Krlevski
"""


def initialiseBoard(n):
    n1 =int((n/2)-1)
    n2= int(n/2)
    #[x][y] co-ord
    
    b= [[0 for j in range(n)]for i in range(n)]
    
    b[n1][n1]=1
    b[n2][n2]= 1
    #Black
    b[n1][n2]= -1
    b[n2][n1]= -1
    #White
    return b



def drawBoard(b):
    #set up window
    t.setup(600,600)
    t.bgcolor("dark green")
    
    #turtle settings
    t.hideturtle()
    t.speed(0)
    
    num=len(b)
    side=600/num
    xcod=-300
    ycod=-300
    for x in b:
        for y in x:
            if(y> 0):
                drawsquare(xcod,ycod,side,'black')
            if(y< 0):
                drawsquare(xcod,ycod,side,'white')
            if(y==0):
                drawsquare(xcod,ycod,side,'dark green')
            
            xcod=xcod+side
        xcod=-300
        ycod=ycod+side
        
        
def drawsquare(x,y,length,col):
    t.penup()
    t.setposition(x,y)
    t.pendown()
    t.begin_fill()
    t.color(col)
    t.pencolor('yellow')
    for x in range(0,4,1):
        t.forward(length)
        t.left(90)
    t.end_fill()

def move(b,m,p):
    for x in range(len(m[2])):  
        r= m[0]
        c= m[1]
        b[r][c]=p

        if p==1:
            r+=m[2][x][0]
            c+=m[2][x][1]
            
            while b[r][c] < 0:
                b[r][c] = toChange(b[r][c],p)
                r+= m[2][x][0]
                c+= m[2][x][1]

        if p==-1:
            r+=m[2][x][0]
            c+=m[2][x][1]
            
            while b[r][c] > 0:
                b[r][c] = toChange(b[r][c],p)
                r+= m[2][x][0]
                c+= m[2][x][1]
                    
    return b

def toChange(val,p):
    #changes value
    x= val
    if x == 0:
        pass
    elif p ==1:
        x= (abs(x) +1)
    elif p==-1:
        x=(abs(x)*-1)-1
    return x
    
def legalDirection(r,c,b,p,u,v):
            
    i= r
    j=c
    f=0
    
    while True:
        #left
        if  v ==-1:
            j+=-1
            if j< 0:
                break
        #right
        if v==1:
            j +=1
            if  j>(len(b)-1):
                break
        #down
        if u==-1:
            i+=-1
            if i<0 :
                break     
        #up
        if u == 1:
            i+=1
            if  i> (len(b)-1):
                break

        
        if b[i][j] ==0:
            break
        

        #checks opposite
        if b[i][j]*p <0: 
            f= 1

        #same and opposite
        if b[i][j]*p >0 and f == 1: 
            
            return True


    return False

                

            

def legalMove(r,c,b,p):
    #returns all moves that are legal
    moves=[]
    for u in[-1,0,1]:
        for v in[-1,0,1]:
            if [u,v] ==[0,0]:
                continue
            if legalDirection(r,c,b,p,u,v)!=False:
                moves.append((u,v))
    return moves

                 
                 
def moves(b,p):
    #lists all possible moves for player p on board b.
    moves=[]
    for r in range(len(b)):
        for c in range(len(b)):
            if b[r][c]==0:
                if len(legalMove(r,c,b,p)) > 0:
                    moves.append((r,c,(legalMove(r,c,b,p))))
    return moves

    
def selectMove(ms,b,p):
    #ms= moves(b,p)
    strategy=  randomChoice(ms)

    #error case   
    if strategy == []:
        return 0
    
    return strategy

def randomChoice (ms):
    # returns choice chosen at random
    y= [i for i,x in enumerate(ms)]
    choice = random.randint(0, len(y)-1)
    z= y[choice]
    
    return ms[z]
    


def scoreBoard(b):
    black, white=0,0
    #initialising variables
    
    for i in range(len(b)):
        for j in range (len(b)):
            piece= b[i][j]            
            if(b[i][j]<0):
                white+=-piece
            if(b[i][j] >0):
                black+=piece
            
    return (black,abs(white))

def find(b):
    for x in b:
        for y in x:
            if y == 0:
                continue
                

def main():
    """ propmts user for player, board size and it conducts the game"""
    
    print('Welcome to Othello')
    print()
    x= str(input("Enter Player: Black or White: " ))
    x.strip().lower()
    if x == "black":
        p=1
    else:
        p =-1

    #computer 
    comp = p*(-1)#opposite p
    n= int(input("Enter board size: "))
    b= initialiseBoard(n)
    drawBoard(b)
    
    while True:
        #user
        print("Your move.")
        toMove= moves(b,p)
        if toMove == []:
            break
        possibleMoves =[]
        for x in toMove:
                possibleMoves.append((x[0],x[1]))
        print("Possible moves: ", possibleMoves)
        
        print("Enter move: ")
        r=int(input("row: "))
        c=int(input("column: "))

        #make move
        for x in toMove:
            if r == x[0] and c ==x[1]:
                b= move(b,x,p)
        drawBoard(b)

        #comp
        print("Computer's move.")
        ms= moves(b, comp)
        if ms ==[]:
            break
        m= selectMove(ms,b,p)
        #no available moves
        if m==0:
            break
        
        b = move(b,m,comp)
        drawBoard(b)
        
        # if board is full
        find(b)

    print("************Game Ended!************")
    score= scoreBoard(b)
    print('Score: ', score)
    input("Hit enter to finish: ")
