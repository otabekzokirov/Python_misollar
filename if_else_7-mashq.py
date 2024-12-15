maxsulotlar=["tarvuz","karam","olma","behi","choy","un","pomidor","limon","kartoshka","piyoz","qovun","tarvuz","uzum"]
buyurtmalar=[]
bor_maxsulotlar=[]
mavjud_emas=[]
for i in range(5):
    n=input(f"{i+1}-maxsulotni kiriting: ")
    buyurtmalar.append(n.lower())
for buyurtma in buyurtmalar:
    if buyurtma in maxsulotlar:
        bor_maxsulotlar.append(buyurtma)
    else:
        mavjud_emas.append(buyurtma)
if mavjud_emas:
    print("Do'konimizda quyidagi maxsulotlar yo'q:")
    for maxsulot in mavjud_emas:
        print(maxsulot)
else:
    print("Siz so'ragan barcha mahsulotlarimiz do'konda bor!")