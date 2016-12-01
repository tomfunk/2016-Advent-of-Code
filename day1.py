#day 1
with open('input.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')
data = data.replace(' ', '')

data = data.split(',')
count = [0,0,0,0]
	
num = 0
loc = []
for x in data:

	if x[0] == 'L':
		num -= 1
		if num == -1:
			num = 3
	else:
		num += 1
		if num == 4:
			num = 0
	place = int(x[1:])
	count[num] += int(place)
'''	part 2 (buggy)
	for y in range(place):
		count[num] += 1
		loco = []
		loco.append(count[0]-count[2])
		loco.append(count[1]-count[3])
		print(loco,loc.count(loco))
		loc.append(loco)
		if loc.count(loco) > 1:
			print(loco,loc.count(loco))
			print(abs(count[0]-count[2])+abs(count[1]-count[3]))
			break
'''

	
print(abs(count[0]-count[2])+abs(count[1]-count[3]))
	
	
		