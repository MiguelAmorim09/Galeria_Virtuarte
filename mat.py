class Matematica:
    def __init__(self, numeroBase):
        self._numeroBase = numeroBase

    def fatorial(self, x):
        if x == 0:
            return 1
        else:
            return x * self.fatorial(x - 1)

    def triangulo_de_Pascal(self):
        triangulo = []
        for n in range(self._numeroBase):
            linha = ""
            for k in range(n + 1):
                coeficiente = self.fatorial(n) // (self.fatorial(k) * self.fatorial(n - k))
                linha += f"{coeficiente:6}"
            triangulo.append(linha)
        return triangulo
