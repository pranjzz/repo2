try:
  age=int(input("enter your age:"))
  if(age>=18):
    print("you are eligible to vote")
  else:
except ValueError:
  print("enter a valid age")
