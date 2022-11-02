class Segitiga:
    def __init__(self, sisi_X, sisi_Y, sisi_Z):
        self.X = sisi_X
        self.Y = sisi_Y
        self.Z = sisi_Z
        
    def jenis_segitiga(self):
        a = self.X
        b = self.Y
        c = self.Z
        if (a >= b and a >= c):
            x = a
            y = b
            z = c
        elif (b >= a and b >= c):
            x = b
            y = a
            z = c
        else:
            x = c
            y = a
            z = b
        
        if (x*x == (y*y + z*z)):
            print("Segitiga siku-siku\n")
        elif (a == b == c):
            print("Segitiga sama sisi\n")
        elif (a == b or b == c) and not (a == b == c):
            print("Segitiga sama kaki\n")
        else:
            print("Segitiga sembarang\n")

Segi3_A = Segitiga(1,2,3)
Segi3_B = Segitiga(12,16,20)
Segi3_C = Segitiga(9,9,15)
Segi3_D = Segitiga(5,5,5)

Segi3_A.jenis_segitiga()
Segi3_B.jenis_segitiga()
Segi3_C.jenis_segitiga()
Segi3_D.jenis_segitiga()
