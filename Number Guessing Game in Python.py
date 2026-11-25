import random
 
random_number=random.randint(1,100)
print(random_number)
limit_guess_number=7

while True:
 try:
  numberinput=int(input("guess the number between 1 and 100?"))
  if limit_guess_number==1:
   break
  
  elif numberinput>random_number and 1 <= numberinput <= 100:
    print(f"the guess input number {numberinput} is more than random number")
    limit_guess_number-=1
  elif numberinput<random_number and 1 <= numberinput <= 100:

    print(f"the guess input number {numberinput} is less than random number")
    
    limit_guess_number-=1
  elif (numberinput==random_number):
   print("the number is matched")
   break
 except KeyboardInterrupt:
    print("canceled")
    break
 except ValueError:
    print("type number ! not string") 
       
