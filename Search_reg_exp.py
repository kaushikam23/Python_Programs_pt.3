import re
try:
    name=input("Enter file name")
    fhand=open(name,'r')

    for line in fhand:
        line=line.rstrip()
        if(re.search('^[Ff]rom',line)):
            x=re.findall('\S+@+\S+',line)
            if(len(x)>0):
                print(x)

except FileNotFoundError:
    print("Error")
    