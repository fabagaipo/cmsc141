class StackClass:
  def __init__(self, itemlist = []):
    self.size = 0
    self.items = itemlist

  def isEmpty(self):
    return True if self.items == [] else False

  def peek(self):
    return self.items[-1:][0]

  def pop(self):
    self.size -= 1
    return self.items.pop()

  def push(self, item):
    self.items.append(item)
    self.size += 1


class Node:
  def __init__(self, item):
    self.item = item
    self.parent = ''
    self.rightChild = ''
    self.leftChild = ''
    self.startStates = []
    self.endStates = []

  
class Tree:
  def __init__(self, root):
    self.root = root


def fileRead():
	from sys import argv
	script = argv
	input_file = open('mpa3.in', 'r')

	data = input_file.read()
	input_file.close()

	return data

def cleanString(string): 
  return string.replace(' ', '')

def getPrecedence(operator): # precedence of the operators
  return { '(' : 1, '+' : 2, '-' : 3, '*' : 4}.get(operator, 0)

def initRegex(regEx): # put - for concats
  newRegEx = ""
  allOps = ['+', '*']
  biOps = ['+']

  lenEx = len(regEx)
  for x in range(0, lenEx):
    ch1 = regEx[x]
    newRegEx += ch1
    
    if x + 1 < lenEx:
      ch2 = regEx[x + 1]

      if ((ch1 != '(' and ch2 != ')') and ch2 not in allOps and ch1 not in biOps):
        newRegEx += '-'
  
  return newRegEx

def toPostfix(stringArr): # transforms the regEx to a postfix notation
  postfix = []
  opStack = StackClass();

  for x in range(0, len(stringArr)):
    if stringArr[x] == 'a' or stringArr[x] == 'b':
      postfix.append(stringArr[x])

    elif stringArr[x] == '(':
      opStack.push(stringArr[x])

    elif stringArr[x] == ')':
      top = opStack.pop()

      while top != '(':
        postfix.append(top)
        top = opStack.pop()
    
    else:
      while (not opStack.isEmpty() and (getPrecedence(opStack.peek()) >= getPrecedence(stringArr[x]))):
        postfix.append(opStack.pop())

      opStack.push(stringArr[x])
  
  while not opStack.isEmpty():
    postfix.append(opStack.pop())

  return postfix

def generateExpTree(regEx): # makes an expression tree and assigns startStates and endStates
  stack = StackClass()
  ctr = 1

  lenEx = len(regEx)
  for x in range(0, lenEx):
    c = regEx[x]

    if c == 'a' or c == 'b':
      n = Node(c)
      n.startStates.append(ctr)
      n.endStates.append(ctr)
      ctr += 1
      stack.push(n)

    elif c == '*':
      parentOp = Node(c)
      parentOp.leftChild = stack.pop()
      parentOp.leftChild.parent = parentOp

      parentOp.startStates = parentOp.leftChild.startStates
      parentOp.endStates = parentOp.leftChild.endStates

      populateDic(parentOp.leftChild.startStates, parentOp.leftChild.endStates)

      stack.push(parentOp)

    elif c == '+':
      parentOp = Node(c)
      parentOp.rightChild = stack.pop()
      parentOp.leftChild = stack.pop()
      parentOp.rightChild.parent = parentOp
      parentOp.leftChild.parent = parentOp

      parentOp.startStates = union(parentOp.leftChild.startStates, parentOp.rightChild.startStates)
      parentOp.endStates = union(parentOp.leftChild.endStates, parentOp.rightChild.endStates)

      stack.push(parentOp)

    elif c == '-':
      parentOp = Node(c)
      parentOp.rightChild = stack.pop()
      parentOp.leftChild = stack.pop()
      parentOp.rightChild.parent = parentOp
      parentOp.leftChild.parent = parentOp

      if parentOp.leftChild.item == '*':
        parentOp.startStates = union(parentOp.leftChild.startStates, parentOp.rightChild.startStates)
      else:
        parentOp.startStates = parentOp.leftChild.startStates

      if parentOp.rightChild.item == '*':
        parentOp.endStates = union(parentOp.leftChild.endStates, parentOp.rightChild.endStates)
      else:
        parentOp.endStates = parentOp.rightChild.endStates

      populateDic(parentOp.leftChild.endStates, parentOp.rightChild.startStates)

      stack.push(parentOp)

  return stack.pop()

def populateDic(start, end): # populates the dictionary with the states from expression tree with the followpos algorithm
  startLen = len(start)
  for x in range(0, startLen):
    c = start[x]
    if c not in followPosArr:
      followPosArr[c] = []
    for y in range(0, len(end)):
      d = end[y]
      if d not in followPosArr[c]:
        followPosArr[c].append(d)

def printDic(): # prints keys, elements of dictionary
  print(followPosArr.items())

def union(l1, l2): # unions 2 arrays
  res = []
  for x in range(0, len(l1)):
    res.append(l1[x])
  for x in range(0, len(l2)):
    if l2[x] not in res:
      res.append(l2[x])

  return res

def resetFollowPosArr(): # clears the dictionary
  followPosArr.clear()

def generateCheckArr(regEx): # removes all the operators from the regEx
  checkString = []
  lenEx = len(regEx)
  for x in range(0, lenEx):
    if regEx[x] not in operators:
      checkString.append(regEx[x])
  return checkString

def generateBooleanArr(i): # generates an array of 0's for boolean array
  arr = []
  while i > 0:
    arr.append(0)
    i -= 1
  return arr

def convertStr(string): # converts a string to a list
  arr = []
  for x in range(len(string)):
    arr.append(string[x])
  return arr

def mapArr(arr1, arr2): # maps 1's to arr2 from the positions contained in the arr1
  for x in range(0, len(arr1)):
    arr2[arr1[x] - 1] = 1
  return arr2

def deepCopy(arr1):
  l = []
  for x in range(0, len(arr1)):
    l.append(arr1[x])
  return l

def isGenerated(regEx, string):
  regEx = toPostfix(initRegex(regEx))
  root = generateExpTree(regEx)
  checkString = generateCheckArr(regEx)

  tmp = deepCopy(root.startStates)

  string = convertStr(string)

  while len(string) > 0:
    char = string.pop(0)
    bits = generateBooleanArr(len(checkString))
    
    for x in range(0, len(tmp)):
      if char == checkString[tmp[x] - 1]:
        bits[x] = 1
    tmp = []
    for x in range(0, len(bits)):
      if bits[x] == 1:
        ind = x + 1
        if ind in followPosArr:
          l = followPosArr[ind]
        else:
          l = []
        tmp = union(tmp, l)
 
  return 'yes' if finalCheck(root.endStates, bits) else 'no'
  
def finalCheck(finalState, currentState): # check if any of the current states are in the finalstates
#   print("acceptable positions of final states: "), finalState
#   print ("final states: "), currentState
  for x in range(0, len(finalState)):
    if currentState[finalState[x] - 1] == 1:
      return True
  return False

def execute():
  data = fileRead()
  output_file = open("bagaipomp3.out", 'w') 
  inputData = data.split('\n')

  testCase = int(inputData[0])
  i = 1

  while(testCase > 0):
    regEx = inputData[i]
    i += 1
    numString = int(inputData[i])
    i += 1

    while(numString > 0):
      output_file.write(isGenerated(cleanString(regEx), cleanString(inputData[i])) + "\n")
      numString -= 1
      i += 1
      resetFollowPosArr()

    testCase -= 1
  
  output_file.truncate()
  output_file.close()


operators = ['+','*','-']
followPosArr = {

}

execute()
