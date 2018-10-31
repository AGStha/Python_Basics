def check(k):
	if (k%2==0):
		print (k)
	else:
		print (2*k)

n=int(input())

for i in range(1,n):

	check(i)
#Alt:
'''
n = input()
for i in xrange(1, n+1):
	if i%2 == 0:
		print i
	else:
		print 2*i
'''
