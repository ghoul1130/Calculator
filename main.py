from replit import clear
from art import logo
print(logo)

#add
def add(n1,n2):
  return n1+n2

#sub
def sub(n1,n2):
  return n1-n2

#mul
def mul(n1,n2):
  return n1*n2

#div
def div(n1,n2):
  return n1/n2


operator_dic ={
  "+" : add,
  "-" : sub,
  "*" : mul,
  "/" : div
}

def calulator():
  n1 = float(input("First Number: "))
  cal_finished = False
  while not cal_finished:
    for op in operator_dic:
      print(op)  
    symbol = input("Enter Operator: ")
    n2 = float(input("Next Number: "))
    func = operator_dic[symbol]
    result = func(n1,n2)
    print(f"{n1} {symbol} {n2} = {result}")
    
    choice = input(f"\ntype 'y' to continue with {result} or 'n' to quit: ")
    if choice == "n":
      clear()
      cal_finished = True
      calulator()
    elif choice == "y":
      n1 = result

calulator()
    
