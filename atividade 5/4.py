def sistema_login():
    login_correto = "admin"
    senha_correta = "1234"
    
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")

    if login == login_correto and senha == senha_correta:
        print("Acesso Permitido")
    else:
        print("Acesso Negado")

sistema_login()