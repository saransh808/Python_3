
def sort(a):
	for i in range(0,len(a)):
		for j in range(0,i):
			if a[i]<=a[j]:
				temp=a[i]
				a[i]=a[j]
				a[j]=temp

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

a=[]
temp=0
while True:
	x = input("Enter Element: ")
	print(x)
	if x == "stop":
		break
	elif x.isdigit():
		a.append(int(x))
b=a #creating copy on array 'a' into 'b' to use it in other sort
print("Using Bubble Sort : ")
sort(a)
print(a)
print("Using Insertion Sort : ")
insertionSort(b)
print(b)
