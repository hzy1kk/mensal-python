import re

def remover_caracteres(cpf):
    return re.sub(r'\D', '', cpf)

def identificar_estado(cpf):
    cpf = remover_caracteres(cpf)
    
    if len(cpf) != 11:
        return 'CPF INVÁLIDO'
    
    estados = {
        '1': 'Distrito Federal, Goiás, Mato Grosso do Sul, São Paulo',
        '2': 'Minas Gerais',
        '3': 'Rio de Janeiro, Espírito Santo',
        '4': 'São Paulo',
        '5': 'Paraná',
        '6': 'Santa Catarina',
        '7': 'Rio Grande do Sul',
        '8': 'São Paulo',
        '9': 'São Paulo'
    }
    
    digito_estado = cpf[8]
    
    if digito_estado in estados:
        return f'O CPF é de: {estados[digito_estado]}'
    else:
        return 'CPF INVÁLIDO'

def main():
    cpf = input("Digite o número do CPF (com ou sem pontuação): ")
    resultado = identificar_estado(cpf)
    print(resultado)

main()