class Node:
        def __init__(self, data):
                self.data = data
                self.next = None

        def print_list(self):
                current_node = self
                while(current_node.next != None):
                        print current_node.data
                        current_node = current_node.next
                print current_node.data

        def remove_node(self, data):
                current_node = self
                flag = current_node
                if current_node.data == data:
                        self = flag.next
                        return True

                while(current_node.next != None):
                        if current_node.data == data:
                                flag.next = current_node.next
                                return True
                        flag = current_node
                        current_node = current_node.next
