

def ShiftLeft(row1, row2, row3, row4):
    y=0
        

    for i in range(3):    
        if row1[y]==0:
            row1.pop(y)
            row1.append(0)
            y-=1
        y+=1
        
    y=0
    for i in range(3):
        if row1[y] == row1[y+1]:
            row1[y+1]= row1[y]*2
            row1.pop(y)
            row1.insert(3,0)
        y+=1
            
        
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
            
            
            
    y=0
    for i in range(3):    
        if row4[y]==0:
            row4.pop(y)
            row4.append(0)
            y-=1
        y+=1
        
    y=0
    for i in range(3):
        if row4[y] == row4[y+1]:
            row4[y+1]= row4[y]*2
            row4.pop(y)
            row4.insert(3,0)
        y+=1
          
            
        
            

    
            
            

   
        
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
    

    

def ShiftUp(row1, row2, row3, row4):
    
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

    
    global column1, column2, column3, column4
    
    column1 = [row4[0], row3[0], row2[0], row1[0]]
    
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
        

    
    
    

    column2 = [row4[1], row3[1], row2[1], row1[1]]
    
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
      
        
    


    column3 = [row4[2], row3[2], row2[2], row1[2]]
    
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
        





    column4 = [row4[3], row3[3], row2[3], row1[3]]
    
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
    





