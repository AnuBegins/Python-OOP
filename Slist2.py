
# write functions to push and pop nodes in a single linked list of strings
# write a traverse function....


class Node:
    def __init__(self, value):  #constructor to initiate this object
        self.value = value  #stores a value
        self.next = None   # stores reference (to next item)

class StackList:
    def __init__(self):
        self.head = None

    def push(self, value):
        node = Node(value)
        runner = self.head

        if runner is None:
            self.head = node
        else:
            while runner.next is not None:
                runner = runner.next
            runner.next = node

    def pop(self):
        previous = None
        runner = self.head
#        count = 1

        while runner.next is not None:
#            print("Attempt",count)
            previous = runner
            runner = runner.next
#            print("new runner is:",runner.value)
#            count +=1
        previous.next = None
        x = runner
        return(x.value)
        
        
    def printAllValues(self, msg=""):
        runner = self.head          # create a runner     
        print("\n\nhead points to ", id(self.head))
        print("Printing the values in the list ---", msg,"---")
        while(runner.next != None):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next        
        print(id(runner), runner.value, id(runner.next))


sm = StackList()
sm.push('Jae')
sm.push('Justin')
sm.push('Ken')
sm.printAllValues("current Slist")
print("popped name is:", sm.pop())
sm.printAllValues("current Slist")


