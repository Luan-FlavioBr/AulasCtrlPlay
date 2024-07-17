import os

def adicionar_produto():
    cod_produto = input("Digite o código do novo produto: ")
    nome_produto = input("Digite o nome do novo produto: ")
    valor_produto = float(input("Digite o valor do produto R$ "))
    
    if os.path.exists("produtos.txt"):
        with open("produtos.txt", "a") as a:
            a.write(f"{cod_produto},{nome_produto},{valor_produto}\n")
    else:
        with open("produtos.txt", "w") as a:
            a.write(f"{cod_produto},{nome_produto},{valor_produto}\n")
        

def listar_produtos():
    with open("produtos.txt", "r") as a:
        print(f"{"Código":^10}{"Produto":^30}{"Valor":>10}")
        for linha in a:
            linha = linha.replace("\n", "").split(",")
            valor = float(linha[2])
            print(f"{linha[0]:<10} {linha[1]:^30} R$ {valor:.2f}")

def apagar_produto():
    listar_produtos()
    print("-"*50)
    cod_produto = input("Digite o código do produto que você gostaria de apagar: ")

    # Criando a lista temporária!
    lista_temporaria = list()

    # Adiciona todos os dados em uma nova lista
    with open("produtos.txt", "r") as a:
        for linha in a:
            linha = linha.replace("\n", "")
            linha = linha.split(",")
            lista_temporaria.append(linha)
    
    # Procura pela lista o código informado
    for i, produto in enumerate(lista_temporaria):
        if produto[0] == cod_produto:
            lista_temporaria.pop(i)

    # Reescreve todo o arquivo com a nova lista
    with open("produtos.txt", "w") as a:
        for linha in lista_temporaria:
            a.write(f"{linha[0]},{linha[1]},{linha[2]}\n")


def alterar_produtos():
    listar_produtos()
    print("-"*50)
    cod_produto = input("Digite o código do produto que você gostaria de alterar: ")
    lista_temporaria = list()

    # Adiciona todos os dados em uma nova lista
    with open("produtos.txt", "r") as a:
        for linha in a:
            linha = linha.replace("\n", "")
            linha = linha.split(",")
            lista_temporaria.append(linha)
    
    # Procura pela lista o código informado
    for i, produto in enumerate(lista_temporaria):

        # Se achar o código, altera as informações
        if produto[0] == cod_produto:
            nome_produto_novo = input("Digite o novo nome do produto: ")
            valor_produto_novo = input("Digite o novo valor do produto: R$")
            produto[1] = nome_produto_novo
            produto[2] = valor_produto_novo

    # Reescreve todo o arquivo com a nova lista
    with open("produtos.txt", "w") as a:
        for linha in lista_temporaria:
            a.write(f"{linha[0]},{linha[1]},{linha[2]}\n")

while True:
    print(f"{' Mercadinho do Zé ':-^50}\n")
    print(f" 1 - Adicionar produto\n"
          f" 2 - Lista de produtos\n"
          f" 3 - Alterar produto\n"
          f" 4 - Apagar produto\n"
          f" 5 - Sair\n")
    resposta = input("Selecione a opção desejada: ")

    if resposta == "1":
        adicionar_produto()
        os.system("cls")
    elif resposta == "2":
        os.system("cls")
        listar_produtos()
    elif resposta == "3":
        os.system("cls")
        alterar_produtos()
    elif resposta == "4":
        apagar_produto()
        os.system("cls")
    elif resposta == "5":
        break
