
row1 = [0,0,2,2]
row2 = [0,0,2,0]
row3 = [2,4,0,4]
row4 = [0,0,4,4]
# left


def ShiftLeft(row1, row2, row3, row4):
    y=0
        

    for i in range(3):
                
        if row1[y]==0:
            row1.pop(y)
            row1.append(0)
        y+=1
    
    y=0
    for i in range(3):
        
        

        if row1[y] == row1[y+1]:
            row1[y]= row1[y]*2
            row1.pop(y+1)
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
            
            
    y=0
    for i in range(3):
        if row2[y]==0:
            row2.pop(y)
            row2.append(0)
            y-=1
        y+=1
        
        
    y=0
    for i in range(3):
        if row2[y] == row2[y+1]:
            row2[y+1]= row2[y]*2
            row2.pop(y)
            row2.insert(3,0)
        y+=1

                
    if row2[0]==row2[2] and row2[1] == 0 and row2[0] != 0:
        row2[0] = row2[0]*2
        row2.pop(2)
        row2.append(0)
        
    if row2[0] != 0 and row2[0] != row2[1] and row2[1] == row2[3] and row2[2] == 0:
        row2[1] = row2[1]*2
        row2.pop(3)
        row2.append(0)
    if row2[0] != 0 and row2[3] != 0 and row2[2] == 0 and row2[1] == 0 and row2[0] != row2[3]:
        row2.pop(1)
        row2.append(0)
            
            
            
            
            
    y=0
    for i in range(3):            
        if row3[y]==0:
            row3.pop(y)
            row3.append(0)
            y-=1
        y+=1
        
    y=0
    for i in range(3):
        if row3[y] == row3[y+1]:
            row3[y+1]= row3[y]*2
            row3.pop(y)
            row3.insert(3,0)
        y+=1
        
          
    if row3[0]==row3[2] and row3[1] == 0 and row3[0] != 0:
        row3[0] = row3[0]*2
        row3.pop(2)
        row3.append(0)
        
    if row3[0] != 0 and row3[0] != row3[1] and row3[1] == row3[3] and row3[2] == 0:
        row3[1] = row3[1]*2
        row3.pop(3)
        row3.append(0)
    if row3[0] != 0 and row3[3] != 0 and row3[2] == 0 and row3[1] == 0 and row3[0] != row3[3]:
        row3.pop(1)
        row3.append(0)
            
            
            
            
            
            
    y=0
    for i in range(3):    
        if row4[y]==0:
            row1.pop(y)
            row1.append(0)
            y-=1
        y+=1
        
    y=0
    for i in range(3):
        if row4[y] == row4[y+1]:
            row4[y+1]= row4[y]*2
            row4.pop(y)
            row4.insert(3,0)
        y+=1
          
    if row4[0]==row4[2] and row4[1] == 0 and row4[0] != 0:
        row4[0] = row4[0]*2
        row4.pop(2)
        row4.append(0)
        
    if row4[0] != 0 and row4[0] != row4[1] and row4[1] == row4[3] and row4[2] == 0:
        row4[1] = row4[1]*2
        row4.pop(3)
        row4.append(0)
    if row4[0] != 0 and row4[3] != 0 and row4[2] == 0 and row4[1] == 0 and row4[0] != row4[3]:
        row4.pop(1)
        row4.append(0)
        
            
        
            

    
            
            

   
        
def ShiftRight(row1, row2, row3, row4):
    row1.reverse()
    row2.reverse()
    row3.reverse()
    row4.reverse()
    ShiftLeft(row1, row2, row3, row4)
    row1.reverse()
    row2.reverse()
    row3.reverse()
    row4.reverse()
    

    

