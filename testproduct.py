from ontapoop.filefactory import FileFactory
from ontapoop.product import Product

p1=Product(1,"Coca",100)
print(p1)

dataset=[]
dataset.append(p1)
dataset.append(Product(2,"Pepsi",20))
dataset.append(Product(3,"Sting",90))
dataset.append(Product(4,"Aqua",10))
dataset.append(Product(5,"7up",30))
print("danh sach sản phẩm :")
for product in dataset:
    print(product)

while True:
    id=int(input("nhập mã:"))
    name=input("nhập tên:")
    price=float(input("nhập mã:"))
    p=Product(id,name,price)
    dataset.append(p)
    ask=input("nhập tiếp không?(c/k):")
    if ask=='k':
        break
print("danh sách sau khi nhập:")
for product in dataset:
    print(product)



#gọi chức năng chụp ảnh đối tượng xuống ổ cứng
#chụp thành đinhj dạng json
ff=FileFactory()
ff.writeData("mydataset.json",dataset)