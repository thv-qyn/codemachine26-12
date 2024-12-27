from ontapoop.filefactory import FileFactory
from ontapoop.product import  Product

a = float(input("nhập mã a:"))
b = float(input("nhập mã b :"))

ff=FileFactory()
dataset=ff.readData("mydataset.json",Product)
dataset = [product for product in dataset if a<=product.price<=b]
print("danh sách sản phẩm sau khi lọc :")
for product in dataset:
    print(product)