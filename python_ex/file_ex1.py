f = open("C:/test2.txt", 'w')
f.write("Life is too short you need Java")
f.close()

f = open("C:/test2.txt", 'r')
a = f.read()
arrA = a.split(" ")
arrA[6] = 'Python'

a = ' '.join(arrA)

f.close()

f = open("C:/test2.txt", 'w')
f.write(a)
f.close()
