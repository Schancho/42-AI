t = (17,5,2019,1,6)


#print(str(t[3]).zfill() + "/" + str(t[4]) + "/" + str(t[2]) + str(t[0]) + ":" +str(t[1]))
minutes = str(t[1]).zfill(2)
hours = str(t[0]).zfill(2) + ":"
days = str(t[4]).zfill(2) + "/"
months = str(t[3]).zfill(2) + "/"
years = str(t[2]).zfill(4) + " "
print(months + days + years + hours + minutes)
