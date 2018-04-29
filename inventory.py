#inventory
store = {}
laptops = {'dell':10, 'hp':15, 'lenovo':20, 'acer':5}
phones = {'samsung':50, 'iphone':40, 'tecno':100, 'sony':25}
store['laptops'] = laptops
store['phones'] = phones

def add_item(cat, item, qty):
    #function adds item to the store category
    if not isinstance (cat,str) or not isinstance(item, str) or not isinstance(qty, int):
        print('Enter str category, str item and int quantity')
    elif cat not in store:
        print('Create a category first')
    elif item not in store[cat]:
        store[cat][item] = qty
    else:
        count = store[cat][item]
        store[cat][item] = count + qty
        
def del_item(cat, item, qty):
    #function decrements the quantity of the given item
    if not isinstance (cat,str) or not isinstance(item, str) or not isinstance(qty, int):
        print('Enter str category, str item and int quantity')
    elif cat not in store:
        print('Category does not exist')
    elif item not in store[cat]:
        store[cat][item] = qty
    else:
        count = store[cat][item]
        store[cat][item] = count + qty

def add_cat(cat):
    #function adds category to store
    if len(cat)>1 and isinstance(cat, str):
        store[cat] = {}
def view_store():
    print(store)
if __name__=='__main__':
    add_item('laptop', 'compaq', 10)
    view_store()
    
        
    