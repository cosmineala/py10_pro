def nr_elemente(lis):

	return lis.count()



def multime_print(lis):

	print(lis)



def suport(lis):

	sup = lis.copy()

	sup.sort()

	n = 0

	while sup[n] != sup[-1]:

		m = sup.count( sup[n] ) - 1

		while m :

			sup.remove( sup[n] )

			m = m - 1

	n = n + 1

	return sup





def gen( lis ):

	n = random.randint( 1 , 101 )

	while n:
		
		lis.insert( random.randint( 1 , 101 ) )

		n = n - 1



def inserare( lis ):

	n = int( input("Numar de termeni >>> ") )

	while n:
		
		lis.insert( int( input( ">>> " ) ) )







def meniu(lis):

	print("Exit >>> 0")
	print("Crearea multimii >>> 1")
	print("Afisarea multimii >>> 2")
	print("Determinarea numarului de elemente din multime >>> 3")
	print("Determinarea daca multimea este vida >>> 4")
	print("Determinarea daca un element apartine multimii >>> 5")
	print("Determinarea suportul multimii multiple >>> 6")
	print("Determinarea numarului k(e, M), pentru un element e specificat >>> 7")

	m = int( input( ">>> " ) )

	if m == 0 :
		return

	if m == 1 :
		gen(lis) 

	if m == 2 :
		multime_print(lis)

	if m == 3 :
		nr_elemente(lis)

	if m == 4 :
		if nr_elemente(lis) :
			print("Multimea nu este vida")
		else
			print("Multimea este vida")

	if m == 5 :





lis = []

