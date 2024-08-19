def suma(op1, op2):
    return op1 + op2

def resta(op1,op2):
    return op1 - op2

def multiplicacion(op1,op2):
    return op1 * op2

def division(op1,op2):
    return op1 / op2

print("Ingrese operacion a realizar\n 1) Suma\n 2) Resta\n 3) Multiplicacion\n 4) Division")
op= int(input(""))
if op in [1,2,3,4]:
    print("Ingrese operador 1")
    op1 = int(input())
    print("Ingrese operador 1")
    op2 = int(input())
    if op == 1:
        resultado = suma(op1,op2)
    elif op == 2:
        resultado = resta(op1,op2)
    elif op == 3:
        resultado = multiplicacion(op1,op2)
    else:
        resultado = division(op1,op2)
    print(f"El resultado es: {resultado}")
else:
    print("El valor ingresado no es valido")