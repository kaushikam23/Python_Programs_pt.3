text=input("Enter a sentence")
words=text.split()
t=list()
for word in words:
    t.append((len(word),word))

print(t)
t.sort(reverse=True)
res=list()

for length,word in t:
    res.append(word)

print("Sorted array:")
print(res)

