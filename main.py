# input_num = int(input("Enter the number of rows: "))
# input_num = input_num + 1
# list = [] #an empty list
# for n in range(input_num):
#     list.append([])
#     list[n].append(1)
#     for m in range(1, n):
#         list[n].append(list[n - 1][m - 1] + list[n - 1][m])
#     if(input_num != 0):
#         list[n].append(1)
# for n in range(input_num):
#     print(" " * (input_num - n), end = " ", sep = " ")
#     for m in range(0, n + 1):
#         print('{0:5}'.format(list[n][m]), end = " ", sep = " ")
#     print()

#############################################################################
# function binomial (n, k) = n! / (k! * (n - k)!)
import math
# def binomial(n, k):
#     if k > n - k:
#         k = n - k
#     result = 1
#     for i in range(1, k + 1):
#         result *= n - (k - i)
#         result //= i
#     return result

# monresult= binomial(27237,134)
# len(str(monresult))
# print(binomial(27237,134))
# print(math.factorial(10000))
#############################################################################


#  factorial logarithme (n!)
#  logarithme (n!) = logarithme (n) + logarithme (n - 1) + ... + logarithme (n - k) + logarithme (n - k - 1) + ...
# def logarithme(n):
#     result = 0
#     for i in range(1, n + 1):
#         result += math.log(i)
#     return result
#
# print(logarithme(10000000))

#############################################################################

# Polynômes de Bernstein
def binomial(n, k):
    if k > n - k:
        k = n - k
    result = 1
    for i in range(1, k + 1):
        result *= n - (k - i)
        result //= i
    return result
def Bernstein(n, k, t):
    return binomial(n, k) * (t ** k) * ((1 - t) ** (n - k))
print(Bernstein(14, 12, 0.5))

# trace 5 points en utilisant les polynômes de Bernstein en utilisant numpy
import numpy as np
import matplotlib.pyplot as plt

def Bernstein(n, k, t):
    return binomial(n, k) * (t ** k) * ((1 - t) ** (n - k))

t = np.linspace(0, 1, 1000)



plt.plot(t, [Bernstein(0, 0, x) for x in t])
plt.show()  # affiche le graphique