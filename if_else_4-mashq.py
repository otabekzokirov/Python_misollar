print("'Temuriylar' muzeyi")
n=int(input("Iltimos, yoshingizni kiriting: "))
if n<4 or n>60:
    narx=0
elif n<18:
    narx=10000
else:
    narx=20000
print(f"Bilet narxi: {narx} so'm.")