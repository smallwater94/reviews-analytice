data = []
pg = 10
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		if len(data) % 100000 == 0:
			print('進度',pg,'%')
			pg += 10
