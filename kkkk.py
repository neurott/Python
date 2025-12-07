import numpy as np
# a1 = 1000
# d = 5
# def a(n):
#     return a1+(n-1)*d
# # print(a(25))
# a1 = 2.1
# a2 = 2.2
# a3 = 2.3
# d = 0.1
# para sacar la d tienes q restar a2 -a1
# d = a2-a1
# def a(n):
#     return a1+(n-1)*d
# for i in range(1, 40):
#     print(f"{i} = a(n) = {a(i)}")

# a1 = 10
# r = 2

# def S(n):
#     return a1*r**(n-1)


# a1 = 250
# r=50

# def a(n):
#     return a1*r**(n-1)

# a1 = 300
# d = 40
# def a(n):
#     return a1+(n-1)*d

# print(a(8))
A = np.array([[4, 6],
              [8, 5],
              [2, 7]])

B = np.array([[1, 7],
              [4, 6],
              [6, 5]])

S = A+B

print(f"\n{S}")
print(f"\n{S[1][0]}")
print(A[2][1]*1.20)
print(B[2][1]*1.20)


# VERDADERO

# Si se quiere obtener la diferencia de consumo
# entre ambos servidores para cada aplicación,
#  ¿cuál operación matemática
#  debe realizarse entre las matrices A y B?

# Diferencia igual a resta
# sería
D = A-B
