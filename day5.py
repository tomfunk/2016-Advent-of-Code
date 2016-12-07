import hashlib
input = 'cxdnnyjw'
ans = ''
secondans = '????????'
x=0
while '?' in secondans:
#while len(ans) <8:
	x+=1
	val = input + str(x)
	test = val.encode()
	result = str(hashlib.md5(test).hexdigest())
	
	if result[:5] == '00000':
		ans += result[5]
		place = result[5]
		sub = result[6]
		if place.isnumeric():
			place = int(place)
			if place < 8:
				if secondans[place] == '?':
					secondans = secondans[:place] + sub + secondans[place+1:]
	
print("Part 1:", ans[:8])
print("Part 2:", secondans)
	

