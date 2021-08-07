#function for addition
def add(x,y):
    return x+y
#function for subtraction   
def subtract(x,y):
    return x-y
#function for multiplication
def multiply(x,y):
    return x*y
#function for division
def divide(x,y):
    return x/y
#function for exponentiation 
def exponent(x,y):
    return x**y
print("select option:\n1.Addition\n2.Subtraction\n3.Multiplication.\n4.Division.\n5.exponentiation")
while True:
    option=input(" enter option number: ")
    
    if option in ('1','2','3','4','5'):
        
        a= int (input("enter the first number: "))
        b= int(input("enter the second number: "))
    
        if option =='1':
            print(a,"+", b,"=",add(a,b))
        elif option =='2':
            print(a,"-" ,b,"=" ,subtract(a,b))
        elif option=='3':
            print(a,"*", b,"=" ,multiply(a,b))
        elif option =='4':
            print(a,"/", b,"=" ,divide(a,b))
        elif option =='5':
            print(a,"**", b,"=" ,exponent(a,b))

        break
    else:
        print("Syntax error")
