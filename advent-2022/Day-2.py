file=open('Day-2.txt')

list_dict={"A":0,"B":0,"C":0,"Y":0,"X":0,"Z":0}
count=0
for i in file.readlines():
    print(i.split('\n')[0])
    if count==5:
        break
    count+=1