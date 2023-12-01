import math

class ElegNagyTerulet():
    def szabalyos_kerulete(self, a, b, c):
        if int(a) + int(b) < int(c) or int(a) + int(c) < int(b) or int(b) + int(c) < int(a):
            raise ValueError("nem szabályos háromszög")

        if abs(int(a)) != int(a) or abs(int(b)) != int(b) or abs(int(c)) != int(c):
            raise ValueError("nem lehet a háromszög oldala negatív")
        
        return a + b + c

    def feladat_megoldo(self, a, b, c):
        e = ElegNagyTerulet()
        k = e.szabalyos_kerulete(a,b,c)
        
        print(f"{a} + {b} + {c} = {k}")
        
        if k < 30:
            print("Ez egy kis telek")
        elif k >= 30 and k <=50:
            print("Ez a telek pont jó")
        else:
            print("Ez egy nagy telek")

#e = ElegNagyTerulet()
#e.feladat_megoldo(1, 2, 8)
#e.feladat_megoldo(1, 2, 3)
#e.feladat_megoldo(10, 10, 12)
#e.feladat_megoldo(20, 20, 25)
#e.feladat_megoldo("alma", 1, "körte")
