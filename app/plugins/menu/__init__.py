from app.commands import Command

class MenuCommand(Command):
    def execute(self,args):
        print("-----------Menu:-----------")
        print("add <num1> <num2>")
        print("subtract <num1> <num2>")
        print("multiply <num1> <num2>")
        print("divide <num1> <num2>")
