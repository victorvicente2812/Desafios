# Crie uma função que calcule o valor da gorjeta de um garçom, baseada na qualidade do serviço
# qualidade_servico: 'ruim', 'medio', 'bom', 'excelente'

# A função deve pedir o valor da conta e a qualidade do serviço
# Se a qualidade for ruim a gorjeta é 0
# Se a qualidade for media a gorjeta é %2.5 do valor da conta
#Se a qualidade for bom a gorjeta é %4 do valor da conta
#Se a qualidade for excelente a gorjeta é %5 do valor da conta

#Exemplo:
# valor_conta = 100
# qualidade_servico = 'excelente'
# o valor da gorjeta é de R$ 5,00

def calculagorjeta(qualidade_servico, total_conta):
    if qualidade_servico == 'ruim':
        gorjeta = 0
    elif qualidade_servico == 'media':
        gorjeta = total_conta  * 2.5
    elif qualidade_servico == 'boa':
        gorjeta = total_conta  * 4.0
    else:
        gorjeta = total_conta * 5.0

    return(f' O valor da conta foi de {total_conta}, o atendimento foi {qualidade_servico}, com isso a gorjeta é {gorjeta}')

print(calculagorjeta('ruim',100))
print(calculagorjeta('media',100))
print(calculagorjeta('boa',100))
print(calculagorjeta('excelente',100))
