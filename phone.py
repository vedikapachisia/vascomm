import random

s = set()

f = open("phone_numbers.txt", "a+")

while(len(s)  < 1000):
    
    phone = random.randint(100000000, 999999999)
    phone = str(random.randint(6, 9)) + str(phone)
    s.add(phone)
        
for item in s:
    f.write((item) + "\n")