#day 8

with open('input.txt') as myfile:
	data = myfile.readlines()
data = [x.replace('\n','').replace('x',' ').replace('y','').replace('=','').split(' ')for x in data]

screen = [['.' for x in range(50)] for y in range(6)]

def rect(x,y,tempscreen):
	for rows in range(x):
		for cols in range(y):
			tempscreen[rows][cols] = '#'
	return(tempscreen)
def row(row, cnt,tempscreen):
	replace = [['.' for x in range(50)] for y in range(6)]
	for x in range(50):
		for y in range(6):
			if y == int(row):
				offset = int(cnt)
			else:
				offset = 0
			if x + offset < 50:
				replace[y][x+offset] = tempscreen[y][x]
			else:
				replace[y][x+offset-50] = tempscreen[y][x]
	return(replace)		
			
def col(col, cnt,tempscreen):
	replace = [['.' for x in range(50)] for y in range(6)]
	for x in range(50):
		for y in range(6):
			if x == int(col):
				offset = int(cnt)
			else:
				offset = 0
			if y + offset < 6:
				replace[y+offset][x] = tempscreen[y][x]
			else:
				replace[y+offset-6][x] = tempscreen[y][x]
	return(replace)
	
#test = [['rect', '2', '1'], ['rotate', 'column', '', '1', 'b', '1']]
for line in data:
	if line[0] == 'rect':
		screen = rect(int(line[2]),int(line[1]),screen)
	elif line[1] == 'row':
		screen = row(int(line[2]),int(line[4]),screen)
	else:
		screen = col(int(line[3]),int(line[5]),screen)
	#print(line, '\n', screen)
print('Part 1:', sum([x.count('#') for x in screen]))
print('\nPart 2:')
for x in screen:
	print(''.join(x).replace('.',' '))
