def fibonnaci(n):
	"""Base cases are n==1 or n==2
	"""
	if n==1:
		return 1
	elif n==2:
		return 1
	else:
		return (fibonnaci(n-1)+fibonnaci(n-2))

def gcd(x,y):
	if y==0:
		return x
	else:
		return (gcd(y, x%y))

def compareTo(s1,s2):
	"""the ord() function can only compare one character at a time, unfortunately
	"""
	if (len(s1) == 0 and len(s2) == 0):
		return 0
	elif (ord(s1[0]) < ord(s2[0])): 
		return (-(ord(s2[0])))
	elif (ord(s1[0]) > ord(s2[0])):
		return (abs(ord(s1[0])))
	elif (s1[1:2] == '' and s2[1:2] == ''):
		return 0
	else:
		return compareTo(s1[1:], s2[1:])
