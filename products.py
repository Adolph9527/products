products = []
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	price = int(price)
	products.append([name, price])	
print(products)


with open('products.csv', 'w', encoding='utf8') as f:  #encoding
	f.write('名稱,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')  # price is integer now, and should be casted to string