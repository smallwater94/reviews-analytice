data = []
pg = 10 #進度
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		if len(data) % 100000 == 0:
			print('進度',pg,'%')
			pg += 10
print('檔案取完畢 共',len(data),'筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)

print('平均是',sum_len/len(data),'筆留言')