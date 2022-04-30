#create Acronyms using python (short form )

unstr = str(input("Enter the String: "))
text = unstr.split()  #break whole string into word(not char) and store it into list
a = ''
for i in text:
    a = a+str(i[0]).upper()

print(a)
'''
OUTPUT:
Enter the String: Artificial intelligence
AI
'''
