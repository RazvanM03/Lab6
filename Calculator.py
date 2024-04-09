class Calculator:
    def adunare(self, a, b):
        return a + b

    def scadere(self, a, b):
        return a - b

    def inmultire(self, a, b):
        return a * b

    def impartire(self, a, b):
        if b == 0:
            return "Eroare!"
        else:
            return a / b


calc = Calculator()

print("Adunare:", calc.adunare(5, 9))
print("Scadere:", calc.scadere(21, 9))
print("Inmultire:", calc.inmultire(5, 5))
print("Impartire:", calc.impartire(100, 0))
