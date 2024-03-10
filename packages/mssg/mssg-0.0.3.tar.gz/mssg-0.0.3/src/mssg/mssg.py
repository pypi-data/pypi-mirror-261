
import collections
def countermssg(mssg):
    a=collections.Counter(mssg)
    print(a)
def gomssg():
    o=input("mssg:")
def frommssg(a="user"):
    print(a)
def mademssg():
    made=input("the made mssg:")
    n=collections.deque(made)
    for i in range(len(n)):
        print(n.pop())
        n.appendleft(0)
    print(n)
