ls = []
total = 0.0
 
for i in range(5):
    f = float(input("กรอกตัวเลขทศนิยม ครั้งที่ {0:d} : ".format(i+1)))
    ls.append(f)
    total += f
 
print("")
 
for i in range(5):
    print("แสดงผลตัวเลขทศนิยม ครั้งที่ {0:d} : {1:.2f}".format(i+1, ls[i]))
 
print("\nผลรวมทั้งหมด คือ {0:.2f}".format(total))