def ShiftVertical(row1, row2, row3, row4):
    
    global column1, column2, column3, column4
    
    column1 = [row1[0], row2[0], row3[0], row4[0]]
    
    y=0    

    for i in range(3):
                
        if column1[y]==0:
            column1.pop(y)
            column1.append(0)
            y-=1
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
        

    
    
    

    column2 = [row1[1], row2[1], row3[1], row4[1]]
    
    y=0    

    for i in range(3):
                
        if column2[y]==0:
            column2.pop(y)
            column2.append(0)
            y-=1
        y+=1
            
    y=0
    for i in range(3):
        if column2[y] == column2[y+1]:
            column2[y]= column2[y]*2
            column2.pop(y+1)
            column2.insert(3,0)
        y+=1
      
    if column2[0]==column2[2] and column2[1] == 0 and column2[0] != 0:
        column2[0] = column2[0]*2
        column2.pop(2)
        column2.append(0)
        
    if column2[0] != 0 and column2[0] != column2[1] and column2[1] == column2[3] and column2[2] == 0:
        column2[1] = column2[1]*2
        column2.pop(3)
        column2.append(0)
    if column2[0] != 0 and column2[3] != 0 and column2[2] == 0 and column2[1] == 0 and column2[0] != column2[3]:
        column2.pop(1)
        column2.append(0)   
        
    


    column3 = [row1[2], row2[2], row3[2], row4[2]]
    
    y=0    

    for i in range(3):
                
        if column3[y]==0:
            column3.pop(y)
            column3.append(0)
            y-=1
        y+=1
            
    y=0
    for i in range(3):
        if column3[y] == column3[y+1]:
            column3[y]= column3[y]*2
            column3.pop(y+1)
            column3.insert(3,0)
        y+=1
      
    if column3[0]==column3[2] and column3[1] == 0 and column3[0] != 0:
        column3[0] = column3[0]*2
        column3.pop(2)
        column3.append(0)
        
    if column3[0] != 0 and column3[0] != column3[1] and column3[1] == column3[3] and column3[2] == 0:
        column3[1] = column3[1]*2
        column3.pop(3)
        column3.append(0)
    if column3[0] != 0 and column3[3] != 0 and column3[2] == 0 and column3[1] == 0 and column3[0] != column3[3]:
        column3.pop(1)
        column3.append(0)   
        




    column4 = [row1[3], row2[3], row3[3], row4[3]]
    
    y=0    

    for i in range(3):
                
        if column4[y]==0:
            column4.pop(y)
            column4.append(0)
            y-=1
        y+=1
            
    y=0
    for i in range(3):
        if column4[y] == column4[y+1]:
            column4[y]= column4[y]*2
            column4.pop(y+1)
            column4.insert(3,0)
        y+=1
      
    if column4[0]==column4[2] and column4[1] == 0 and column4[0] != 0:
        column4[0] = column3[0]*2
        column4.pop(2)
        column4.append(0)
        
    if column4[0] != 0 and column4[0] != column4[1] and column4[1] == column4[3] and column4[2] == 0:
        column4[1] = column2[1]*2
        column4.pop(3)
        column4.append(0)
    if column4[0] != 0 and column4[3] != 0 and column4[2] == 0 and column4[1] == 0 and column4[0] != column4[3]:
        column4.pop(1)
        column4.append(0)   
        





def ShiftUp(row1, row2, row3, row4):
    ShiftVertical(row1, row2, row3, row4)
    row1[0] = column1[0]
    row2[0] = column1[1]
    row3[0] = column1[2]
    row4[0] = column1[3]
    
    
    row1[1] = column2[0]
    row2[1] = column2[1]
    row3[1] = column2[2]
    row4[1] = column2[3]

    row1[2] = column3[0]
    row2[2] = column3[1]
    row3[2] = column3[2]
    row4[2] = column3[3]

    
    row1[3] = column4[0]
    row2[3] = column4[1]
    row3[3] = column4[2]
    row4[3] = column4[3]
    

def ShiftDown(row1, row2, row3, row4):
    ShiftVertical(row1, row2, row3, row4)
    row1[0] = column1[3]
    row2[0] = column1[2]
    row3[0] = column1[1]
    row4[0] = column1[0]
    
    
    row1[1] = column2[3]
    row2[1] = column2[2]
    row3[1] = column2[1]
    row4[1] = column2[0]

    row1[2] = column3[3]
    row2[2] = column3[2]
    row3[2] = column3[1]
    row4[2] = column3[0]

    
    row1[3] = column4[3]
    row2[3] = column4[2]
    row3[3] = column4[1]
    row4[3] = column4[0]


ShiftLeft(row1, row2, row3, row4)
print(row2)
