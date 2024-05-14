print("**********CALCULADORA***********")
print("--------------MENU--------------")
print("1.- Suma")
print("2.- Resta")
print("3.- Multiplicación")
print("4.- División")
print("5.- Salir")
Salir = True
while Salir:
    opc=int(input("Elije una opción: "))
    if (opc==1):
        Sumando1=float(input("Introduce 1er sumando: "))
        Sumando2=float(input("Introduce 2º sumando: "))
        print("La suma es: ",Sumando1+Sumando2)
    elif (opc==2):
        Minuendo=float(input("introduce el minuendo: "))
        Sustraendo=float(input("introduce el sustraendo: "))
        print("La resta es: ",Minuendo-Sustraendo)
    elif (opc==3):
        Multiplicando=float(input("introduce el multipicando: "))
        Multiplicador=float(input("introduce el multiplicador: "))
        print("La multiplicación es: ",Multiplicando*Multiplicador)
    elif (opc==4):
        Dividendo=float(input("Introduce el dividendo: "))
        Divisor=float(input("Introduce el divisor: "))
        if Divisor==0:
            print("La división no tiene solución")
        else:
            print("La división es: ",Dividendo/Divisor)
            print("Además el resto es: ",Dividendo%Divisor)
    elif (opc==5):
       Salir = False
print("Hasta otra")       
