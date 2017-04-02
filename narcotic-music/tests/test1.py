with open("instruments.txt") as f:
    content = f.readlines()
comm = "Instruments:\n"
for x in content:
    comm += x
return comm
