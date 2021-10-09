def syst(a,b):
	n=''
	while a>0:
		n=str(a%b)+n
		a=a//b
	print(n)

print("введите число")
x=int(input())
print("введите 2 или 8")
s=int(input())
if s!=2 or s!=8:
	print('error')
	exit()

syst(x,s)
