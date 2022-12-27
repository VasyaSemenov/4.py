from functools import reduce
import csv

with open("data-20200320T1016-structure-20200320T1016.csv","r") as file:
	keys = file.readline()
	reader = csv.reader(file, delimiter=",")
	dataset = [x for x in reader]
keys = list(keys.split(","))
entry_mode = list(map(lambda x: x[4] == 'Безвизовый', dataset))
print(entry_mode.count(True))