class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    '''Insert at head'''
    def insert_at_start(self, data):
        node = Node(data, self.head)
        self.head = node

    '''Insert at end'''
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        val = self.head
        while val.next:
            val = val.next
        val.next = Node(data, None)

    '''Insert values into Linked List'''
    def insert_list(self, data_list):
        for val in data_list:
            self.insert_at_end(val)

    '''Inserting at index'''
    def insert_at(self, index, data):
        if index < 0 or index > self.length():
            raise Exception('Invalid index')

        count = 0
        val = self.head
        if index == 0:
            node = Node(data, self.head)
            self.head = node

        while val:
            if count == index-1:
                node = Node(data, val.next)
                val.next = node
                break
            val = val.next
            count += 1

    '''Delete from index'''
    def delete(self, index):
        last_index = self.length() - 1
        if index < 0 or index > last_index:
            raise Exception('Invalid index')

        if index == 0:
            self.head = self.head.next
            return
        count = 0
        val = self.head
        while val:
            if count == index - 1:
                print('>>>>>>>>>>>>',str(val.next.data), 'deleted <<<<<<<<<<<<')
                val.next = val.next.next
                break
            val = val.next
            count += 1

    '''Length of Linked List'''
    def length(self):
        count = 0
        val = self.head
        while val:
            count += 1
            val = val.next
        return count

    def print_length(self):
        print('Length of Linked List is ->', self.length())
        return

    '''Print Linked List'''
    def print_linked_list(self):
        if self.head is None:
            print('Linked List is empty')
            return
        itr = self.head
        res = ''
        while itr:
            res += str(itr.data) + ' --> '
            itr = itr.next
        print(res)


def main():
    list_ = ['apple', 'banana', 'cake', 'python']
    ll = LinkedList()

    ll.insert_at_start(5)
    ll.insert_at_end(100)
    ll.insert_at_start(120)
    ll.insert_at_start(0)
    ll.print_linked_list()
    ll.insert_list(list_)
    ll.print_linked_list()
    ll.print_length()
    ll.length()
    ll.insert_at(2, 'Swapnil')
    ll.print_linked_list()
    ll.delete(1)
    ll.delete(5)
    ll.print_linked_list()
    ll.print_length()


if __name__ == '__main__':
    main()
