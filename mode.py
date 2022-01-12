import csv
from collections import Counter

with open("HeightWeight.csv", newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)
array=[]

for i in range(len(file_data)):
    get=file_data[i][2]
    array.append(float(get))

data=Counter(array)
modedataforrange={
    "75-85":0,
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "125-135":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0,
}

for weight,occurance in data.items():
    if 75<float(weight)<85:
        modedataforrange["75-85"]+=occurance
    elif 85<float(weight)<95:
        modedataforrange["85-95"]+=occurance
    elif 95<float(weight)<105:
        modedataforrange["95-105"]+=occurance
    elif 105<float(weight)<115:
        modedataforrange["105-115"]+=occurance
    elif 115<float(weight)<125:
        modedataforrange["115-125"]+=occurance
    elif 125<float(weight)<135:
        modedataforrange["125-135"]+=occurance
    elif 135<float(weight)<145:
        modedataforrange["135-145"]+=occurance
    elif 145<float(weight)<155:
        modedataforrange["145-155"]+=occurance
    elif 155<float(weight)<165:
        modedataforrange["155-165"]+=occurance
    elif 165<float(weight)<175:
        modedataforrange["165-175"]+=occurance
    

moderange,modeoccurance=0,0

for range,occurance in modedataforrange.items():
    if occurance>modeoccurance:
        moderange,modeoccurance=[int(range.split("-")[0]),int(range.split("-")[1])], occurance

mode=float((moderange[0]+moderange[1])/2)
print(f"Mode is {mode:2f}")