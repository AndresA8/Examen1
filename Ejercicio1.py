""" 1.Construir un programa que permita ingresar N (cantidad digitada por
el usuario) números enteros y cuente cuantos múltiplos de 2 y de 3 fueron ingresados (+1) """

num1 = 0
num2 = 0
x = True
contador = 0

while x != False: 
    contador += 1  
    num = int(input(f'Ingrese numero {contador}: '))    
    if(num % 2 == 0):
        num1 +=1
    if(num % 3 == 0):
        num2 += 1
    pregunta = input ('¿Ingresara otro valor? s/n ')
    if(pregunta == 'n'):
     x = False


print(f'Existen {num1} multiplos de 2')
print(f'Existen {num2} multiplos de 3')

