information = input()
wood_for_table = int(information.split(" ")[0])
pocket_num = int(information.split(" ")[1])
pocket_max = int(information.split(" ")[2])
wood_stock = int(information.split(" ")[3])
ans = 0
if pocket_max == wood_for_table:
    if wood_stock / pocket_num == pocket_max:
        print(pocket_num)
        exit()
if wood_stock == pocket_max * pocket_num and pocket_max > wood_for_table:
     print(0)
     exit()
if wood_for_table >= pocket_max:
    print(int(wood_stock / wood_for_table))
    exit()
if pocket_max >= wood_stock:
    if (wood_stock / wood_for_table) > (pocket_num - 1):
        print(pocket_num - 1)
        exit()
    else:
        print(int(wood_stock / wood_for_table))
        exit()
if pocket_num >= wood_stock:
    print(int(wood_stock / wood_for_table))
    exit()
while wood_stock > 0:
    wood_stock -= wood_for_table
    pocket_num -= 1
    if wood_stock >= 0 and pocket_num > 0:
        if wood_stock / pocket_num <= pocket_max:
            ans += 1
        else:
            break
    elif pocket_num == 0 and wood_stock == 0:
        ans += 1
        break
    elif wood_stock < 0 and pocket_num <= 0:
        break
    elif wood_stock > 0 and pocket_num <= 0:
        break
    elif wood_stock < 0 and pocket_num > 0:
        # if wood_stock == 0:
        #     ans += 1
        break

print(ans)
