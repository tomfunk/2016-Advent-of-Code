#day 6

with open('input.txt') as myfile:
	data = myfile.readlines()
	
data = [x.replace('\n','') for x in data]

tilt = []
for x in range(8):
	addn = ''
	for y in data:
		addn += y[x]
	tilt.append(addn)
ans = ''
secans = ''
for x in range(8):
	max =0
	min = 1000
	winner = ''
	loser = ''
	for char in tilt[x]:
		test = tilt[x].count(char)
		if test > max:
			max = test
			winner = char
		if test < min:
			min = test
			loser = char
	ans += winner
	secans += loser
	
	
print('Part 1:', ans)
print('Part 2:', secans)