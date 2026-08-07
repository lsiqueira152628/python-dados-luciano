#variaveis e classes 
#classe = int, float, str, bool 
#int = armazena numeros inteiros. Ex.: 3, 100 ou -5
#float = armazena numeros com ponto flutuante. Ex.: 3.14, 100.0 ou -0.5
#str = armazena strings, ou seja, textos ou sequencias de caracteres. Ex.: "Olá!", ou '1234'
#bool = Armazena valores lógicos Ex.: True ou False

nome = 'Luciano'
sobrenome = 'Siqueira'
idade = 48
masculino = True
salario_atual = 15.500

#type()
type(nome)
type(idade)
type(masculino)
type(salario_atual)

print('Me chamo', nome, sobrenome, ', tenho', idade, 'anos de idade', 'e o meu salario atual é', salario_atual )

#Exercio int e float 
q_seguranca = 5 
s_seguranca = 3000

q_docente = 16
s_docente = 6000

q_diretoria = 1
s_diretoria = 12500

total_empregados = q_seguranca + q_docente + q_diretoria
total_empregados

diferenca_salario = s_diretoria - s_seguranca
diferenca_salario

media = (q_seguranca*s_seguranca + q_docente*s_docente + q_diretoria*s_diretoria) / (total_empregados)
media

#Exponenciação (**)
2*2*2
2**3

operador = 2
potencia = 3 
operador ** potencia 

#Módulo (%)
7%3

dividendo = 7
divisor = 3
dividendo % divisor

#Divisão inteira (//)
7//3

numerador = 7
denominador = 3 
numerador // denominador

#strings 
s1 = 'Luciano'
s2 = "Luciano"
print(type(s1), type(s2))

#manipular string 

texto = '    Geovana Alessandra dias Sanyos  '
print (texto)

texto.upper()#retorna conteudo em maiusculo
texto.lower()#retorna conteudo em minusculo

texto.strip()#remove os espaços em branco do inicio e do fim da string

texto.replace('y','t')#substituir caracter antigo por novo


texto = texto.strip().replace('y','t').upper()
texto

#tabela unicode 
chr(64)# '@'
chr(79)+chr(108)+chr(225)#'Olá'

#coletando dados 
nome = input('Escreva seu nome: ')
nome

ano_entrada = input('Escreva o ano que iniciou seus estudos em python: ')
type(ano_entrada)

ano_entrada = int(input('Escreva o ano que iniciou seus estudos em python: '))
type(ano_entrada)

novo_salario = float(input('Digite qual a sua pretensão salarial: '))
print(f'Ano de entrada {ano_entrada} - Pretensão salarial {novo_salario}')

print(f"Me chamo {nome} , tenho {idade} anos de idade e meu salario atual é {salario_atual}")

#palavra chave
#string %s
#inteiro %d
#float %f
#caractere %c

print('Me chamo %s, tenho %d anos e meu salario atual é %.3f.' %(nome, idade, salario_atual))

#caracteres especiais 

#\n é usado para pular uma linha no texto 
print("Estudar é um esforço constante, \nÉ como cultivar uma planta, \nPrecisamos de dedicação e paciência, \nPara ver o fruto amadurecer")

#\t usado para adicionar um espaço de tabulação no texto
print('Quantidade\tQualidade\n5 amostras\tAlta\n3 amostras\tBaixa')

#\\usado para imprimir uma unica barra invertida 
print("Caminho do arquivo: C:\\arquivos\\documento.csv")

#\" é usado para imprimir aspas duplas quando estamos trabalhando com uma string criada a partir de aspas duplas ". Porém, isso não é necessário caso seja uma string criada por aspas simples '
print("Ouvi uma vez \"Os frutos do conhecimento são os mais doces e duradouros de todos.\"")