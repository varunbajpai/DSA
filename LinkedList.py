class LinkedList:
	def __init__(self):
		self.data = None
		self.next = None

head = LinkedList()

def insert(val):
	if head == None:
		head.data = val
		return
	else:
		node = head
		newNode = LinkedList()
		while node.next != None:
			node = node.next
		node.next = newNode
		newNode.data = val
	
def travel(head):
	if head != None:
		print(head.data)
		travel(head.next)

insert(1)
insert(2)
insert(3)
insert(4)
travel(head)