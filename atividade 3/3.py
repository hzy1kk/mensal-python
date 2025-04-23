def dolares_para_float(d):
    return float(d.replace('$', '').replace(',', '.'))

def percentual_para_float(p):
    return float(p.replace('%', '').replace(',', '.')) / 100

dolares = dolares_para_float(input("Quanto custou a refeição? "))
percentual = percentual_para_float(input("Qual percentual você gostaria de deixar de gorjeta? "))

gorjeta = dolares * percentual

print(f"Deixe ${gorjeta:.2f}")
