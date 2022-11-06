
class Interest:

    def __init__(self, principal, rate, time):
        self.rate = rate
        self.principal = principal 
        self.time = time

    def simple(self):
        amount = self.principal*(self.rate/100)*self.time
        return "{:.2f}".format(amount)
    
    def compound(self):
        new_principal = int(self.principal)
        count = 0
        while count < self.time:
            I = ((int(self.rate)/100) * new_principal)
            new_principal += I
            count+=1
        return "{:.2f}".format(new_principal-self.principal)



# value = Interest(100,50,2)
# print(value.simple())
# print(value.compound())

while True:
    print("Interese: Simple or Compound")
    operation = input("=> ").lower()

    if operation == "simple":

        principal = int(input("starting capital: "))
        rate = int(input("Rate(in %): "))
        time = int(input("Time(nos of I occurance): "))

        value = Interest(principal, rate, time)
        print(value.simple(), "\n")

    elif operation == "compound":

        principal = int(input("starting capital: "))
        rate = int(input("Rate(in %): "))
        time = int(input("Time(nos of I occurance): "))

        value = Interest(principal, rate, time)
        print(value.compound(), "\n")
    
    elif operation == 'exit':
        break

    else:
        print("\n>> WRONG SYNTAX <<\n") 