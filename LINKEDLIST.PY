class List:
    def __init__(self,data):
        self.data=data
        self.address=None
class Linkedlist:
        def __init__(self):
            self.head=None
            self.last=None
        def createlist(self,n):
            newnode=List(n)
            if(self.head== None):
                self.head=newnode
                self.last=newnode
            else:
                self.last.address=newnode
                self.last=newnode
        def printlist(self):
            tem=self.head
            while(tem is not None):
                print(tem.data)
                tem=tem.address
        def insertfront(self,j):
            newnode=List(j)
            newnode.address=self.head
            self.head=newnode
        def insertlast(self,m):
                newnode=List(m)
                tem=self.last
                tem.address=newnode
        def anyposition(self,v,p):
            tem=self.head
            while p>0:
                prev=tem
                tem=tem.address
                p=p-1
            newnode=List(v)
            newnode.address=prev.address
            prev.address=newnode
        def deleteanyposition(self,p):
            p=p-1
            tem=self.head
            while p>0:
                prev=tem
                tem=tem.address
                p=p-1
            prev.address=tem.address
        def deletefirst(self):
            self.head=self.head.address
        
        def deletelast(self):
            tem=self.head
            while tem.address.address is not None:
                tem=tem.address
            tem.address=None
        def countnode(self):
            tem=self.head
            count=0
            while tem is not None:
                count=count+1
                tem=tem.address
            print(count)
x=Linkedlist()
x.createlist(11)
x.createlist(15)
x.createlist(17)
x.createlist(121)
x.insertlast(100)
x.insertfront(23)
x.anyposition(45,5)
x.deleteanyposition(3)
x.deletefirst()
#x.deletelast()
x.printlist()
x.countnode()