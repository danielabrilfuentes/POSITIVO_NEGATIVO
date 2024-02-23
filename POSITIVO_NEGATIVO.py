# programa para verificar si un numero es positivo o negativo 

# input 
x=int(input("digite un nomero: "))

# processing 
if x > 0:
    RTA = "positivo"
elif x == 0:
    RTA = "su numero es neutro"
else:
    RTA = "negativo"

# output 
print("el numero",x,"es",RTA)
