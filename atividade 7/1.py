def notas_equipe():
    notas = []
    for i in range(5):
        nota = float(input(f"Digite a nota do aluno {i+1}: "))
        notas.append(nota)
    
    maior = max(notas)
    menor = min(notas)
    media = sum(notas) / len(notas)
    
    print(f"\nMaior nota: {maior}")
    print(f"Menor nota: {menor}")
    print(f"Média das notas: {media}")

notas_equipe()