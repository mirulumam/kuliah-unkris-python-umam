class Stack:
    def __init__(self): self.item = []
    def push(self, it): self.item.append(it)
    def peek(self):
        if self.isEmpty() == True: return 0
        return self.item[-1]
    def pop(self):
        if self.isEmpty() == True: return 0
        return(self.item.pop())
    def length(self): return (len(self.item))
    def isEmpty(self):
        if self.item == []: return True
        else: return False

r_stack = Stack()

def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            r_stack.push(convert_string[n])
        else:
            r_stack.push(convert_string[n % base])

        n = n // base

    res = ""
    while not r_stack.isEmpty():
        res = res + str(r_stack.pop())
    return res

print(to_str(1453, 16))
print(to_str(1980, 16))
