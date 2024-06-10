class Node:
  """
  Kelas untuk merepresentasikan simpul dalam pohon biner.

  Atribut:
    data: Nilai yang disimpan di simpul.
    left: Referensi ke simpul anak kiri.
    right: Referensi ke simpul anak kanan.
  """

  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


def insert(root, data):
  """
  Menambahkan elemen baru ke pohon biner.

  Argumen:
    root: Referensi ke simpul akar pohon.
    data: Nilai yang ingin ditambahkan.

  Kembalian:
    Referensi ke simpul baru yang ditambahkan.
  """

  if root is None:
    return Node(data)
  elif data < root.data:
    root.left = insert(root.left, data)
  else:
    root.right = insert(root.right, data)
  return root


def search(root, data):
  """
  Menjelajahi pohon dengan cara preorder.

  Argumen:
    root: Referensi ke simpul akar pohon.
  """

  if root is None:
    return False
  elif root.data == data:
    return True
  elif data < root.data:
    return search(root.left, data)
  else:
    return search(root.right, data)
def preorder(root):
  if root is not None:
    print(root.data)
    preorder(root.left)
    preorder(root.right)


def inorder(root):
  """
  Menjelajahi pohon dengan cara inorder.

  Argumen:
    root: Referensi ke simpul akar pohon.
  """

  if root is not None:
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def postorder(root):
  """
  Menjelajahi pohon dengan cara postorder.

  Argumen:
    root: Referensi ke simpul akar pohon.
  """

  if root is not None:
   postorder(root.left)
   postorder(root.right)
   print(root.data)


# Contoh penggunaan

data = [10, 5, 15, 3, 12, 20]

root = None
for num in data:
  root = insert(root, num)
if search(root, 15):
  print("Nilai 15 ditemukan dalam pohon")
else:
  print("Nilai 15 tidak ditemukan dalam pohon")
print("Preorder traversal:")
preorder(root)

print("\nInorder traversal:")
inorder(root)

print("\nPostorder traversal:")
postorder(root)
