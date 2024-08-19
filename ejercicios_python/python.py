import sys

if len(sys.argv) > 1:
    parametro = sys.argv[1]
    print(f"Hola {parametro}")
else:
    print("No existen parametros")