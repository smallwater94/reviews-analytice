data = []
pg = 10
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		if len(data) % 100000 == 0:
			print('進度',pg,'%')
			pg += 10
print('檔案取完畢 共',len(data),'筆資料')

allnum = 0
con = 0
while con < 1000000:
	allnum += len(data[con])
	con += 1
avg = allnum / 1000000
print(avg)