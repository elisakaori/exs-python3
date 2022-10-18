#!/usr/bin/env python
# coding: utf-8

# ### Estrutura de Decisão

# 1. Faça um Programa que peça dois números e imprima o maior deles.

# In[5]:


n1 = float(input('digite o primeiro número: '))
n2 = float(input('digite o segundo número: '))

if n1 > n2:
    print(n1)
elif n1 < n2:
    print(n2)
    


# 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

# In[6]:


num = float(input('digite um vallor: '))

if num < 0:
    print(num, 'é negativo')
elif num > 0:
    print(num, 'é positivo')


# 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
# 

# In[7]:


letra = input('digite F para Feminino ou M para Masculino: ')

if letra == 'F':
    print('F - Feminino')
elif letra == 'M':
    print('M - Masculino')
else:
    print('Sexo Inválido')


# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
# 

# In[9]:


letra = input('digite uma letra: ')
vogais = ['a', 'e', 'i', 'o', 'u']

if letra in vogais:
    print('você digitou uma vogal')
else:
    print('você digitou uma consoante')


# 5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar: <br> <br>
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;<br>
# A mensagem "Reprovado", se a média for menor do que sete;<br>
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
# 

# In[13]:


nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
media = (nota1 + nota2)/2

if media == 10:
    print('Aprovado com Distinção')
elif media >= 7:
    print('Aprovado')
else:
    print('Reprovado')
    


# 6. Faça um Programa que leia três números e mostre o maior deles.

# In[21]:


n1 = float(input('digite o primeiro número: '))
n2 = float(input('digite o segundo número: '))
n3 = float(input('digite o terceiro número: '))

if n1 > (n2 and n3):
    print('o número', n1, 'é o maior')
elif n2 > (n1 and n3):
    print('o número', n2, 'é o maior')
elif n3 > (n1 and n2):
    print('o número', n3, 'é o maior')


# 7. Faça um Programa que leia três números e mostre o maior e o menor deles.
# 

# In[23]:


n1 = float(input('digite o primeiro número: '))
n2 = float(input('digite o segundo número: '))
n3 = float(input('digite o terceiro número: '))

maior = 0
menor = 0

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3 
    
print('o maior número é {} e o menor número é {}'.format(maior, menor))


# 8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
# 

# In[28]:


prod1 = float(input('qual o valor do primeiro produto? '))
prod2 = float(input('qual o valor do segundo produto? '))
prod3 = float(input('qual o valor do terceiro produto? '))

if prod1 < (prod2 and prod3):
    print('você deve comprar o primeiro produto')
elif prod2 < (prod1 and prod3):
    print('você deve comprar o segundo produto')
elif prod3 < (prod1 and prod2):
    print('você deve comprar o terceiro produto')


# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
# 

# In[29]:


lista = []

for i in range(3):
    lista.append(float(input('digite o {}o número '.format(i+1))))
    
lista.sort(reverse = True)
print(lista)


# 10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
# 

# In[31]:


letra = input('digite M para Matutino, V para Vespertino ou N para Noturno: ')

if letra == 'M':
    print('Bom Dia!')
elif letra == 'V':
    print('Boa Tarde!')
elif letra == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido!')


# 11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# 
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% 
# 
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

# In[34]:


salario = float(input('digite o seu salário: '))

if salario <= 280:
    percentual = 20
    aumento = salario * percentual/100
    novo_sal = salario + aumento
elif 280 < salario <= 700:
    percentual = 15
    aumento = salario * percentual/100
    novo_sal = salario + aumento
elif 700 < salario <= 1500:
    percentual = 10
    aumento = salario * percentual/100
    novo_sal = salario + aumento
else:
    percentual = 5
    aumento = salario * percentual/100
    novo_sal = salario + aumento
    
print('o salário antes do reajuste: {} \npercentual de aumento aplicado: {} \nvalor do aumento: {} \nnovo salário: {}'.format(salario, percentual, aumento, novo_sal))


# In[ ]:


12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 
11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao 
Salário Bruto menos os descontos. 

O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
    
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 

Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00


# In[52]:


valor_hora = float(input('digite o valor da sua hora: '))
qtd_horas = float(input('digite a quantidade de horas trabalhadas no mês: '))

