def calculadora(numero1, numero2):
    soma = numero1 + numero2
    subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2

    if numero2 == 0:
        divisao = "Não é possível dividir por zero"
    else:
        divisao = numero1 / numero2

    print(f"Soma: {numero1} + {numero2} = {soma}")
    print(f"Subtração: {numero1} - {numero2} = {subtracao}")
    print(f"Multiplicação: {numero1} * {numero2} = {multiplicacao}")
    print(f"Divisão: {numero1} / {numero2} = {