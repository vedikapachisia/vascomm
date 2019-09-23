import random 

date = random.randint(1, 28)
month = random.randint(1, 12)
year = random.randint(1970, 2002)

f = open("dates.txt", "a+")

for i in range(0, 1000):
    date = "%02d" % date
    month = "%02d" % month
    date_string = (str(date) + "/" + str(month) + "/" + str(year) + "\n")
    f.write(date_string)

    date = random.randint(1, 28)
    month = random.randint(1, 9)
    year = random.randint(1970, 2002)

f.close()


