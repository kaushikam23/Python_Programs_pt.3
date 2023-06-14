import re
try:
    name=input("Enter filename")
    fhand=open(name,'r')
    s=[]
    sum=0
    for line in fhand:
        line=line.rstrip()
        x= re.findall('^X-\S*: ([0-9.]+)', line)
        s.append(x)

    print(s)
    for i in range(len(s)):
        sum+= float(s[i][0])
    
    print(sum/len(s))

except FileNotFoundError:
    print("Error opening the file")
