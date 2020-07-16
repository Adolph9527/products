import os #operation system

#讀取檔案
def read_file(filename):
	products = [] #寫入時會用到所以寫在外面
	with open(filename,'r', encoding='utf-8') as f:  #讀取跟寫入必須用同一種編碼
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
	return products   #將清單存起來、回傳出去給某個變數			


#讓使用者輸入(新增資料)
def user_input(products):
	while True:
		name = input('請輸入商品名稱： ')
		if name == 'q':
			break
		price = input('請輸入商品價格： ')
		price = int(price)
		products.append([name, price])
	print(products)
	return products

#印出所有購買紀錄
def print_products(products):
	for p in products:
		#if '商品,價格' in p:
		#	continue
		print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:  #encoding
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')  # price is integer now, and should be casted to string
					#字串相連用+


def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #檢查檔案是否存在
		print('有檔案!!')
		products = read_file(filename)
	else:
		print('找不到檔案')	
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)


main()