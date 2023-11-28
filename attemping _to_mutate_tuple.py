
sum1 = (1, " John", "Carlos", "johncarlos@gmail.com")
sum2 = (2, "Marisa", "Elisa", "masisaelisa@hotmail.com")
sum3 = (3, " Vanessa", "Elsa", "vanessaelsa@gmail.com")


sum = [sum1, sum2, sum3]

for item in sum:
    for element in item:
        print(element)
print("Hello")

#Attempt to change an email for John Carlos
 # Attempt to change email for John Doe
sum[0] = (1, "John", "sits","johndoe@yahoo.com" )

for item in sum:
    print(item)
    
print(f"this is the lentgh{len(sum1)} of this tuple")
user4_id_email = (4, "momobaz@gmail.com")
user4_firstname_lastname = ("Momo", "Baz")
user4 = user4_id_email + user4_firstname_lastname
print(user4)

# repeat operator