salario_bruto = valor_hora * qtd_horas
fgts = salario_bruto * 0.11
inss = salario_bruto * 0.10
sindicato = salario_bruto * 0.03

if salario_bruto  <= 900:
    imposto_renda = 0
elif 900 < salario_bruto <= 1500:
    imposto_renda = 0.05 * salario_bruto 
elif 1500 < salario_bruto <= 2500:
    imposto_renda = 0.10 * salario_bruto 
else:
    imposto_renda = 0.20 * salario_bruto 

total_desc = imposto_renda + inss

print('Salário Bruto: R${:.2f}'.format(salario_bruto))
print('(-) IR (5%): {:.2f}'.format(imposto_renda))
print('(-) INSS: ( 10%){:.2f}'.format(inss))
print('FGTS (11%): R${:.2f}'.format(fgts))
print('Total de descontos: R${:.2f}'.format(total_desc))
print('Salário Liquido: R${:.2f}'.format(salario_bruto - total_desc))


# 13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
# 

# In[55]:


numero = int(input('digite um número de 1 a 7 para escolher um dia da semana: '))

if numero == 1:
    print('1-Domingo')
elif numero == 2:
    print('2-Segunda')
elif numero == 3:
    print('3-Terça')
elif numero == 4:
    print('4-Quarta')
elif numero == 5:
    print('5-Quinta')
elif numero == 6:
    print('6-Sexta')
elif numero == 7:
    print('7-Sabádo')
else:
    print('Valor inválido')


# In[ ]:


14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, 
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o 
conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.


# In[56]:


n1 = float(input("digite nota 1: "))
n2 = float(input("digite nota 2: "))
media = (n1 + n2)/2

if media >=9:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
elif media >= 0:
    conceito = "E"

if conceito in ("A","B","C"):
    resultado = "APROVADO!"
elif conceito in ("D", "E"):
    resultado = "REPROVADO"
    
print("nota 1: {}\nnota 2: {}".format(n1, n2))
print("média: ", media)
print("conceito: ", conceito)
print("resultado: ", resultado)


# 15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um 
# triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. <br><br>
# Dicas:<br>
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;<br>
# Triângulo Equilátero: três lados iguais;<br>
# Triângulo Isósceles: quaisquer dois lados iguais;<br>
# Triângulo Escaleno: três lados diferentes;

# In[58]:


l1 = int(input('digite o lado 1: '))
l2 = int(input('digite o lado 2: '))
l3 = int(input('digite o lado 3: '))

if l1 > (l2 + l3) or l2 > (l1 + l3) or l3 > (l1 + l2):
    print('não pode ser um triângulo')
elif l1 == l2 == l3:
    print('equilátero')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('isósceles')
else:
    print('escaleno')


# 22. Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

# In[3]:


num = float(input('digite um número: '))

if num % 2 == 0:
    print('o número {} é par!'.format(num))
else:
    print('o número {} é ímpar!'.format(num))


# 23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
# 

# In[3]:


num = float(input('digite um número: '))

num2 = round(num)

if num == num2:
    print('o número escolhido é inteiro')
else:
    print('o número escolhido é decimal')


# 24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. <br>
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:<br><br>
# par ou ímpar;<br>
# positivo ou negativo;<br>
# inteiro ou decimal.

# In[10]:


num1 = float(input("digite o número 1: "))
num2 = float(input("digite o número 2: "))
operacao = input("digite a operação: [+, -, /, *]: ")


def checar():
    if (resultado // 1 == resultado):
        print("inteiro")
        if resultado % 2 == 0:
            print("par")
            if resultado > 0:
                print("positivo")
            else:
                print("negativo")
        else:
            print("ímpar")
    else:
        print("decimal")


if operacao == '+':
    resultado = num1 + num2
    print("resultado: ", resultado)
    checar()
elif operacao == '-':
    resultado = num1 - num2
    print("resultado: ", resultado)
    checar()
elif operacao == '/':
    resultado = num1 / num2
    print("resultado: ", resultado)
    checar()
elif operacao == '*':
    resultado = numero1 * numero2
    print("resultado: ", resultado)
    checar()
else:
    print("Valor Invalido")

