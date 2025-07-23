'''
Пусть 
z_{1} = 2 + 5i
z_{2} = 3 + i
Чему равно z_{1}/z_{2}?
'''

from fractions import Fraction as F
# z1 = complex(2, 5)
a, b = F(2), F(5)

# z2 = complex(3, 1)
c, d = F(3), F(1)

# (a + bi) / (c + di) = [(ac + bd) + (bc - ad)i] / (c² + d²)
denom = c**2 + d**2
real_part = (a * c + b * d) / denom
imag_part = (b * c - a * d) / denom

print(f"{real_part} + {imag_part}i")