# Rain Nõmmik
# Kontrolltöö - variant 1

# Ülesanne 1

def list_sum(list): # define function
    return (sum(list)) # print the lenght of the list

print(list_sum([1,2,3,4,5,6])) # call the function on the and use the list as the input

# Ülesanne 2

b = []
def liblikas(a): # define function
    a = a.split()
    for x in a: # Check every element in list a
        if x[0] == 'A' or x[0] == 'a': # if it starts with A or a then
            x = 'Liblikas' # if true replace it with liblikas
        b.append(x) # create a new list 
        c = ' '.join(b) # chnage the list back to string
    return c 

print(liblikas('Arno isaga koolimajja jõudis, olid tunnid juba alanud'))

# Ülesanne 3

# Ei joudnud




