# Na mesma linha dos exercicios anteriores crie uma função chamada pode_ver_filme que recebe a idade e a classificação indicativa do filme
# classificacao: 'L' (Livre), 'Maior de 12', 'Maior de 14', 'Maior 16', 'Maior 18'

#Exemplo:
# idade = 10
# classificacao = 'Maior de 12'
# resposta = "Não pode assitir o filme"

def pode_ver_filmes(idade, classificacao):
    if classificacao == "L":
        return "Pode assistir o filme"
    elif idade >= classificacao:
        return "Pode assistir o filme"
    else:
        return "Não pode assistir o filme"

idade = int(input("Digite sua idade: "))
classificacao = int(input("Digite a classificação: "))

print(pode_ver_filmes(idade, classificacao))