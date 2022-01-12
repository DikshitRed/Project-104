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
sum=0

for i in array:
    sum+=i

mean=sum/n
print("The mean of the weight is " + str(mean))