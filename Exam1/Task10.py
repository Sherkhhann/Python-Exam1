numbers=[2, 4, 6, 8, 10, 12, 14]
i=0
s=0
while i<len(numbers):
 if numbers[i]==numbers:
  s+=1
 i+=1
if s>1:
 print("False")
else:
 print("True")