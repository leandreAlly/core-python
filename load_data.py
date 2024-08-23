

# file = open("hello.txt", "w")
# file.write("Hello, world")
# file.close()

import csv

with open("favorite_colors.csv") as file:
  reader = csv.DictReader(file, delimiter=",")
  for row in reader:
        print(row['name'] + " works as a " + row['occupation'] + " and their favorite color is " + row['favorite_color'])


