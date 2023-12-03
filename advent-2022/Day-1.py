file=open('file.txt')
lst=[]
count=0
singlesum=0
for i in file.readlines():
    sp=i.split('\n')[0]
    if(sp!=''):
        singlesum+=int(sp)
    elif(sp==''):
        lst.append(singlesum)
        singlesum=0
    
print(len(lst))
print(max(lst))