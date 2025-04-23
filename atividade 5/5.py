def verificar_triangulo(lado1, lado2, lado3):
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        return True
    else:
        return False

def tipo_triangulo(lado1, lado2, lado3):

    if not verificar_triangulo(lado1, lado2, lado3):
        return "Os valores informados não formam um triângulo válido."
    
    if lado1 == lado2 == lado3:
        return "Triângulo equilátero: Todos os três lados são iguais."
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Triângulo isósceles: Dois lados são iguais e um é diferente."
    else:
        return "Triângulo escaleno: Todos os lados possuem medidas diferentes."

def main():
    lado1 = float(input("Digite o valor do primeiro lado: "))
    lado2 = float(input("Digite o valor do segundo lado: "))
    lado3 = float(input("Digite o valor do terceiro lado: "))
    resultado = tipo_triangulo(lado1, lado2, lado3)
    print(resultado)

main()