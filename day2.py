# day 2

with open('input.txt') as myfile:
	data = myfile.readlines()

data = [x.replace('\n','') for x in data]
#part 1 keypad
nums = [[1,2,3],[4,5,6],[7,8,9]]
#part 2 keypad
#nums = [['X','X',1,'X','X'],['X',2,3,4,'X'],[5,6,7,8,9],['X','A','B','C','X'],['X','X','D','X','X']]

x=0
y=2
ans = ''
for line in data:
	#print('/n')
	for char in line:
		if char == "R":
			x +=1
			try:
				if nums[y][x] == 'X':
					x -= 1
			except:
				x -= 1
		elif char == "L":
			x -=1
			if x < 0:
				x = 0
			try:
				if nums[y][x] == 'X':
					x += 1
			except:
				x += 1
		elif char == "U":
			y -=1
			if y < 0:
				y = 0

			try:
				if nums[y][x] == 'X':
					y += 1
			except:
				y += 1		
		elif char == "D":
			y +=1
			try:
				if nums[y][x] == 'X':
					y -= 1
			except:
				y -= 1
		#print(x,y,nums[y][x])
	ans += str(nums[y][x])
print(ans)
		
