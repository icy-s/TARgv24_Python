# #ülesanne 2
# while True:
#     try:   
#         A=int(input("Sisesta A: "))
#         break
#     except:
#         print("On vaja naturaalne arv")
# summa=0
# if A>0:
#     for i in range(1,A+1,1): #start, stop, step
#         summa+=i   #summa = summa + i
#         print(f"{i}. samm summa={summa}")
# print(f"Vastus {summa}")

# #ülesanne 3
# p=1
# for j in range(8):
#     while True:
#         try:   
#             arv=float(input(f"Sisesta {j+1} arv: "))
#             break
#         except:
#             print("On vaja arv")
#     if arv>0:
#         p*=arv
#     else:
#         print("Korrutame arvud rohkem kui 0")
#     print(f"{j+1}. samm korrutis= {p}")
# print(f"Lõpptulemus on {p}")

# #ülesanne 4
# for i in range(10,21,1):
#     print(i**2, end=";")

# #ülesanne 8
# for d in range (1,21):
#     print(f"{d} inch = {d*2.5}cm")

# #ülesanne 15
# for read in range(10):
#     for rida in range(10):
#         print (rida, end=" ")
#     print()

# #ülesanne 16
# for j in range(1,10):
#     for i in range(1,10):
#         if i==j:
#             print(j, end=" ")
#         else:
#             print("0", end=" ")
#     print()