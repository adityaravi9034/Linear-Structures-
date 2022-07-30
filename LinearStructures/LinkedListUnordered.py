class Node:
    def __init__(self, initData):
        self.data = initData
        self.nextdata = None

    def data(self):
        return self.data

    def getnextdata(self):
        return self.nextdata

    def setData(self, newData):
        self.data = newData

    def setnextdata(self, newnextdata):
        self.nextdata = newnextdata


class UnorderedList:

    def __init__(self):
        self.head = None

    def index(self, index):
        counter = 0
        current = self.head
        while current is not None:
            if counter == index:
                return current.data()
            else:
                counter += 1
                current = current.getnextdata()

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setnextdata(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.getnextdata()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.data() == item:
                found = True
            else:
                current = current.getnextdata()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while current is not None and not found:
            if current.data() == item:
                found = True
            else:
                previous = current
                current = current.getnextdata()

        if found:
            if previous is None:
                self.head = current.getnextdata()
            else:
                previous.setnextdata(current.getnextdata())
        else:
            print("Element not present")

    def pop(self, index=None):
        if index is None:
            return self.__pop()
        else:
            return self.__popindex(index)

    def __pop(self):
        current = self.head

        if current is None:
            return "The list is empty"

        previous = None
        end = False

        while not end:
            if current.getnextdata() is None:
                end = True
            else:
                previous = current
                current = current.getnextdata()

        if previous is None:
            self.head = current.getnextdata()
        else:
            previous.setnextdata(None)

        return current.data()

    def __popindex(self, index):
        current = self.head

        if current is None:
            return "The list is empty"

        previous = None
        counter = 0
        found = False

        data = None

        while current is not None and not found:
            if counter == index:
                found = True
                data = current.data()
            else:
                previous = current
                current = current.getnextdata()
                counter += 1

        if found:
            if previous is None:
                self.head = current.getnextdata()
            else:
                previous.setnextdata(current.getnextdata())
        else:
            print("Index too big")

        return data


if __name__ == "__main__":
    import random

    myLList = UnorderedList()
    for i in range(100):
        num = random.randint(0, 100)
        myLList.add(num)

    print(myLList.index(5))
    print(myLList.size())
    print(myLList.pop())
    myLList.remove(5)
    print(myLList.size())
