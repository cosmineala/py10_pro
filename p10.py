from random import *
from math import *

# Determinarea numarului de elemente ( 3  4 )
def nr_elemente(lis):

	return len( lis )


# Afisarea multimii ( 2 )
def multime_print(lis):

	print(lis)


# Determinarea suportului ( 6 )
def suport(lis):

	sup = lis.copy()

	sup.sort()

	n = 0

	while n < len( sup ) :

		m = sup.count( sup[n] ) - 1

		while m :

			sup.remove( sup[n] )

			m = m -1

		n = n + 1

	return sup




# Crearea multimii ( 1 )
def gen( lis ):

	n = randint( 1 , 101 )

	while n:
		
		lis.append( randint( 1 , 101 ) )

		n = n - 1

# Adaugare de termeni ( 11 )
def inserare( lis ):

	n = int( input("Numar de termeni >>> ") )

	for i in range( 0 , n):
		
		lis.append( int( input( ">>> " ) ) )


# Verifica daca lista este inclusa in alta lista ( 8 )
def if_include(lis):

	lis2 = []
	gen(lis2)

	sup_lis = []
	sup_lis2 = []

	sup_lis = suport(lis)
	sup_lis2 = suport(lis2)

	for i in range( 0 , len(sup_lis) - 1) :

		if sup_lis[i] in sup_lis2 :
			return "Este inclusa"

	return "Nu este inclusa"

# Operatiile de reuniune diferenta si incluziune ( 9 )
def operation(lis):

	 lis2 = []
	 gen(lis2)

	 print( "Reuniune : " + str( set( lis ) | set( lis2 ) ) )
	 print( "Intersectie : " + str(  set( lis ) & set( lis2 ) ) )
	 print( "Diferenta : " + str( set( lis ) - set( lis2 ) ) )


def if_inlude_who(lis):

	lis2 = []
	gen(lis2)

	sup_lis = []
	sup_lis2 = []

	sup_lis = suport(lis)
	sup_lis2 = suport(lis2)

	if len( sup_lis ) < len( sup_lis2 ) :

		if len( set( sup_lis ) & set( sup_lis2 ) ) == len( sup_lis ) :

			print("Multimea 1 inclusa in 2")

		else : 

			print("Multimea 1 nu este inclusa in 2")

	else : 

		if len( set( sup_lis ) & set( sup_lis2 ) ) == len( sup_lis2 ) :

			print("Multimea 2 inclusa in 1")

		else : 

			print("Multimea 2 nu este inclusa in 1")


# Meniul
def meniu(lis):

	print("Exit >>> 0")
	print("Crearea multimii >>> 1")
	print("Afisarea multimii >>> 2")
	print("Determinarea numarului de elemente din multime >>> 3")
	print("Determinarea daca multimea este vida >>> 4")
	print("Determinarea daca un element apartine multimii >>> 5")
	print("Determinarea suportul multimii multiple >>> 6")
	print("Determinarea numarului k(e, M), pentru un element e specificat >>> 7")
	print("Determinarea daca multimea multipla curenta este inclusa in alta multime specificata >>> 8")
	print("Operatiile de reuniune, diferenta si intersectie a doua multimi multiple >>> 9")
	print("Compararea a doua multimi pe baza operatiei de incluziune >>> 10")
	print("Introduceti n elemente >>> 11")

	m = int( input( ">>> " ) )

	if m == 0 :
		return

	if m == 1 :
		gen(lis) 

	if m == 2 :
		multime_print(lis)

	if m == 3 :
		print( nr_elemente(lis) )

	if m == 4 :
		if nr_elemente(lis) :
			print("Multimea nu este vida")
		else :
			print("Multimea este vida")

	if m == 5 :
		if int( input(">>> ") ) in lis :
			print("Termenul este in lista")
		else :
			print("Termenul NU este in lista")

	if m == 6 :
		print( suport( lis ) )

	if m == 7 :
		print( lis.count( int( input("Introduceti elementul e \n>>>") ) ) )

	if m == 8 :
		print( if_include(lis) )

	if m == 9 :
		operation(lis)

	if m == 10 :
		if_inlude_who(lis)

	if m == 11 :
		inserare( lis )

	meniu(lis)



# Main

lis = []

meniu(lis)

print("Program terminat")
