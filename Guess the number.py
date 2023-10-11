import random

lr,hr=map(int,input("Enter lower range and higher range :").split())
num=random.randint(lr,hr)
guess=''
count=0
while guess!= num:
    count+=1
    guess=int(input("Make a guess :"))
    if guess<num:
        print("Go higher")
    elif guess>num:
        print("Go lower")
print(f'Congrats, you found the number in {count} tries')

    
