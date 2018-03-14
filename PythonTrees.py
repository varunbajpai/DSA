class Tree:
	def __init__(self):
		self.data = None
		self.right = None
		self.left = None

root=Tree()
		
def insert(val):
	if root.data == None:
		root.data = val
		return
	else:
		node = root
		while True:
			if val>node.data:
				if node.right == None:
					newNode = Tree()
					newNode.data = val
					node.right = newNode
					break
				else:
					node = node.right
					continue
			else:
				if node.left == None:
					newNode = Tree()
					newNode.data = val
					node.left = newNode
					break
				else:
					node = node.left
					continue
				
					
def travel(root):
	#print(root.data)
	if root != None:
		travel(root.left)
		print(root.data)
		travel(root.right)
		
insert(100)
insert(5)
insert(110)
travel(root)
	