def ShiftLeft1():
        L=[3,4]
        print("This is the original list")
        g=L[0]
        L.pop(0)
        L.append(g)
        print(L)
        print("This is the new list")
        if row1[y] == row1[y+1]:
            row1[y]= row1[y]*2
            row1.pop(y+1)
            row1.insert(3,0)
        elif row1[y] !=0 and row1[y+1] == 0 and row1[y+2]== 0 or row1[y+2]==row1[y]:
            row1[y]=row1[y]*2


row1 = [0,0,2,0]
row2 = [2,2,4,0]
row3 = [2,0,4,4]
row4 = [2,0,2,2]
# left

def ShiftLeft():
    y=0

    for i in range(3):
                
        if row1[y]==0:
            x1=row1[y]
            row1.pop(y)
            row1.append(x1)
            y-=1
        y+=1
    y=0
    for i in range(3):
            
        

        if row1[y] == row1[y+1]:
            row1[y]= row1[y]*2
            row1.pop(y+1)
            row1.insert(3,0)
            if row1[0] == 0:
                row1.pop(0)
                row1.insert(3,0)
        y+=1

      
    if row1[0]==row1[2] and row1[1] == 0 and row1[0] != 0:
        row1[0] = row1[0]*2
        row1.pop(2)
        row1.append(0)
    if row1[0] != 0 and row1[0] != row1[1] and row1[1] == row1[3] and row1[2] == 0:
        row1[1] = row1[1]*2
        row1.pop(3)
        row1.append(0)
    if row1[0] != 0 and row1[3] != 0 and row1[2] == 0 and row1[1] == 0 and row1[0] != row1[3]:
        row1.pop(1)
        row1.append(0)
        
        y+=1
        

    print(y)
            
           
    print(row1)
    
    
    
    
    
    
def testing():
    x= str(1)
    print()
    
    
    if row1[y] == 0:
            x1=row1[y]
            row1.pop(y)
            row1.insert(0,0)
    if row1[3]==row1[1] and row1[2] == 0 and row1[3] != 0:
                row1[3] = row1[3]*2
                row1.pop(1)
                row1.insert(0,0)
    if row1[3] != 0 and row1[3] != row1[2] and row1[2] == row1[0] and row1[1] == 0:
                row1[3] = row1[3]*2
                row1.pop(0)
                row1.insert(0,0)
                
    y=3
    for i in range(3):
        
        if row1[y] == row1[y-1]:
            row1[y]= row1[y]*2
            row1.pop(y-1)
            row1.insert(0,0)
        if row1[3] != 0 and row1[y] == row1[y-1]:
            row1[y-1]= row1[y]*2
            row1.pop(y)
            row1.insert(0,0)
        if row1[3]==row1[1] and row1[2] == 0 and row1[3] != 0:
            row1[3] = row1[3]*2
            row1.pop(1)
            row1.insert(0,0)
            
        if row1[3] != 0 and row1[3] != row1[2] and row1[2] == row1[0] and row1[1] == 0:
            row1[2] = row1[2]*2
            row1.pop(0)
            row1.insert(0,0)
        y=y-1



def ShiftRight():
    row1.reverse()
    ShiftLeft()
    row1.reverse()

    
    
            

            
    print(row1)


def ShiftVertical():
    global column1 
    column1 = [row1[0], row2[0], row3[0], row4[0]]
    
    y=0    

    for i in range(3):
                
        if column1[y]==0:
            x1=column1[y]
            column1.pop(y)
            column1.append(x1)
        y+=1
            
    y=0
    for i in range(3):
        if column1[y] == column1[y+1]:
            column1[y]= column1[y]*2
            column1.pop(y+1)
            column1.insert(3,0)
        y+=1
      
    if column1[0]==column1[2] and column1[1] == 0 and column1[0] != 0:
        column1[0] = column1[0]*2
        column1.pop(2)
        column1.append(0)
        
    if column1[0] != 0 and column1[0] != column1[1] and column1[1] == column1[3] and column1[2] == 0:
        column1[1] = column1[1]*2
        column1.pop(3)
        column1.append(0)
    if column1[0] != 0 and column1[3] != 0 and column1[2] == 0 and column1[1] == 0 and column1[0] != column1[3]:
        column1.pop(1)
        column1.append(0)   
        

    
    

def ShiftUp():
    ShiftVertical()
    row1[0] = column1[0]
    row2[0] = column1[1]
    row3[0] = column1[2]
    row4[0] = column1[3]
    

def ShiftDown():
    global column1
    column1 = row1
    
    
ShiftDown()

print(column1)
print(row2)
print(row3)
print(row4)


    