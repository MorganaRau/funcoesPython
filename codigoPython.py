1)

while True: #loop enquanto permanecer a condição
 x1 = int(input('--Deseja inserir dados?1-sim 0-não:--'))
 if(x1 == 0): # se digitar 0 o loop é encerrado
  print ('até mais')
  break
 if (x1 == 1): #verifica em qual conceito a nota se encaixa
    nome = input('qual seu nome')
    nota = float(input(' qual a sua nota'))
 if (nota <=2.9):
    print('O aluno', nome, 'tirou nota', nota, 'e se enquadra no conceito E')


 if (nota >=3) and (nota <=4.9):
    print('O aluno', nome, 'tirou nota', nota, 'e se enquadra no conceito D')

 if (nota >=5) and (nota <=6.9):
    print('O aluno', nome, 'tirou nota', nota, 'e se enquadra no conceito C')


 if (nota >=7) and (nota <=8.9):
    print('O aluno', nome, 'tirou nota', nota, 'e se enquadra no conceito B')


 if (nota >=9) and (nota <=10):
    print('O aluno', nome, 'tirou nota', nota, 'e se enquadra no conceito A')

2)

nome= input("informe o seu nome:") 
sobNome= input("informe seu sobrenome:")
email="@algoritmos.com"
lista=[]
lista[:] = nome #o nome é separado em char
character = lista[0] #a primeira letra de nome

print(nome, sobNome, "seu email é:", end = "")# cria uma frase só
print(character, sobNome, email, sep = '')# sep une todos strings

3)
import random
lista=[]
listaSorteio=[]
while True: #enquanto a condição for verdadeira

  decisao = int(input("--inserir valores?1-sim 0-nao:--"))

  if (decisao == 0):

    print(lista)
    sorteado = (random.choice(lista))#um nome da lista é sorteado
    print("o sorteado foi:", sorteado)

    break
  if (decisao == 1):
      nome = input("insira o nome:")

      valor = int(input("insira o valor doado:"))


      vezes : int = valor/10 #valor da doação é transformado em um #número para o sorteio

      v = int(vezes) 
      nomes=[nome] * v # esse número vai multiplicar quantas vezes #o nome da pessoa aparece na lista


      lista.append(nomes) #os nomes vão para uma lista




4)

from operator import itemgetter
dicio : dict = {}
lista = []
count = 0
dicioCopy : dict = {}
while True:
   decisao = int(input("--inserir valores?1-sim 0-nao:--"))


   if (decisao == 0):
     print("--Codigo Encerrado--")
     print("Lista Original:", lista)
     print("Lista Ordenada:", novaLista)
     break
   if (decisao == 1):

    c = input("codigo:") #valores a serem inseridos no dicionário
    e = input("estoque:")
    m = input("minimo:")


    dicio = { 
    'codigo:': c, #índice e valores
    'estoque:': e,
    'minimo:': m
       }

    dicioCopy = dicio.copy()#cópia do dicionário
    lista.append(dicioCopy) #lista igual ao dicionário 
    novaLista = sorted(lista, key=itemgetter('codigo:')) 
    # itens da lista são organizados por ordem de ‘código’


