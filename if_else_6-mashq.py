maxsulotlar=["olma","gilos","behi","limon","banan","pomidor","tarvuz","qovun","apelsin","nok","shaftoli"]
savat=[]
for i in range(5):
    n=input(f"{i+1}-maxsulot nomini kiriting: ")
    savat.append(n.lower())
for buyurtma in savat:
    if buyurtma in maxsulotlar:
        print(f"Do'konda {buyurtma} maxsuloti bor.")
    else:
        print(f"Do'konda {buyurtma} maxsuloti yo'q.")