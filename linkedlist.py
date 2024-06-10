class Node:
    def __init__(self, item, price, quantity):
        self.item = item
        self.price = price
        self.quantity = quantity
        self.next = None

class ShoppingList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_item(self, item, price, quantity):
        new_node = Node(item, price, quantity)
        new_node.next = self.head
        self.head = new_node

    def remove_item(self, item):
        current = self.head
        prev = None
        while current:
            if current.item == item:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next

    def print_list(self):
        if self.is_empty():
            print("Daftar belanja kosong")
            return

        current = self.head
        print("Daftar Belanja:")
        while current:
            print(f"- {current.item}: {current.quantity} pcs x Rp{current.price:,}")
            current = current.next

# Contoh penggunaan
shopping_list = ShoppingList()

shopping_list.add_item("Apel", 5000, 2)
shopping_list.add_item("Susu", 7000, 1)
shopping_list.add_item("Roti", 4000, 3)

shopping_list.print_list()

# Menghapus item
shopping_list.remove_item("Roti")

shopping_list.print_list()
