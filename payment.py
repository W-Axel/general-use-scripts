import numpy as np

a = "AXEL"
g = "GAETAN"
j = "JERNE"
l = "LAURE"
t = "THOMAS"
names = np.array([a,g,j,l,t])

class Payment:
    def __init__(self, name, price, participants):
        self.name = name
        self.price = price
        self.participants = participants

    def process(self):
        for n in range(0, len(names)):
            for m in self.participants:
                if (names[n] == m) & (m != self.name):
                    owes[n,np.where(names == self.name)] += self.price / len(self.participants)
    

def simplify():
    for n in range(0, len(names)):
        for m in range(0, len(names)):
            if (owes[n,m] >= owes[m,n]) & (n != m):
                owes[n,m] -= owes[m,n]
                owes[m,n] = 0
            owes[n,m] = round(owes[n,m], 2)

def receipt():
    for n in range(0, len(names)):
        for m in range(0, len(names)):
            if (owes[n,m] != 0):
                print(f"{names[n]} owes {names[m]} {owes[n,m]} euro")

owes = np.zeros((5,5))

# Fritwerk
Payment(a, 17.4, [a, j]).process()
# Absynth
Payment(j, 65.47, [a, g, j, t]).process()
# Gluwein
Payment(g, 22, [a, g, j, l, t]).process()
# Flamkuchen
Payment(l, 23, [a, g, j, t]).process()
# Pintjs (markt)
Payment(g, 16, [a, g, j, t]).process()
# Pintjs (café)
Payment(t, 44, [a, g, j, l, t]).process()

simplify()
receipt()