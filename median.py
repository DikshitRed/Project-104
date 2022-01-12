import csv

with open("HeightWeight.csv", newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)
array=[]

for i in range(len(file_data)):
    get=file_data[i][2]
    array.append(float(get))

n=len(array)
array.sort()

if n % 2 == 0:
    median1=float(array[n//2])
    median2=float(array[n//2-1])
    median=(median1+median2)/2

else:
    median=array[n//2]

print("Median is " + str(median))