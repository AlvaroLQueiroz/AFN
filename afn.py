# -*- coding: utf-8 -*-
from os import system
from os import name

#Limpa o terminal de acordo com o S.O.
def clear():
	system(['clear','cls'][name == 'nt'])

class AFN:
	states = None #Estados do autômato.
	alphabet = None #Alfabeto aceito pelo autômato.
	matrix = {} #Matriz de transição.
	initial = None #Estado inicial.
	acceptance = None #Conjunto de estados de aceitação.
	word = None #Palavra de entrada.

	#Reseta o autômato.
	def reset(self):
		self.states = None
		self.alphabet = None
		self.matrix = {}
		self.initial = None
		self.acceptance = None
		self.word = None

	#Le o autômato.
	def read(self):
		clear()
		print "Os elementos devem ser separados por virgula(,)\ne as linhas da matriz devem ser separadas por ponto e virgula(;).\n\
Ex.: Informe os estados: A, B, C\n\
     Informe o alfabeto: 0, 1\n\
     Informe a matriz de transição: C, B; A, A; A, C\n"

     	#Le os estados como uma string e os separa em uma lista.
		self.states = str(raw_input("Informe os estados: "))
		self.states = self.states.replace(' ', '').split(',')

		#Le o alfabeto como uma string e o separara em uma lista.
		self.alphabet = str(raw_input("Informe o alfabeto: "))
		self.alphabet = self.alphabet.replace(' ', '').split(',')

		#Le a matriz de transição como uma string e separa as linhas em uma lista.
		auxiliary  = str(raw_input("informe a matriz de transiçao: "))
		auxiliary  = auxiliary .replace(' ', '').split(';')
		
		#Verifica se a matriz esta completa.
		if len(auxiliary) != len(self.states):
			print "Matriz invalida."
		
		#Separa as colunas, linha por linha.
		for counter in range(len(auxiliary)):
			auxiliary[counter] = auxiliary[counter].split(',')	

		#Cria uma matriz de dicionario com a matriz de transição.
		#Ex.: matrix = {'A':{'0':{'A'}, '1':{'A'}},
		#			   {'B':{'0':{'B'}, '1':{'A'}}}
		for line in range(len(self.states)):
			self.matrix[self.states[line]] = {}
			for column in range(len(self.alphabet)):
				self.matrix[self.states[line]][self.alphabet[column]] = auxiliary[line][column]

		#Le o estado inicial.
		self.initial = str(raw_input("Infome o estado inicial: "))
		
		#Le o conjunto de estados de aceitção como uma string e os sepera em uma lista.
		self.acceptance = str(raw_input("Infome o(s) estado(s) de aceitação: "))
		self.acceptance = self.acceptance.replace(' ', '').split(',')

	#Le uma palavra de entrada.
	def readWord(self):
		self.word = str(raw_input("Informe a palavra: "))
		self.word = self.word.replace(' ', '').split(',')

	#Executa o autômato.
	def execute(self):
		final = self.initial 
		counter = 0 #Contador de transições.
		print "Estado inicial: ", final
		
		#Percorre o alfabeto da entrada.
		for letter in self.word:
			try:
				counter += 1
				final = self.matrix[final][letter]
				print "Transição ", counter, "foi para o estado", final, "."
			except:
				print "A palavra contem caracteres que nao estão no alfabeto."
				return 
		#A entrada é considerada invalida até que verificação seja feita.
		result = "A palavra nao foi aceita."

		#Percorre o conjunto de estados de aceitação verificando se o estado final esta no conjunto de aceitação.
		for i in self.acceptance:
			if i == final:
				result = "A palavra foi aceita."
		
		print result

	#Exibe as informações do autômato.
	def display(self):
		clear()
		print "Estados: ", self.states
		print "Alfabeto: ", self.alphabet
		print "Estado inicial: ", self.initial
		print "Estado(s) de aceitação: ", self.acceptance
		print "Matriz: "

		for i in self.states:
			for j in self.alphabet:
				print self.matrix[i][j], 
			print''


machine = AFN() #Cria um objeto AFN.
machine.read() #Faz a primeira leitura do autômato.

done = False #Controla o fim do programa.
stop = False #controla o fim de uma execução do autômato.

#Loop principal.
while not done:
	#Loop de entradas no autômato.
	while not stop:
		machine.display()
		machine.readWord()
		machine.execute()
		stop = False
		stop = str(raw_input("Deseja entrar com outra palavra? (Y/n): "))
		if(stop == ''):
			stop = False
		elif(stop.lower() == 'y'):
			stop = False
		else:
			stop = True

	#Verifica se o usuario deseja entrar com outra maquina.
	if stop:
		option = str(raw_input("Deseja entrar com outra maquina? (Y/n): "))

		if(option == ''):
			done = False
			machine.reset()
			machine.read()
		elif(option.lower() == 'y'):
			stop = False
			machine.reset()
			machine.read()
		else:
			stop = True
			done = True
