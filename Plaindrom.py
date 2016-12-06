print("ce programme determine que un nombre est plaindrom: ")

n=nb = input('donner un nombre entier: ')
n1=n
n2=0

while n1>0 :
	q=n1/10
	r=n1-10*q
	n2=10*n2+r
	n1=q
if n==n2:
	print("est plaindrom ")
else:
	print("n'est pas plaindrom ")
