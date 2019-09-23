import random

s = set()

file = open("phone_numbers", "w")

    while s.__len__()  < 1000:
        
        phone = random.randint(1000000000, 9999999999)
        s.add(phone)
        
file.write(s)