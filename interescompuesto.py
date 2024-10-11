def calcularintereses(p,r,t,n):
    A = p*(1+r/n)**(n*t)
    return A
p = float(input("capital inicial"))
r = float(input("interés anual en porcentaje"))
t = float(input("número de año"))
n = float(input("nº de periodo por año"))

capitalfinal = calcularintereses(p,r,1,n)
print(f"la cantidad final después de 1 de años será {capitalfinal}")

capitalfinal = calcularintereses(p,r,2,n)
print(f"la cantidad final después de 2 de años será {capitalfinal}")

capitalfinal = calcularintereses(p,r,3,n)
print(f"la cantidad final después de 3 de años será {capitalfinal}")

capitalfinal = calcularintereses(p,r,4,n)
print(f"la cantidad final después de 4 de años será {capitalfinal}")

capitalfinal = calcularintereses(p,r,5,n)
print(f"la cantidad final después de 5 de años será {capitalfinal}")

capitalfinal = calcularintereses(p,r,6,n)
print(f"la cantidad final después de 6 de años será {capitalfinal}")

capitalfinal = calcularintereses(p,r,7,n)
print(f"la cantidad final después de 7 de años será {capitalfinal}")

capitalfinal = calcularintereses(p,r,8,n)
print(f"la cantidad final después de 8 de años será {capitalfinal}")

capitalfinal = calcularintereses(p,r,9,n)
print(f"la cantidad final después de 9 de años será {capitalfinal}")

capitalfinal = calcularintereses(p,r,10,n)
print(f"la cantidad final después de 10 de años será {capitalfinal}")