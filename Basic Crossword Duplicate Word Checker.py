f = open("themeless11.TXT", "r")
words_raw=f.readlines()
starting_point=words_raw.index("<GRID>\n")
for i in range(starting_point+1):
    words_raw.pop(0)

def justalpha(x):
    return ''.join([y for y in x if y.isalpha()])
 
y = [(x.split('.')) for x in words_raw]
allclues = [z.strip() for x in y for z in x]
print(allclues)
words = [justalpha(y.upper()) for x in allclues for y in x.split()]
for w in set(words):
    if words.count(w)>1: print (w, words.count(w))

   
