
n=input('donner un nombre: ');
for i in range(1,n+1):
	for j in range(1,n-i+1):
		print " ",
	for k in range(1,i+1):
		print k,
	for a in range(i-1,0,-1):
		print a,
	print "\n"

