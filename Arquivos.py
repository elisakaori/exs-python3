#!/usr/bin/env python
# coding: utf-8

# Exercício 1

# In[3]:


import os

def ip_valido(ip_string):
    partes = ip_string.split('.')
    if len(partes) != 4:
        return False
    for parte in partes:
        if not parte.isdigit():
            return False
        parte_integer = int(parte)
        if parte_integer < 0 or parte_integer > 255:
            return False
    return True

if os.path.exists("lista_IPs.txt"):
    ips = open("lista_IPs.txt", "r")
    lista_ips = ips.read().split("\n")
    
    validos = []
    invalidos = []
    
    for ip in lista_ips:
        if ip_valido(ip) == True:
            validos.append(ip)
        else:
            invalidos.append(ip)

    arquivo_relatorio = open("resposta.txt", "wt")
        
    if len(validos) > 0:
        arquivo_relatorio.write("[Endereços válidos:]\n")
        for valido in validos:
            arquivo_relatorio.write(valido+"\n")
        
    if len(invalidos) > 0:
        arquivo_relatorio.write("\n[Endereços inválidos:]\n")
        for invalido in invalidos:
            arquivo_relatorio.write(invalido+"\n")
        
    arquivo_relatorio.close()


# Exercício 2

# In[150]:


teste = open('relatorio.txt', 'w+')
d = {}
valores = []
soma = 0
i = 0
# abrindo arquivo e transformando em um dicionário
with open("usuario.txt") as f:
    for line in f:
        (key, val) = line.split()
        d[key] = round(int(val)/1048576, 2)
        soma = round(int(val)/1048576, 2) + soma
        i = i + 1
        
# espaço medio ocupado
media = round(soma/i, 2)
media

# transformando valores do dicionário em uma lista
valores = d.values()
valores = list(valores)

# porcentagem de uso
def porcentagem(valores):
    i = 0
    for i in range(len(valores)):
        valores[i]=round((valores[i]/soma)*100, 2)
    return valores


porcentagem(valores)
    
#
linha = '\n------------------------------------------------------------------------------'

print('ACME Inc.' + f"{'Uso do espaço em disco pelos usuários':>69}" + linha, file = teste)
print('Nr.\t' + 'Usuário' + '{:>33}'.format('Espaço utilizado') + '{:>30}'.format('% do uso')+ linha, file = teste)

i = 0
for key, val in d.items():
    print('{}\t'.format(i + 1) + key +":  \t"+'{:>20}'.format(str(val))+ ' MB  \t{:>20} %'.format(valores[i]),file = teste)
    i = i + 1

print('\nEspaço total ocupado: {:>10} MB'.format(soma) + '\n' + 'Espaço médio ocupado: {:>10} MB'.format(media), file = teste)

