# Python3 code to demonstrate 
# each occurrence frequency using 
# naive method 

# initializing string
stri = ''  
with open('lab/T1.txt', 'r') as file:
    # copying text from file 
    test_str = file.read().replace('\n', '')
    # sort because yes
    stri = sorted(test_str)
  
# using naive method to get count 
# of each element in string 
all_freq = {}
  
for i in stri:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
  
# printing result 
print ("Count of all characters is :\n " +  str(all_freq))


for  all_freq
    val = all_freq[i]
    print(val * (val-1))
