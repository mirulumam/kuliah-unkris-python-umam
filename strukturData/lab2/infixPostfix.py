# please install regex package first from command line
# command to install:
# python -m pip install regex
import ast
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

NUMBERS = "1234567890"
LETTERS = "QWERTYUIOPASDFGHJKLZXCVBNM"
OPERATORS = "^*/+-"

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
    opener = 0
    for token in tokenList:
        if token in LETTERS + NUMBERS:
            postfixList.append(token)
        elif token == '(':
            opener += 1
            opStack.push(token)
        elif token == ')':
            if opener == 0:
                return "Invalid Infix"
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
            opener -= 1
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