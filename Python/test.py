import  csv
import random

""" f = open('info.csv','r')
rdr = csv.reader(f)

for line in rdr:
  print(line)

f.close() """

fn = ['김','박','이','황','정','최','유']
mn = ['민준','해연','준영','유진','영준','지우','서윤']
sex = ['남','여']


f = open('info.csv', 'a', newline='')
wr = csv.writer(f)

for i in range(10):
  nameRan = random.randrange(0,8)
  ageRan = random.randrange(20,40)
  sexRan = random.randrange(0,2)
  name = fn[nameRan] + mn[nameRan]
  wr.writerow([i+1,name,ageRan,sex[sexRan]])

f.close()


""" with open("info.csv", 'a') as f:
  f.truncate(0)
 """
