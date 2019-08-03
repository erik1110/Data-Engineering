class Count(object):
    
    def add(self,x,y):
        return x+y
    
    def sub(self,x,y):
        return x-y

if __name__ == '__main__':
    c=Count()
    print(c.add(1,2))
    print(c.sub(10,5))