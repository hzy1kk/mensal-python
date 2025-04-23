def verificar_par_impar(valor):
    try:
        numero = int(valor)

        if numero % 2 == 0:
            return True
        else:

            return False
    except ValueError:
        return "Valor informado é inválido"

entrada = input("Digite um número: ")

print(verificar_par_impar(entrada))