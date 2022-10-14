class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_to_tail(self, node):
        if self.head == None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.set_next(node)

    def remove_from_head(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add_to_tail(Node('1'))
    linked_list.add_to_tail(Node('3'))
    linked_list.add_to_tail(Node('2'))
    print("ll:", linked_list)
    first = linked_list.remove_from_head()
    print("removed:", first)
    print("ll:", linked_list)      
