class Stack:
  def __init__(self):
    self.items = []
  def isEmpty(self):
    return self.itmes == []
  def push(self,item):
    self.items.append(item)
  def pop(self):
    return self.items.pop()
  def peek(self):
    return self.items[len(self.items) - 1]
  def size(self):
    return len(self.items)

def baseconverter(decNumber, base):
  remstack = Stack()
  digit = '0123456789ABCDEFG'
  while decNumber > 0:
    rem = decNumber % base
    remstack.push(rem)
    decNUmber = decNumber // base
  binstring = ''
  while not remstack.isEmpty():
    binstring += digit[remstack.pop()]
  return binstack
      
    
