text=input("enter a text:")
words=text.lower().split()

frequency={}

for word in words:
    if word in frequency:
        frequency[word]+=1
    else:
        frequency[word]=1

for x,y in frequency.items():
    print(x,":",y)