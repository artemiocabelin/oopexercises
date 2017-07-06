import store_product
import store

corvin = store_product.Product("Kansas", "Kor")
jeeves = store.Store("New York", "John")


jeeves.add_product("lotion").inventory()
corvin.add_prod('Gatorade').product_inventory()