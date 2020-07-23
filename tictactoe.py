from random import randint
import time
def choice():
    print("Enter ur choice 'X' or 'O'")
    player=input().upper()
    if player=='X':
        return ['X','O']
    else:
        return ['O','X']

def first_turn():
    if randint(0,1)==0:
        turn='X'
    else:
        turn='O'
    return turn

def draw(L):
    print(L[0],"  |  ",L[1],"  |  ",L[2],end="")
    print("")
    print("------------------")
    print(L[3],"  |  ",L[4],"  |  ",L[5],end="")
    print("")
    print("------------------")
    print(L[6],"  |  ",L[7],"  |  ",L[8],end="")

    
def checkwinner(L,turn):
    #horizontal 1
    if (L[0]==turn and L[1]==turn and L[2]==turn):
        return True
    #horizontal 2
    elif (L[3]==turn and L[4]==turn and L[5]==turn):
        return True
    #horizontal 3
    elif (L[6]==turn and L[7]==turn and L[8]==turn):
        return True
    #vertical 1
    elif (L[0]==turn and L[3]==turn and L[6]==turn):
         return True
    #vertical 2
    elif (L[1]==turn and L[4]==turn and L[7]==turn):
         return True
    #vertical 3
    elif ( L[2]==turn and L[5]==turn and L[8]==turn):
         return True
    #diagonal left
    elif ( L[0]==turn and L[4]==turn and L[8]==turn):
         return True
    #diagonal right
    elif (L[2]==turn and L[4]==turn and L[6]==turn):
           return True
    else:
        return False
def user(L):
    global pos
    print("Your turn")
    print("Enter the position(1-9)")
    pos=int(input())
    if L[pos-1]=='':
        L[pos-1]=player
        draw(L)
    else:
        print("Enter a valid position")
        user(L)
    
    return   

def copyboard(L):
    duplboard=[]
    for x in L:
        duplboard.append(x)
    return duplboard    
    

   
             
def block(L):
    flag=0
    cb=copyboard(L)
    for i in range(0,9):
        if cb[i]=='':
            cb[i]=player
            if checkwinner(cb,player)==True:
                L[i]=cpu
                flag=1
                break
            else:
                cb[i]=''
    if flag==0:
        trick(L)
    return
def trick(L):
    cb=copyboard(L)
    for x in range(0,9):
        winmove=0
        if cb[x]=='':
            cb[x]=cpu
        for y in range(0,9):
            if cb[y]!='':
                continue
            else:
                cb[y]=cpu
                if checkwinner(cb,cpu)==True:
                    winmove+=1
                    temp=x
                else:
                    cb[y]=''
                if winmove==2:
                    L[x]=cpu
                    break
        break
    if winmove==1:
        L[x]=cpu
    elif winmove==0:
        for y in range(0,9):
            if L[y]=='':
                L[y]=cpu
                break
            
    return

def move(L):
    flag=0
    cb=copyboard(L)
    for i in range(0,9):
        if cb[i]=='':
            cb[i]=cpu
            if checkwinner(cb,cpu):
                L[i]=cpu
                flag=1
                break
            else:
                cb[i]=''
    if flag==0:
        block(L)
    return
            
          


   
             


        

def com(L,count):
    print("CPU's turn")
    if turnfirst==cpu:
        if count==1:
            L[4]=cpu
        if count==3:
            if pos==2:
                L[6]=cpu
            elif pos==4:
                L[2]=cpu
            elif pos==8:
                L[0]=cpu
            elif pos==6:
                L[0]=cpu
            if pos==1:
                L[8]=cpu
            elif pos==3:
                L[6]=cpu
            elif pos==7:
                L[2]=cpu
            elif pos==9:
                L[0]=cpu
        
        if count>3:
            move(L)
    
        

    if turnfirst==player:
        s=0
        if count==2:
            if pos==1 or pos==3 or pos==7 or pos==9:
                s=1
                L[4]=cpu
            if pos==2 or pos==4:
                L[0]=cpu
            elif pos==6 or pos==8:
                L[8]=cpu
            if pos==5:
                s=2
                L[6]=cpu
        if count==4:
           if s==1:
               if pos==3:
                   L[7]=cpu
               else:
                    move(L)
           if s==2:
                if pos==3:
                    L[0]=cpu
                else:
                    move(L)
           if s==0:
                move(L)

        if count>4:
            move(L)
    draw(L)
    return            
               
           
            

print("Welcome to Tic Tac Toe")

while True:
    L=['']*9
    draw(L)
    print()
    count=0
    player,cpu=choice()
    turn=first_turn()
    turnfirst=turn
    print(turn,"goes first")
    mode=True
    while mode:
        if turn==player:
            user(L)
            print()
            count+=1
            if checkwinner(L,turn):
                print(turn,"is the winner")
                mode=False
            elif count==9 and checkwinner(L,turn)==False:
                print("GAME TIED")
                break
            else:
                turn=cpu
        else:
            count+=1
            time.sleep(0.3)
            com(L,count)
            print()
            if checkwinner(L,turn):
                print("COMPUTER BEAT YOU")
                mode=False
            elif count==9 and checkwinner(L,turn)==False:
                 print("GAME TIED")
                 break
            else:
                turn=player
    print("DO U WANT TO PLAY AGAIN(Y/N)")
    if input().upper()=='N':
        break



           
            
    
        
        
            
                
                
                
            
        
        
    

