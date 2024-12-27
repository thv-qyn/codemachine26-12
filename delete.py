from ontapoop.filefactory import FileFactory
from ontapoop.product import  Product
x = float(input("nhập mã x :"))
ff=FileFactory()
dataset=ff.readData("mydataset.json",Product)
dataset = [product for product in dataset if product.price >= x]
print("danh sách sản phẩm sau khi xóa:")
for product in dataset:
    print(product)
