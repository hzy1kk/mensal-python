def comentar_idade(idade):
    try:
        idade = int(idade)

        if idade < 0:
            return "Valor informado é inválido"
        elif idade < 18:
            return "Você é menor de idade."
        elif 18 <= idade <= 59:
            return "Você é adulto."
        else:
            return "Você é idoso."

    except ValueError:
        return "Valor informado é inválido"