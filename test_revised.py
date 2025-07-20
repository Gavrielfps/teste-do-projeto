data_base = {'name' : '', 'email' : '', 'password' : ''}

print("*"*50)
print("Bem-vindo ao sistema de cadastro do BlaBlaCar!")
while True:
    print("*"*50)
    print("Qual das opções abaixo você deseja?")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Buscar usuário")
    print("4 - Excluir usuário")
    print("5 - Atualizar usuário")
    print("0 - Sair")
    option = int(input(" "))
    
    if (option == 1):
        print("*"*50)
        print("Opção escolhida: 1")
        print("CADASTRAR USUÁRIO")
        print("*"*50)
        username_blablacar = input("Insira um nome de usuário:\n")
        email_blablacar = input("Insira um endereço de e-mail válido:\n")
        psw_blablacar = input("Insira uma senha:\n")
        data_base['name'] = username_blablacar
        data_base['email'] = email_blablacar
        data_base['password'] = psw_blablacar
        print("#"*50)
        print("Usuário cadastrado!")
        print(f'Nome: {data_base["name"]}\nE-mail: {data_base['email']}')
    
    elif (option == 2):
        print("*"*50)
        print("Opção escolhida: 2")
        print("LISTAR USUÁRIIOS")
        print("*"*50)
        print(f'Usuários:\n\t{data_base['name']}')
    
    elif (option == 3):
        print("*"*50)
        print("Opção escolhida: 3")
        print("BUSCAR USUÁRIO")
        print("*"*50)
        user_search = input("Insira o usuário para realizar a busca:\n\tVocê pode pesquisar por e-mail ou nome de usuário.\n")
        if (user_search in data_base['name'] or data_base["email"]):
            print(f'Usuário encontrado!\n\t{data_base["name"]}\n\t{data_base["email"]}')
        else:
            print("Usuário não encontrado!")
    
    elif(option == 4):
        print("*"*50)
        print("Opção escolhida: 4")
        print("EXCLUIR USUÁRIO")
        print("*"*50)
        user_search = input("Insira qual usuário deseja excluir:\n\tVocê pode pesquisar por e-mail ou nome de usuário.")
        if (user_search in data_base["name"] or data_base["email"]):
            print(f"Usuário encontrado!\n\t{data_base["name": user_search]}\n\t{data_base['email']}")
            decision = input("Deseja mesmo exluir?\nESTA AÇÃO É IRREVESSÍVEL!")
            if (decision == 'Sim' or "sim" or "S" or "S"):
                del data_base["name": user_search]
            else:
                print("Usuário não encontrado!")
                continue
    
    elif(option == 5):
        print("*"*50)
        print("Opção escolhida: 5")
        print("ATUALIZAR USUÁRIO")
        print("*"*50)
        user_search = input("Insira o usuário para realizar a busca:\n\tVocê pode pesquisar por e-mail ou nome de usuário.")
        if (user_search in data_base['name'] or data_base["email"]):
            print(f'Usuário encontrado!\n{data_base["name": user_search]}\n\t{data_base['email']}')
            username_blablacar = input("Insira um nome de usuário:\n")
            data_base["name"] = username_blablacar
            email_blablacar = input("Insira um endereço de e-mail válido:\n")
            data_base["email"]
            psw_blablacar = input("Insira uma senha:\n")
            data_base["password"] = psw_blablacar
            print("#"*50)
            print("NOVO USUÁRIO CADASTRADO!")
            print(f"\n\t{data_base['name']}\n\t{data_base['email']}")
        else:
            print("[ERRO DESCONHECIDO]")
    
    elif(option == 0):
        print("*"*50)
        print("Opção escolhida: 0")
        print("ATUALIZAR SAIR")
        print("*"*50)
        exit()