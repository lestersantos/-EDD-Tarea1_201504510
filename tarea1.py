"""
Estrucutras de Datos 2do semestre 2019
Tarea1
Lester Efrain Ajucum Santos
201504510
"""
class Node:

	def __init__(self,data):
		self.next = None
		self.data = data

class List:
	def __init__(self):
		self.first = None
		self.last = None

	#Add at head of the list
	def add(self,data):
		newNode = Node(data)
		if self.first == None:
			#empty list
			self.first = newNode
		else:
			newNode.next = self.first
			self.first = newNode



	def show(self):
		aux = self.first
		while aux != None:
			print (aux.data,end = '')
			aux = aux.next
			if aux != None:
				print ("-->",end = '')
			else:
				print ()


	def isEmpty(self):

		temp = self.first
		if temp == None:
			empty = True
		else:
			empty = False
		return empty



	def search(self,data):
		if self.isEmpty():
			print ("La Lista esta vacia")
		else:
			temp = self.first
			while temp != None:
				if temp.data == data:
					return temp
					break
				else:
					temp = temp.next
			return temp


	def deleteHead(self,):
		if self.isEmpty():
			print ("La Lista esta vacia")
		else:
			self.first = self.first.next


	def update(self,currentData,newData):
		if self.isEmpty():
			print ("La lista esta vacia")
		else:
			myNode = self.search(currentData)
			if myNode == None:
				print ("No se Encontro Dato, Error al modificar")
			else:
				myNode.data = newData
				print ("Dato Modificado Correctamente")

myList = List()

strInput = 0

while strInput != '6':
	print ()
	print ("-------------------------------------")
	print ("USAC")
	print ("FACULTAD DE INGENIERIA")
	print ("LESTER EFRAIN AJUCUM SANTOS")
	print ("201504510")
	print ("EDD 2DO SEMESTRE")
	print ()
	print ("----------- Main Menu -----------")
	print ("1.Insertar Dato")
	print ("2.Mostrar Lista")
	print ("3.Buscar Dato")
	print ("4.Eliminar (Primer Elemento)")
	print ("5.Modificar Dato")
	print ("6.Salir")
	print ()
	strInput = input("Option:")

	if strInput == '1':
		print ("Dato a ingresar")
		dataInput = input("dato:")
		myList.add(dataInput)
		print ("Dato Agregado A la Lista Correctamente!")
	elif strInput == '2':
		myList.show()
	elif strInput == '3':
		print ("Dato a Buscar")
		dataInput = input("dato:")
		foundIt = myList.search(dataInput)
		if foundIt == None:
			print ("Dato No Encontrado")
		else:
			print ("Se encontro: ",end = '')
			print (foundIt.data)
	elif strInput == '4':
		myList.deleteHead()
		print ("Se Elimino El primer Elemento de la lista!")
	elif strInput == '5':
		dataInput = input("Dato a modificar: ")
		dataInput2 = input("Nuevo dato: ")
		myList.update(dataInput,dataInput2)
		
