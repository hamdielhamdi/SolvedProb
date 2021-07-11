
class  node:
	def __init__(self, data=None):
		self.data = data
		self.next =None


class linked_list:
	def __init__(self):
		self.head = node()

	def append(self, data):
		new_node = node(data)
		cur = self.head
		while cur.next!=None:
			cur = cur.next
		cur.next = new_node

	def len(self):
		cur = self.head
		total = 0
		while cur.next!=None:
			total +=1
			cur = cur.next
		return total

	def display(self):
		elem  = []
		cur = self.head
		while cur.next != None:
			cur = cur.next
			elem.append(cur.data)
		return elem

	def get(self, index):
		if index >= self.len():
			print('error index out of range !!!')
		cur_index = 0
		cur = self.head
		while True:
			cur = cur.next
			if cur_index==index: 
				return cur.data
			cur_index+= 1

	def delete(self, index):
		if index >= self.len():
			print('error index out of range !!!')
		cur_index = 0
		cur = self.head
		while True:
			last_node = cur
			cur = cur.next
			if cur_index==index: 
				last_node.next = cur.next
				return 
			cur_index+= 1

