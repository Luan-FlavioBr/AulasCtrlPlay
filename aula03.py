# convidados = ["André", "Kalleo", "Laura", "Luan"]
# print(convidados)

# # Inverte a ordem da lista (Não leva em consideração
# # ordem crescente ou decrescente)
# convidados.reverse()
# print(convidados)


# # Mudando o elemento do index 1 para "Mario"
# convidados[1] = "Mario"
# print(convidados)

# # Adicionando convidado ao fim da lista
# convidados.append("Sonic")
# print(convidados)

# # Adicionando "Hulk" no index 1 da lista
# convidados.insert(1, "Hulk")
# print(convidados)

# # Deletando Elementos da lista! del
# del convidados[1]
# print(convidados)


# # Deletando o último elemento da lista! .pop()
# convidadoDeletado = convidados.pop()

# # Printando o convidado que foi deletado!
# print("O convidado deletado foi: "+convidadoDeletado)

# # Printando a lista
# print(convidados)

# #------------------------------------------------- 
# convidadoViajando = "Luan"

# # Removendo elemento por meio do valor!
# convidados.remove(convidadoViajando)
# print(convidados)

# numeros = []

# numeros.append(int(input("Digite um número: ")))
# numeros.append(int(input("Digite um número: ")))
# numeros.append(int(input("Digite um número: ")))
# print(numeros)

# # # Em ordem crescente
# # numeros.sort()
# # print(numeros)

# # # Em ordem decrescente
# # numeros.sort(reverse=True)
# # print(numeros)


# # Sorted NÃO muda a lista principal!
# # Em ordem crescente
# print(sorted(numeros))

# # Em ordem decrescente
# print(sorted(numeros, reverse=True))

# print(numeros)

teste = [
    ["Andre", "José", "Kalleo", "Laura"],
    ["Palmeiras", "Corinthians", "São Paulo", "Ituano"]
]

# Exibindo o index 0 da lista teste
print(teste[1])

# Exibindo o index 3 da lista no index 0 da lista teste
print(teste[1][0])



