goods_dict = {
    "001": {"name": "爱马仕腰带", "price": 1999},
    "002": {"name": "劳力士男表", "price": 19999},
    "003": {"name": "巴宝莉眼镜", "price": 4999},
    "004": {"name": "路虎发现四", "price": 99999}
}
print('--------------------------------------商品列表------------------------------------------------------')
for keys in goods_dict:
    print(keys, goods_dict[keys]["name"],    goods_dict[keys]["price"])
print('----------------------------------------------------------------------------------------------------')
shopping = {}
i = 0
while input('按任意键购物，结束请按p:') != 'p':
    a = 0                                   # 商品编号初始化
    b = 0                                   # 数量初始化
    while a not in goods_dict:
        a = input('请输入商品编号:')
        if a not in goods_dict:
            print('商品编号错误，请重新输入！')
    while b <= 0:
        b = int(input('请输入商品数量:'))
        if b < 0:
            print('数量格式错误，请重新输入数量！')
    shopping[i] = goods_dict[a]
    shopping[i]['quality'] = b
    i += 1
print('------------------------------------------购物车-----------------------------------------------------')
Total = 0            # 总价格初始化
print('name  price   quality')
for keys in shopping:
    print(shopping[keys]['name'], shopping[keys]['price'], shopping[keys]['quality'])
    Total += shopping[keys]['price'] * shopping[keys]['quality']
print('Total:{}'.format(Total))
print('------------------------------------------------------------------------------------------------------')