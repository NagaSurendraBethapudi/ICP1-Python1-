Favourites = input('enter your favourite videos : ')
result = ''
for i in Favourites:
    if i == 'n':
        i = 'ns'
    result +=i 
print("String after adding ns : ", result)