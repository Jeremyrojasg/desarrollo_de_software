def a_celcius(grado):
    return (grado - 32)*(5/9)
def a_farenheit(grado):
    return (grado * (9/5))+ 32

print("Ingrese la conversion que desea realizar\n1) Celcius a Farenheit\n2) Farenheit a Celcius")
op = int(input())
if op in [1,2]:
    print("Ingrese el valor que desea convertir")
    grado = int(input())
    if op ==1:
        valor = a_farenheit(grado)
        print(f"{grado}ºC equivalen a: {valor}ºF")
    else:
        valor = a_celcius(grado)
        print(f"{grado}ºF equivalen a: {valor}ºC")
else:
    print("El valor ingresado no es valido")