def calcularNotaAcceso(notaBachillerato, notaFaseGeneral):
    notaAcceso = 0.6*notaBachillerato + 0.4*notaFaseGeneral
    return notaAcceso 

def calcularNotaAdmision(notaAcceso, m1, m2, a, b):
    notaAdmision = notaAcceso + m1*a + m2*b
    return notaAdmision

notaBachillerato = float(input("Nota bachillerato"))
notaFaseGeneral = float(input("Nota fase general"))

notaAcceso = calcularNotaAcceso(notaBachillerato, notaFaseGeneral)
print(f"Tu nota de acceso es {notaAcceso}")

m1 = float(input("Nota materia específica 1"))
m2 = float(input("Nota materia específica 2"))
a = float(input("Coeficiente ponderación materia 1"))
b = float(input("Coeficiente ponderación materia 2"))

notaAdmision = calcularNotaAdmision(notaAcceso, m1, m2, a, b)
print(f"Tu nota de admision es {notaAdmision}")