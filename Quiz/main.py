quiz = {
    'Question 1': {"What is the capital of Imo State?":'owerri'},
    'Question 2': {'What is the capital of FCT?': 'abuja'},
    'Question 3': {'What is my name?': 'princewill'}
}

number_passed = 0
for i in quiz:
    for y in quiz[i]:
        print(i, "\n", y)
        answer = input('=> ').lower()
        if answer == quiz[i][y]:
            print("\n>> Correct! <<\n")
            number_passed+=1
        else:
            print('\n>> Wrong! <<\n')
print(f"Score >> {(number_passed*100)/3}%")