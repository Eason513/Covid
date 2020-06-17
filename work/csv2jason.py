fileobj = open("test.csv","r")#r,w or a are options
datalist = fileobj.readlines()
fileobj.close()
conflist = []
for country in datalist:
    templist = country.split(",")
    pname = templist[2]
    cname = templist[3]
    lat = templist[5] 
    lon = templist[6]
    conf = int(templist[7])
    conflist.append({"pname":pname,"cname":cname,"lat":lat,"lon":lon,"conf":conf})
