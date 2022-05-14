# please install regex package first from command line
# command to install:
# python -m pip install regex
import ast

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

NUMBERS = "1234567890"
LETTERS = "QWERTYUIOPASDFGHJKLZXCVBNM"
OPERATORS = "^*/+-"

def infixToPostfix(infixexpr):
    try:
        ast.parse(infixexpr)
    except:
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
        if token in LETTERS + NUMBERS:
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

def doMath(op, op1, op2):
    if op == "^":
        return pow(op1, op2)
    elif op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

def evaluation(expression, tokenType):
    operandStack = Stack()
    tokenList = expression.split()

    for token in tokenList:
        if token in tokenType:
            operandStack.push(int(token))
        elif token in OPERATORS:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
        else:
            return "Token tidak valid: {0}".format(token)

    return operandStack.pop()

def postFixEvaluation(postfixExpr):
    return evaluation(postfixExpr, NUMBERS)

def infixEvaluation(infixExpr):
    return evaluation(infixExpr, NUMBERS)