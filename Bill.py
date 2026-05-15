
class Bill:
    def __init__(self,name1,name2,price1,price2):
        self.name1=name1
        self.name2=name2
        self.price1=price1
        self.price2=price2

    def calculate_bill(self,gst,discount):
        a=self.price1+self.price2
        if gst=="yes" or "YES":
            b=a+a*0.15
            print(b)
        else:
            pass
        if discount=="yes":
            print(b-a*0.1)
        else:
            pass
bill_calculator=Bill("laptop","phone",10000,2000)
bill_calculator.calculate_bill("yes",'yes')

      