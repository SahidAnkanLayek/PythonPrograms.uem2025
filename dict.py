#top most repetative word in a given file 


fhand = open('abc.txt')
counts = dict()  

# Loop through each line in the file
for line in fhand:
    words = line.split()  # Split the line into words
    for word in words:
        counts[word] = counts.get(word, 0) + 1
ist=list()
for key,val in counts.items():
    ist.append((val,key))
ist.sort(reverse=True)
for val,key in ist[:10]:
    print(key,val)    
