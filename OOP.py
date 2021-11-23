def kalkulator(opcija):
    a =int(input("a: "))
    b =int(input("b: "))

    if opcija ==1:
        return a+b

    if opcija ==2:
        return a*b



class Kalkulator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def zbroji(self,ime):
        print(ime)
        return self.a + self.b

    #@staticmethod
    #def pomnozi(self, a,b):
    #    print("umnozak: ",a*b)

    def get_a(self):
        return self.a

    def set_a(self,a):
        self.a= a
        
def primjer(a, *args):           #tuple
    print(a)
    print(args)

primjer(2,3,4,5,6)


def primjer2(a,**kwargs):        #dictionary
    print(a)
    print(kwargs.get("novo"))

primjer2(2, ime="dani", novo="novo")

def default(b,a=19):   #vrijednost koja nije postavljena ide na prvo mjesto 
    print(a+b)
default(6)
