# latihan soal dari sini https://pynative.com/python-functions-exercise-with-solutions/
# soal no 1
# def bio(name,age):
#     print(name,age)
# bio('Arif',23)
#======================================
#soal no 2
# def func1(*args):
#     for i in args:
#         print (i)
# func1(1,2,3)
#=====================================
#soal no 3
# def calculation(a,b):
#     return a+b,a-b
# res = calculation(20,10)
# print(res)
#=====================================
#soal no 4
# def showEmployee(nama,gaji=9000):
#     return nama,gaji
# print(showEmployee("Ben",9000))
# print(showEmployee("Ben"))
#====================================
#soal no 5
# def luar(a,b):
#     def dalam(a,b):
#         return a+b
#     return dalam(a,b)+5
# print(luar(5,10))
#===================================
#soal no 6
#  def hitungjumlah(angka):
#     bil = []
#     for i in range(num+1):
#         bil.append(i)  
#     return sum(bil)
# num = 10
# print(hitungjumlah(num))

# def calculateSum(num):
#     if num :
#         return num + calculateSum(num-1)
#     else:
#         return 0
# print(calculateSum(10))        
############################################
#soal no 8
# def diantara(awal,akhir):
#     deret=[]
#     for i in range(awal,akhir,2):
#         deret.append(i)
#     return deret
# print(diantara(4,30))
#=========================================
# soal no 9
alist = [4,6,8,24,12,2]
def maks(baris):
    a = sorted(baris)
    return a[-1]
print(maks(alist))
print(max(alist))

