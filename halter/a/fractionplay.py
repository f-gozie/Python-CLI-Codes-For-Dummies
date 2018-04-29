from fractions import Fraction

fraction = Fraction
f1 = fraction(3, 4)
print(f1)
print(f1.numerator)
print(f1.denominator)
print(float(f1))
f2 = Fraction(1, 8)
print(f2)
f3 = f1 + f2
print(f3)