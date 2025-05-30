# class demo:
#     def dis(self):
#         print("hi im 1")
#     def dis(self,x):
#         print("hi im 2 ")
# obj=demo()

# #obj.dis() this will throw type error dis() missing 1 required argument
# obj.dis(4)

class parent:
    def demo(self):
        print("parent call")
    def display(self):
        print("no overriding")
class child(parent):
    def demo(self):
        print("child call")
obj=child()
obj.demo()
obj.display()
obj2=parent()
obj2.demo()
