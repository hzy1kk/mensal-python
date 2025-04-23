def verificar_par_e_positivo(numero):
    if numero > 0 and numero % 2 == 0:
        return True
    else:
        return False

def main():
    numero = float(input("Digite um número: "))
    
    if verificar_par_e_positivo(numero):
        print("True")
    else:
        print("False")

main()