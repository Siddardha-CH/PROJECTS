import random
l=[0,1,2]
s=random.choice(l)
print("0 for rock,1 for paper,2 for scissor")
k=int(input())
if(s==0):
  print("computer - rock")
if(s==1):
  print("computer - paper")
if(s==2):
  print("computer - scissor")
if k==0:
  print("you - rock")
if k==1:
  print("you - paper")
if k==2:
  print("you - scissor")
if(s==0):
    if(k==0):
        print("tie")
    if(k==1):
        print("win")
    if(k==2):
        print("lose")
if(s==1):
    if(k==0):
        print("lose")
    if(k==1):
        print("tie")
    if(k==2):
        print("win")
if(s==2):
    if(k==0):
        print("win")
    if(k==1):
        print("lose")
    if(k==2):
        print("tie")
