# Python3 code to demonstrate 
# each occurrence frequency using 
# naive method 

# initialize string
filetext = ''  

# get text from file
with open('/Users/USER/pyproj/virupaksa/pucrs-ss/lab19ago/assets/TextoClaro.txt', 'r') as file:
    # copy text from file 
    filetext = file.read().replace('\n', '')
    # sort because why not
    filetext = sorted(filetext)

# initialize array
occurrences = {}

# use naive method to get count of each element in string   
for letter in filetext:
    # has previous captured occurence
    if letter in occurrences:
        # increment occurence
        occurrences[letter] += 1
    # first time captured
    else:
        # make it one
        occurrences[letter] = 1

print('LETTER OCCURENCES\n')
for letter in occurrences: print(letter, ':', occurrences[letter])

# initialize DIVIDEND variable
fSum = 0

for letter in occurrences: 
    #sum (fi*(fi-1))
    fSum += occurrences[letter]*(occurrences[letter]-1)

# Index of coincidence = { DIVIDEND: fSum } / { DIVIDER: n * (n-1) }
ic = fSum/(len(occurrences)*(len(occurrences)-1))

print("\nIc: ", ic)
