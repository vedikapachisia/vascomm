import models

import threading
import time 
import random
import datetime

user_details = list(UserDetails.objects.all())

def get_random_time():
    t = random.randint(1, 100) * 0.01
    return t

def print_size():
    while True:
        time.sleep(1)
        print(len(user_details))
        f = open("f.txt", "a+")
        f.write(len(user_details))

def run_threads():
    t1 = threading.Thread(print_size)
    t1.start()
    t1.join()
