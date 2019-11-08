import sys
class A():
    def __init__(self,qq):
        self.qq = qq


    def eat(self):
        print(self.qq)




if __name__ == '__main__':
    # print(sys.path)
    a = A('11')
    b = A('22')
    print(a)
    print(b)
