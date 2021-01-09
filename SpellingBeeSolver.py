# This is a python program meant to solve the NYT Spelling Bee Game
##import time
##start_time = time.process_time
txtfile=open("wlist_match10.txt","r")
WordList=txtfile.readlines()

center=input("What is the central letter (it must be used in every word)? ")
Letters=(input("What are the remaining (6) letters? ") + center)
letters=Letters.lower()
RefinedWL=[]
pangrams=[]

for line in WordList:
    if((center in line) and (len(line)>4)):
        RefinedWL.append(line)

def checkline(x):
    for character in x:
        if(character not in letters):
            return False
    return True

def isPangram(y):
    for character in letters:
        if(character not in y):
            return False
    return True
counter=0
for line in RefinedWL:
    if(checkline(line[:-1])):
        if (isPangram(line[:-1])):
            pangrams.append(line[:-1])
        else:
            counter+=1
            print(line[:-1])
##elapsedTime = time.process_time-start_time
print("\nThe program generated " + str(counter), "words! Keep in mind that some of these may not be accepted by the website game. \n")
##print(elapsedTime)
print("The Pangrams are: " + ", ".join(pangrams))

        
            

