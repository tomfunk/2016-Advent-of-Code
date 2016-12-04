#day 4
from string import ascii_lowercase

with open('input.txt') as myfile:
	data = myfile.readlines()
	
data = [x.replace('\n','').replace('-',' ').replace(']','').split('[') for x in data]

#part 1
def check(akey):
	ans = ''
	cnt = {x : akey.count(x) for x in ascii_lowercase}
	for y in range(10,0,-1):
		for z in ascii_lowercase:
			if cnt.get(z, None) == y:
				ans += z
	return ans[:5]
	
val = 0
for line in data:
	if check(line[0]) == line[1]:
		val += int(line[0][-3:])
print('Part 1:',val)

	
#part 2	
def rotate(akey):
	realnum = int(akey[-3:]) % 26
	
	x=0
	pos = []
	for a in ascii_lowercase:
		x+=1
		pos.append([a,x])
	newstr = ""
	for char in akey[:-4]:
		for x in pos:
			if x[0] == char:
				val = x[1] + realnum
				if val > 26:
					val -= 26
		for x in pos:
			if x[1] == val:
				newstr += x[0]
	return newstr

for line in data:
	if 'north' in rotate(line[0]):
		print('Part 2:',line[0][-3:])