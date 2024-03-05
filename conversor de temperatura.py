#CONVERSOR DE TEMPERATURA

#Grados centígrados = (grados Fahrenheit − 32) × 5/9.
#Grados Fahrenheit = (grados centígrados × 9/5) +32

#Formula para calcular Centigrados
def calcel(t):
    return int((t-32)*(5/9))

#Formula para calcular Fahrenheit
def calfahr(t):
    return int(t*(9/5)+32)

choise = input('Elige sólo con la letra \n\nQué unidad quieres obtener? Fahrenheit(F) o Celsius(C)?: ')
choise = choise.lower()

temp = input('Ingresa los grados de temperatura: ')
temp = int(temp)

if choise == 'c':
    print('A- La temperatura es: ')
    print(calcel(temp),'grados centígrados')
elif choise == 'f':
    print('B- La temperatura es: ')
    print(calfahr(temp),'grados farherenheit')
else:
    print('Discula, debes elegir unicamente entre Fahrenheit(F) o Celsius(C)')

