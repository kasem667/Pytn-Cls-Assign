class A:
    def classA(self):
        print("I am in class A.")

class B (A):
    def classB(self):
        print("I am in class B.")

class D:
    def classD(self):
        print("I am in class D.")

class C (A, D):
    def classC(self):
        print("I am in class C.")

class E (B):
    def classE(self):
        print("I am in class E.")

class F (B):
    def classF(self):
        print("I am in class F.")

method = E()
method.classE()
method.classB()
method.classA()