import os #operation system

#讀取檔案
products = [] #寫入時會用到所以寫在外面
if os.path.isfile('products.csv'): #檢查檔案是否存在
	print('有檔案!!')
	with open('products.csv','r', encoding='utf-8') as f:  #讀取跟寫入必須用同一種編碼
		for line in f:
			if '商品,價格' in line:
				continue #結束這回合 執行下一次迴圈
			name, price = line.strip().split(',')  #讀取是一行一行讀取  split後會變成清單
			#name = s[0]
			#price = s[1]
			#print(s)  #2-d小清單
			#print(s) #1-d大清單
			#裝進清單
			products.append([name,price])
	print(products)
else:
	print('找不到檔案.....')






#讓使用者輸入
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入商品價格： ')
	price = int(price)
	products.append([name, price])	
print(products)

#印出所有購買紀錄
for p in products:
	if '商品,價格' in p:
		continue
	print(p[0] , '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:  #encoding
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')  # price is integer now, and should be casted to string