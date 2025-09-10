# Programa de calculadora b�sica
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return 'Error: Divisi�n por cero'
    return a / b

if __name__ == '__main__':
    print('Calculadora b�sica')
    print('Operaciones disponibles: suma, resta, multiplicaci�n, divisi�n')
    op = input('Ingrese la operaci�n: ')
    a = float(input('Ingrese el primer n�mero: '))
    b = float(input('Ingrese el segundo n�mero: '))
    if op == 'suma':
        print('Resultado:', sumar(a, b))
    elif op == 'resta':
        print('Resultado:', restar(a, b))
    elif op == 'multiplicaci�n':
        print('Resultado:', multiplicar(a, b))
    elif op == 'divisi�n':
        print('Resultado:', dividir(a, b))
    else:
        print('Operaci�n no v�lida')
