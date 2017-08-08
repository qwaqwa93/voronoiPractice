
# Node with two children
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def left(self, data=None):
        node = Node(data)
        self.left = node

    def right(self, data=None):
        node = Node(data)
        self.right = node

    def insert(self, data):
        if self.data:
            if data[0] < self.data[0]:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data[0] > self.data[0]:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def find(self, data):
        if data == self.data[0]:
            return self.data
        elif data < self.data[0]:
            if self.left:
                return self.left.find(data)
            else:
                print("No matching key")
                return None
        else:
            if self.right:
                return self.right.find(data)
            else:
                print("No matching key")
                return None

    def __str__(self):
        if self.data == None:
            return "None"
        retString = ""
        if self.left:
            retString += "[" + str(self.left) + "]<--"
        retString += str(self.data)
        if self.right:
            retString += "-->[" + str(self.right) + "]"
        return retString

# Some Tests
if __name__ == "__main__":
    myBST = Node()
    myBST.insert((5,1))
    myBST.insert((2,13))
    myBST.insert((10,3))
    myBST.insert((4, 5))
    myBST.insert((9, 7))
    print myBST
