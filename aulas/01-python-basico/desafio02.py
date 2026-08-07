#Questão 1
nome = input('Digite o seu nome: ')
print(f'Olá, {nome}.')

#Questão 2
nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
print(f'Olá {nome}, você tem {idade} anos.')

#Questão 3 
nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
altura = float(input('Digite sua altura: '))
print(f'Olá {nome}, você tem {idade} anos e mede {altura} metros!')

#Questão 4 
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
print(a+b)

#Questão 5 
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
print(a+b+c)

#Questão 6 
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
print(a-b)

#Questão 7
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
print(a*b)

#Questão 8
numerador = int(input('Digite o numerador: '))
denominador = int(input('Digite o denominador (OBS: o valor não pode ser nulo): '))
print(numerador/denominador)

#Questão 9
operador = int(input('Digite o operador valor: '))
potencia = int(input('Digite a potência valor: '))
print(operador**potencia)

#Questão 10
numerador = int(input('Digite o numerador: '))
denominador = int(input('Digite o denominador (OBS: o valor não pode ser nulo): '))
print(numerador//denominador)

#Questão 11
numerador = int(input('Digite o numerador: '))
denominador = int(input('Digite o denominador (OBS: o valor não pode ser nulo): '))
print(numerador%denominador)

#Questão 12
nota_1 = float(input('Digite a 1° nota: '))
nota_2 = float(input('Digite a 2° nota: '))
nota_3 = float(input('Digite a 3° nota: '))
print(f'Média {(nota_1+nota_2+nota_3)/3}.')

#Questão 13
frase = 'Olá Python!'
print(frase)

#Questão 14
frase = input('Digite uma frase: ')
print(frase)

#Questão 15
frase = input('Digite uma frase: ')
print(frase.upper())

#Questão 16
frase = input('Digite uma frase: ')
print(frase.lower())

#Questão 17
frase = ' Olá Python!  '
print(frase.strip())

#Questão 18
frase = input('Digite uma frase: ')
print(frase.strip())

#Questão 19
frase = input('Digite uma frase: ')
print(frase.strip().lower())

#Questão 20
frase = input('Digite uma frase: ')
print(frase.lower().replace('e','f'))

#Questão 21 
frase = input('Digite uma frase: ')
print(frase.lower().replace('a',chr(64)))

#Questão 22
frase = input('Digite uma frase: ')
print(frase.lower().replace('s',chr(36)))