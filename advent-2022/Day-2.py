file=open('Day-2.txt')


count=0
for i in file.readlines():
    value=i.split('\n')[0]
    num=0
    if(value[0] =="A" and value[1]=="Y"):
        num=8
    elif(value[0] =="A" and value[1]=="X"):
        pass  
    elif(value[0] =="A" and value[1]=="Z"):
        pass  
    elif(value[0] =="B" and value[1]=="Y"):
        pass  
    elif(value[0] =="B" and value[1]=="X"):
        pass  
    elif(value[0] =="B" and value[1]=="Z"):
        pass  
    elif(value[0] =="C" and value[1]=="Y"):
        pass
    elif(value[0] =="C" and value[1]=="X"):
        pass  
    elif(value[0] =="C" and value[1]=="Z"):
        pass       