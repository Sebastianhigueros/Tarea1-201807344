from collections import OrderedDict
def netPrice(n,Objects):
    for item, quantity in Objects.items():
        print(item,quantity)
        

if __name__ == "__main__":
    n = int(input())
    Objects = OrderedDict()
    for x in range(n):
        item,separation, quantity = input().rpartition(' ')
        Objects[item] = Objects.get(item,0) + int(quantity)
    netPrice(n,Objects)