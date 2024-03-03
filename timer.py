import datetime
import time
import os

file = open('data.txt', 'r')
Lines = file.readlines()

count = 0

godzina = 0
minuta = 0

for line in Lines:
    if count == 0:
        godzina = int(line.strip())
    if count == 1:
        minuta = int(line.strip())
    count += 1

file.close()

time_check = datetime.time(godzina, minuta)

while datetime.datetime.now().time() <= time_check:
    if datetime.datetime.now().time() >= time_check:
        break
    time.sleep(3)

os.system("boom.py")
