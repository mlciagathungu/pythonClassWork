

myName=input(
   " Enter your name:"
)
print( f"{myName}","Welcome my console calculator")
while True:
   print("\nAvailable operations:")
   print("1. Addition(+)")
   print("2. Subtraction(-)")
   print("3. Multiplication(*)")
   print("4. Division(/)")
   print("5. Modulus(%)")
   print("6. Exit")

   my_choice=input(" Enter your choice:1-6 ")
   num1=float(input(" Enter your first number:"))
   num2=float(input(" Enter your second number:"))

   if my_choice=="1-6":
      print(f"{myName}" "Thankyou for using this calculator!")
      break
   elif my_choice=="1":
      print(f"{myName}" "Your have entered the addition operation")
      result=num1+num2
      print(f"{num1}  +{num2} " f"{result} =")
   elif my_choice=="2":
         print( f"{myName} ""You have entered the subtraction operation")
         result = num1 -num2
         print(f"{num1}  -{num2} " f"{result} =")
   elif my_choice=="3":
      print( f"{myName} ""You have entered the multiplication operation")
      result = num1 *num2
      print(f"{num1}  *{num2} =" f"{result} ")
   elif my_choice=="4":
      print( f"{myName} " "You have entered the division operation")
      result = num1/num2
      print(f"{num1}  /{num2} ="  f"{result} ")
   elif my_choice=="5":
      print( f"{myName} ","You have entered the modulus operation")
      result = num1%num2
      print(f"{num1}  %{num2} =" f"{result} ")
   elif my_choice == "6":
      print(f"{myName} " "You have entered an exit operation")

   else:
      print(f"{myName} " "You entered"  f"{my_choice} " "which is not available")
      break
