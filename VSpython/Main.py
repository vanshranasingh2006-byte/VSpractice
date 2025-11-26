import random
score=0
count=1
print("Welcome to the Math Quiz!")  
while True:
    no1=random.randint(1,20)
    no2=random.randint(1,20)
    opp=random.choice(['+','-','*'])
   
    if opp=='+':
        ans=no1+no2    
    elif opp=='-':
        ans=no1-no2
    else:
        ans=no1*no2
    user_ans=int(input(f'What is {no1} {opp} {no2} ? '))
    
    if count==10:
        print(score,"out of 10")
        break
    
    if user_ans==ans:
        score+=1
        count+=1
        print('Correct Answer') 
        print("You got 1 point")
        print(score)
    
    else:
        print('Wrong Answer')
        print(f'The correct answer is {ans}')
        count+=1
        print(score)
        

    
    