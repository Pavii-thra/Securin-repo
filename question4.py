dieA = [1,2,3,4,5,6]
dieB = [1,2,3,4,5,6]


l = [1,2,3,4,5,6,7,8,9,10,11]


def transform_undoom(dieA,dieB):
    
    DieA = [1,2,3,4,0,0]
    DieB = [1]
    hist = {
        2 : 1,
        3 : 2,
        4 : 3,
        5 : 4,
        6 : 5,
        7 : 6,
        8 : 5,
        9 : 4,
        10 : 3,
        11 : 2,
        12 : 1
    }
    # print(hist)
    for i in DieA:
        if i!=0:
            sumi=i+1
            hist[sumi]-=1
    
    
    
    k=1
    i=4
    j=0
    while j<2:
        
        sumi = k+1
        if(hist[sumi]-1<0):
            k+=1
        else:
            hist[sumi]-=1
            DieA[i]=k
            j+=1
            i+=1
            k=1
        
        
    
    
    
   
    
    
    i=0
    j=0
    k=2
    
    while(j<5):
        
        
        newHist = hist
        
        while(i<6):
            
            a = DieA[i]
            sumi = a + k
            if(newHist[sumi]-1<0):
            
                i=0
                k+=1
                newHist = hist
                # print(newHist)
                
            else:
                newHist[sumi]-=1
                i+=1
                
        DieB.append(k)
        print(hist,k)   
        j+=1
        i=0
        hist = newHist
        k+=1
        
    print("New Die A :",DieA) 
    print("New Die B :",DieB) 




transform_undoom(dieA,dieB)