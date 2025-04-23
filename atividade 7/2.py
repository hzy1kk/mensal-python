def notas_carnaval():
    notas = []
    for i in range(5):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
    
    notas_ordenadas = sorted(notas)
    notas_validas = notas_ordenadas[1:-1]
    media = sum(notas_validas) / len(notas_validas)
    
    print(f"\nMédia das notas (descontando a maior e a menor): {media}")

notas_carnaval()