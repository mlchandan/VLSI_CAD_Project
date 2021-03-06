#Code is using STACK to convert the boolean infix expression to postfix expression
# NOT(~) operation is to be performed within the brackets to specify its limit 
#Example : ~ ( A )   
# ~  A | B ==> This is equivalent to ~ ( A | B ) in this code

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


def infixToPostfix(infixexpr):
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    print  tokenList

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
            if  not opStack.isEmpty() :
                 if opStack.peek()== "~" :
                      postfixList.append(opStack.pop())
            
        else:
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

#print(infixToPostfix("A * B + C * D"))
#print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

print(infixToPostfix("  ~  ( A  | ( B   &  C ) ) ^ D  "))
#Result :- A B C & | ~ D ^
