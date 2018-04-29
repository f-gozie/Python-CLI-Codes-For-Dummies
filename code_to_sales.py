#sales

import sys

sys.path.append('/path/to/your_folder_name/')

import inventory
inventory.view_store()

print(dir())

from inventory import add_item
add_item('laptops', 'compaq', 10)

print(dir())