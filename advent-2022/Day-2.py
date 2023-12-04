file=open('Day-2.txt')

count=0
for i in file.readlines():
    print(i.split('\n')[0])
    if count==5:
        break
    count+=1