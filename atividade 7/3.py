def lista_convidados():
    convidados = []
    num_convidados = int(input("Quantos convidados deseja adicionar? "))
    
    for i in range(num_convidados):
        nome = input(f"Digite o nome do convidado {i+1}: ")
        convidados.append(nome)
    
    lista_final = sorted(set(convidados))
    
    print("\nLista final de convidados (sem duplicatas e ordenada):")
    print(lista_final)

lista_convidados()