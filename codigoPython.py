1)

while True: #loop enquanto permanecer a condi��o
 x1 = int(input('--Deseja inserir dados?1-sim 0-n�o:--'))
 if(x1 == 0): # se digitar 0 o loop � encerrado
  print ('at� mais')
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
lista[:] = nome #o nome � separado em char
character = lista[0] #a primeira letra de nome

print(nome, sobNome, "seu email �:", end = "")# cria uma frase s�
print(character, sobNome, email, sep = '')# sep une todos strings

3)
import random
lista=[]
listaSorteio=[]
while True: #enquanto a condi��o for verdadeira

  decisao = int(input("--inserir valores?1-sim 0-nao:--"))

  if (decisao == 0):

    print(lista)
    sorteado = (random.choice(lista))#um nome da lista � sorteado
    print("o sorteado foi:", sorteado)

    break
  if (decisao == 1):
      nome = input("insira o nome:")

      valor = int(input("insira o valor doado:"))


      vezes : int = valor/10 #valor da doa��o � transformado em um #n�mero para o sorteio

      v = int(vezes) 
      nomes=[nome] * v # esse n�mero vai multiplicar quantas vezes #o nome da pessoa aparece na lista


      lista.append(nomes) #os nomes v�o para uma lista




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

    c = input("codigo:") #valores a serem inseridos no dicion�rio
    e = input("estoque:")
    m = input("minimo:")


    dicio = { 
    'codigo:': c, #�ndice e valores
    'estoque:': e,
    'minimo:': m
       }

    dicioCopy = dicio.copy()#c�pia do dicion�rio
    lista.append(dicioCopy) #lista igual ao dicion�rio 
    novaLista = sorted(lista, key=itemgetter('codigo:')) 
    # itens da lista s�o organizados por ordem de �c�digo�


