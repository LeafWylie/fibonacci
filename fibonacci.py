terms = int(input("how many terms: "))

n1,n2 = 0, 1
count = 0

if terms <= 0:
  print("not valid")
elif terms == 1:
  print(n1)
else:
   while count < terms:
       print(n1)
       n3 = n1 + n2
       
       n1 = n2
       n2 = n3
       count += 1
