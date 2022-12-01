rawlist = open("elfcalories.txt","r")
elflist = []

#create list from text file
for line in rawlist:
    if line == "\n":
        elflist.append("BREAK")
    else:
        str = line.split("\n")[0]
        num = int(str)
        elflist.append(num)
#print(elflist)

elfdict = {}

x = 0
elf = 1

for element in elflist:
    if type(element) == int:
        x = x + element
    elif element == "BREAK":
        elfdict[elf]=x
        x = 0
        elf = elf +1

print(elfdict)

elfmax = max(elfdict, key=elfdict.get)
print(elfmax)
print(elfdict[elfmax])



