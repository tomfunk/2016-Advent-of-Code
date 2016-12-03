#day 3

with open('input.txt') as myfile:
	data = myfile.readlines()
data = [x.replace('\n','')for x in data]

data = [x.split(' ')for x in data]

newdata = []

for x in data:
	ndew = [int(y) for y in x if len(y) > 0]
	newdata.append(ndew)	

ptwodata = []
	
for x in range(0,len(newdata)-2,3):
	for y in range(3):
		ndew = [newdata[x][y],newdata[x+1][y],newdata[x+2][y]]
		ptwodata.append(ndew)
	ans = 0

#for part one for x in newdataata
for x in ptwodata:
	if sum(x) - max(x) > max(x):
		ans +=1

print(ans)