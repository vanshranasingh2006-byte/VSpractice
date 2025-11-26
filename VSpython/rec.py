i=1
a=int(input("enter the number of element u want to sum: "))
sl=[]
while i<=a:
    no=int(input(f"pls enter the {i} number: "))
    sl.append(no)
    i+=1

s2=0
total=0
while s2<len(sl):
    total+=sl[s2]
    s2+=1
print(f"ur total sum of {a} is {total}")
    

    