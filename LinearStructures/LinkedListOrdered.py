class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.nextdata = None

    def Data(self):
        return self.data

    def nextdatadata(self):
        return self.nextdata

    def setData(self,newdata):
        self.data = newdata

    def setnextdata(self,newnextdata):
        self.nextdata = newnextdata


class Ordered:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.nextdatadata()

        return count

    def index(self, index):
        counter = 0
        current = self.head
        while current is not None:
            if counter == index:
                return current.Data()
            else:
                counter += 1
                current = current.nextdatadata()

    def search(self, item):
        current = self.head
        found = False
        stop = False

        while current is not None and not found and not stop:
            if current.Data() == item:
                found = True
            else:
                if current.Data() > item:
                    stop = True
                else:
                    current = current.nextdatadata()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.Data() > item:
                stop = True
            else:
                previous = current
                current = current.nextdatadata()

        temp = Node(item)
        if previous is None:
            temp.setnextdata(self.head)
            self.head = temp
        else:
            temp.setnextdata(current)
            previous.setnextdata(temp)

    def pop(self, index=None):
        if index is None:
            return self.__pop()
        else:
            return self.__popindex(index)

    def __pop(self):
        current = self.head

        if current is None:
            return "Empty List"

        previous = None
        end = False

        while not end:
            if current.nextdatadata() is None:
                end = True
            else:
                previous = current
                current = current.nextdatadata()

        if previous is None:
            self.head = current.nextdatadata()
        else:
            previous.setnextdata(None)

        return current.Data()

    def __popindex(self, index):
        current = self.head

        if current is None:
            return "Empty List"

        previous = None
        counter = 0
        found = False

        data = None

        while current is not None and not found:
            if counter == index:
                found = True
                data = current.Data()
            else:
                previous = current
                current = current.nextdatadata()
                counter += 1

        if found:
            if previous is None:
                self.head = current.nextdatadata()
            else:
                previous.setnextdata(current.nextdatadata())
        else:
            print("Index too big")

        return data



