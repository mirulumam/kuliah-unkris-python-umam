# please install regex package first from command line
# command to install:
# python -m pip install regex
import regex

class Stack:
    def __init__(self):
        self.item = []
    
    def push(self,it):
        self.item.append(it)
    def peek(self):
        if self.isempty() == True:
            return 0
        return self.item[-1]
    
    def pop(self):
        if self.isempty() == True:
            return 0
        return(self.item.pop())
    
    def length(self):
        return (len(self.item))
    
    
    def isempty(self):
        if self.item == []:
            return True
        else:
            return False

def infixToPostfix(infixexpr):
    infixexpr = infixexpr.replace(" ", "").replace("", " ")[1: -1]
    # [+-]*: any sequence of these two characters, which serve as unary operators. + is in that sense a useless operator, but it is allowed.
    # [\d\w\s]: any non-empty sequence of digits, words, and whitespace. representing an unsigned integer
    # (?1): recursion. This will use the whole regular expression -- except for the ^ and $ anchors! -- in a recursive way. With the surrounding, literal parentheses, this allows for expression nesting.
    # [+^*/-]: any binary operator (extend with more operators as needed)
    # (?2): to match the second operand of a binary operator, re-using the same pattern as was used to match the first operand.
    result = regex.match(r"^(([+-]*[\d\w\s\(\)]+|\((?1)\))([+^*/-](?2))*)$", infixexpr)
    if result is None:
        return "Invalid Infix"

    prec = {}
    prec["^"] = 3
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
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
        else:
            while (not opStack.isempty()) and (prec[opStack.peek()] >= prec[token]): postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isempty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)






