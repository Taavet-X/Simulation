import GeneradorLinealCongruente
import X2
import KolmogorovSmirnov

GeneradorLinealCongruente.execute(x0 = 5, a = 106, c = 1283, m = 6075)
print("-- X^2 --")
X2.execute("GLC.txt")
print("-- Kolmogorov Smirnov --")
KolmogorovSmirnov.execute("GLC.txt")