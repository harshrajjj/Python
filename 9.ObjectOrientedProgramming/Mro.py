#method resolution order
class A:
    label = 'A : base class'

class B(A):
    label = 'B : derived class'

class C(A):
    label = 'C : derived class'

class D(B, C):
    pass

cup = D()
print(cup.label)
print(D.__mro__)