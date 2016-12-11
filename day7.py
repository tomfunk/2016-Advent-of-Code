with open('input.txt') as myfile:
	data = myfile.readlines()
	
data = [x.replace('\n','').replace('[',']').split(']') for x in data]

def haspal(s):
	ans = 0
	for x in range(len(s)-3):
		test = s[x:x+4]
		if test == test[::-1] and test[:2] != test[2:]:
			ans +=1
	if ans > 0:
		return True
	else:
		return False

def aba(line):
	ans = 0
	abas = []
	for x in range(len(line)):
		if x % 2 == 0:
			for y in range(len(line[x])-2):
				test = line[x][y:y+3]
				if test == test[::-1] and test[0] != test[1]:
					abas.append(str(test[1]+test[0]+test[1]))
	for x in range(len(line)):
		if x % 2 != 0:
			for aba in abas:
				if aba in line[x]:
					ans+=1
	if ans > 0:
		return True
	else:
		return False
			
#'odd' numbers are in brackets
#print(haspal('abbasadasda'))
finans = 0
secans = 0
for line in data:
	ans = 0
	if aba(line):
		secans += 1
	for x in range(len(line)):
		if haspal(line[x]):
			if x % 2 == 0:
				ans += 1
			else:
				ans -= 3000
	if ans > 0:
		finans +=1
print("Part 1:",finans)	
print("Part 2:",secans)
