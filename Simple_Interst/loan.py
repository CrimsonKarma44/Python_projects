# loan = int(input("Loan: "))
# time = int(input("time: "))
# rate = int(input("rate of lone: "))

# loan -(repayment* time) + interest = 0

loan = 42000
repayment = 3500
rate = 10
count = 0
while loan > 0:
    interest = (loan*(rate/100))
    loan+= (interest-repayment)
    count+=1
    print(loan)

print(count)