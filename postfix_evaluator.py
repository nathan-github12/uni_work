class Evaluate_postfix:

    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def Top(self):
        return self.array[-1]

    def pop(self):
        if not self.isEmpty():
            self.top = self.top -1
            return self.array.pop()
        else:
            return "empty (cant pop)"

    def push(self, operator):
        self.top = self.top + 1
        self.array.append(operator)


    def evaluateExpression(self, exp):
        for i in exp:
            if i.isdigit():
                self.push(i)

            else:
                num1 = self.pop()
                num2 = self.pop()
                self.push(str(eval(num2 + i + num1)))


        return int(self.pop())

expression = input("Please enter a postfix expression")
out  = Evaluate_postfix(len(expression))
print("the postfix evaluation of this expression is: ", (out.evaluateExpression(expression)))
       
        
