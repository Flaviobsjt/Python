# importações:
# import bebidas
# import doces
import math
# importações únicas:
# from doces import pudim
# from bebidas import cafe

# exemplos de importações?
# math
# (ceil = arredonda pra cima)
# (floor = arredonda pra baixo)
# (trunc = truncar um número)
# (pow = potencia)
# (sqrt = raiz quadrada)
# (factorial = fatorial)
# import math (from math import sqrt), (from math import sqrt, ceil)

from math import ceil
número = int(input('Digite um número: '))
raiz = math.sqrt(número)
print('A raiz de {} é igual {:.1f}'.format(número, math.ceil(raiz)))

# import random
#num = random.radint (1, 10)
#print(num_)