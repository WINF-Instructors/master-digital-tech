class Node:
  
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None

# insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if self.head is not None:
      current = self.head
      while current.next is not None:
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
    # print method for the linked list
  def printLL_iterative(self):
    current = self.head
    while current is not None:
      print(current.data)
      current = current.next

  def printLL_recursive(self):
    def recursive_step(ll):
      if ll is not None:
        print(ll.data)
        recursive_step(ll.next)
    recursive_step(self.head)

  def ll_to_list_procedural(self):
    new_list = []
    current = self.head
    while current is not None:
      new_list.append(current.data)
      current = current.next
    return new_list
  
  def ll_to_list_functional(self):
    def recursive_step(ll, l):
      if ll is not None:
        return recursive_step(ll.next, l + [ll.data])
      else:
        return l
    return recursive_step(self.head, [])

  def reduce(self, f, init):
    def recursive_step(ll, collect):
      if ll is not None:
        return recursive_step(ll.next, f(collect,ll.data))
      else:
        return collect
    return recursive_step(self.head, init)
  
  def ll_to_list_via_reduce(self):
    return self.reduce(lambda x,y: x+[y], [])

  def print_ll_via_reduce(self):
    return self.reduce(lambda x,y: x+"\n"+str(y), "")
    
  def map(self, f):
    def recursive_step(ll, tail_ll):
      if ll is not None:
        cur_data = ll.data
        tail_ll.insert(f(cur_data))
        return recursive_step(ll.next, tail_ll.next)
    if self.head is not None:
      new_ll = LinkedList()
      new_ll.insert(f(self.head.data))
      return recursive_step(self.head.next, new_ll.head)

  

LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL_iterative()
LL.printLL_recursive()
l = LL.ll_to_list_procedural()
print(l)
l2 = LL.ll_to_list_functional()
print(l2)
#new_ll = LL.map(lambda x: x*2)
#print(new_ll)
l3 = LL.ll_to_list_via_reduce()
print(l3)
print(LL.print_ll_via_reduce())