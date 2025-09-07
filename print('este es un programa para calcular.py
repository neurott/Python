print('este es un programa para calcular el area de un triangulo! ')
lado1=int(input('Ingrese el primer lado por favor: '))
lado2=int(input('Ingrese el segundo lado por favor: '))
lado3=int(input('Ingrese el tercer lado por favor: '))
s=(lado1 + lado2 + lado3)/2
area=(s* (s-lado1)*(s-lado2)*(s-lado3))**(1/2)
print('este es el area del trianguloooo!: ', area)
