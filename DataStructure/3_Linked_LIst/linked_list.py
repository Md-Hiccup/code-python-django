class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("linked list is empty")

        itr = self.head
        llstr = ''
        while(itr != None):
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while(itr.next):
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("This is not a valid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("This is not a valid index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        itr = self.head
        count = 0
        while(itr):
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
            count += 1
            itr = itr.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_end(40)
    ll.print()

    ll1 = LinkedList()
    ll1.insert_values(["banana", "mango", "grapes", "orange"])
    ll1.remove_at(2)
    ll1.print()
    ll1.insert_at(1, "grapes")
    ll1.print()
    ll1.insert_at(0, "jackfruit")
    ll1.print()

    ll2 = LinkedList()
    ll2.insert_values([45, 7, 12, 56])
    ll2.insert_at_end(67)
    ll2.remove_at(2)
    ll2.print()



