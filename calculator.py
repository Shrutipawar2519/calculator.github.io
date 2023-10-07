def add(a,b):
    tot=a+b
    print('Ans:',tot)
def sub(a,b):
    tot=a-b
    print('Ans:',tot)
def div(a,b):
    tot=a/b
    print('Ans:',tot)
def mul(a,b):
    tot=a*b
    print('Ans:',tot)
def mod(a,b):
    tot=a%b
    print('Ans:',tot)
def fd(a,b):
    tot=a//b
    print('Ans:',tot)
def pe(a,b):
    tot=a**b
    print('Ans:',tot)
while True:
 ch=int(input('please enter your choice:,\n1.addition\t\t2.substraction\n3.division\t\t4.multiplication\n5.modulor\t\t6.floor division \n7.power exponent \t8.Exit'))
 if ch==8:
      print('THANK YOU')
      break
 fn=int(input('please enter first number:'))
 sn=int(input('please enter second number:'))

 if ch==1:
  add(fn,sn)
 elif ch==2:
   sub(fn,sn)
 elif ch==3:
   div(fn,sn)
 elif ch==4:
  mul(fn,sn)
 elif ch==5:
   mod(fn,sn)
 elif ch==6:
   fd(fn,sn)
 elif ch==7:
   pe(fn,sn)
 else:
      print('PLEASE ENTER VALID CHOICE')

   
    
