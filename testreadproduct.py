from ontapoop.filefactory import FileFactory
from ontapoop.product import  Product

ff=FileFactory()
dataset=ff.readData("mydataset.json",Product)
print("danh sách sản phẩm:")
for product in dataset:
    print(product)


