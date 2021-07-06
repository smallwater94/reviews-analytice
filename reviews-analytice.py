def read():
	data = []
	pg = 10 #進度
	with open('reviews.txt', 'r') as f:
		for line in f:
			data.append(line)
			if len(data) % 100000 == 0:
				print('進度',pg,'%')
				pg += 10
	print('檔案取完畢 共',len(data),'筆資料')
	return data

def lenNumber(data):
	sum_len = 0
	for d in data:
		sum_len += len(d)

	print('平均長度是',sum_len/len(data))

	new = []
	for d in data:
		if len(d) < 100:
			new.append(d)
	print('共有', len(new)/10000,'% 的留言長度小於100')

	# good = []
	# for d in data:
	# 	if 'good' in d:
	# 		good.append(d)
	# print('含有',len(good),'筆留言含有good')

		#上下相等,下為速寫法

	good = [d for d in data if 'good' in d]
	print('含有',len(good),'筆留言含有good')

def findWord(data):
	wc = {} #word_count
	for d in data:
		words = d.split()
		for word in words:
			if word  in wc:
				wc[word] += 1
			else:
				wc[word] = 1

	for word in wc:
		if wc[word] > 1000000:
			print(word,wc[word])

	print(len(wc))
	print(wc['Taiwan'])

	while True:
		word = input('請問你要查甚麼字？')
		if word == 'q':
			break
		elif word not in wc:
			print('這個字沒有出現過')
		else:
			print(word,'出現過的次數為:',wc[word])
	print('\n感謝你使用本查詢功能\n')

def main():
	data = read()
	lenNumber(data)
	findWord(data)

main()