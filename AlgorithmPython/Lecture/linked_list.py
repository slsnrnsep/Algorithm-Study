class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,data):
        self.head = Node(data)

    def append(self,data):
        if self.head is None:
            self.head = Node(data)
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next=Node(data)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        node = self.get_node(index - 1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index - 1)
        node.next = node.next.next

    def get_linked_list_sum(linked_list_1, linked_list_2):
        sum_1 = _get_linked_list_sum(linked_list_1)
        sum_2 = _get_linked_list_sum(linked_list_2)

        return sum_1 + sum_2

    def _get_linked_list_sum(linked_list):
        linked_list_sum = 0
        head = linked_list.head
        while head is not None:
            linked_list_sum = linked_list_sum * 10 + head.data
            head = head.next
        return linked_list_sum