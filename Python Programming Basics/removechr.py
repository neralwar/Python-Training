
inputstring ="NNPPJJSSLLKKNNIIYYTT"

duplist=[]

for i in inputstring:
    if i not in duplist:
        duplist.append(i)


print(" ".join(duplist))

def checkifvowel(inputstring):
    vowel =['a','e','o','i','u']
    for v in vowel:
       if inputstring.find(v) == -1:
           print("ALL VOWEL LETERS ARE NOT PRESENT")
           return -1
    print("PRESENT")

def findtextinstring(inputstring,testtofind):
    if inputstring.find(testtofind) != -1:
        print("TEXT PRESENT")
    else:
        print("TEXT NOT PRESENT")


def removenthchr(inputstr,pos):
    newstring=""
    for i in inputstr:
        if i == pos-1:
            pass
        else:
            newstring = newstring + i

    print(newstring)
        

removenthchr("Ashish Neralwar",7)
findtextinstring("Ashsih Neralwar","XX")
checkifvowel("AshishNeralwaraeoiu")