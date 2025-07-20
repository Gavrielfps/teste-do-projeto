usuarios = list()

while True:
    print("*" * 50)
    print("Bem Vindo ao Sistem!")
    print("*" * 50)

    opcao = input("Escolha uma das opções\n\n" \
    "1 - Cadastrar Usuário\n" \
    "2 - Listar usuários\n" \
    "3 - Buscar usuário por email\n" \
    "4 - Remover usuário por email\n" \
    "5 - Atualizar email\n" \
    "0 - Sair\n\nOpção: ")

    if(opcao == '0'):
        break

    if(opcao == '1'):
        nome = input("Digite seu nome: ")
        email = input("Digite o seu email: ")
        senha = input("Digite a sua senha: ")
        usuarios.append([nome, email, senha])
        print("Usúario cadastrado com sucesso!")
    
    if(opcao == '2'):
        print("\nLista de usuários\n")
        for usu in usuarios:
            print(f"Nome {usu[0]}")
            print(f"Email {usu[1]}")
            print("-" * 50)

        print("\n")

    if(opcao == '3'):
        emailbusca = input("Digite um email para efetuar a busca: ")
        encontrado = False
        for usu in usuarios:
            if(emailbusca == usu[1]):
                encontrado = True
                print("Encontrado o usuário\n\n")
                print(f"Nome: {usu[0]}")
                print(f"Email: {usu[1]}")
                print("-" * 50)
        if(not encontrado):
            print("Usuário não existe!\n\n")

    if(opcao == '4'):
        emailbusca = input("Digite um email para efetuar a remoção: ")
        indice = -1
        for ind in range(len(usuarios)):
            if(emailbusca == usuarios[ind][1]):
                indice = ind
        
        if(indice == -1):
            print("Não encontrou o usuário!")
        else:
            usuarios.pop(indice)
    
    if(opcao == '5'):
        emailbusca = input("Digite um email para efetuar a atualização: ")
        indice = -1
        for ind in range(len(usuarios)):
            if(emailbusca == usuarios[ind][1]):
                indice = ind
        
        if(indice == -1):
            print("Não encontrou o usuário!")
        else:
             nomeNovo = input("Digite seu nome novo: ")
             senhaNova = input("Digite a sua nova senha: ")

             usuarios[indice][0] = nomeNovo
             usuarios[indice][2] = senhaNova    
