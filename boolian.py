temperature = int(input("enter the current temperature"))
if temperature > 30:
      print("its too hot")
elif temperature >= 20:
      print("it's nice")
else:
      print("it's cold")
print("code sucssesfull")

age = 12
if age >= 18:
      message = "you are eligible for driver liscence"
else:
      message = "wait for right time"

#another interesting way to write this code
    
message1 = "eligible" if age >= 18 else "not eligible" #(turnary operator)
print(message1)
