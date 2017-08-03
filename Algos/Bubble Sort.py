
def sort(a):
	for i in range(0,len(a)):
		for j in range(0,i):
			if a[i]<=a[j]:
				temp=a[i]
				a[i]=a[j]
				a[j]=temp
a=[]
temp=0
while True:
	x = input("Enter Element: ")
	print(x)
	if x == "stop":
		break
	elif x.isdigit():
		a.append(int(x))
sort(a)
print(a)
