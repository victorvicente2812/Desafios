#crie uma função chamada cumprimentar ela deve receber o nome e a hora, essa função deve gerar cumprimentos baseados no periodo d
#Periodo : Manhã 5 até 12, Tarde: 13 até 18, Noite: 18 até 24

#Exemplo:
#Nome: Allana
#Hora : 9
#Bom dia, Allana

# Exemplo2:
#Nome: Gustavo B
#Hora : 15
#Boa tarde, Gustavo B
def cumprimentar(nome,hora):
    if hora >=5 and hora <=12:
        return(f'Bom Dia, {nome}')
    elif hora >=13 and hora <=18:
        return(f'Boa Tarde, {nome}')
    else:
        return(f'Boa Noite, {nome}')

print(cumprimentar('Kelvin', 8))
print(cumprimentar('Kelvin', 13))
print(cumprimentar('Kelvin', 18))