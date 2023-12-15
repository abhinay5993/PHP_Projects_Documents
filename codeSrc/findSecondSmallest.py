def findSmallestAndSecondSmallestNum():
    imp_lst=[]
    noOfItems=int(input("Enter Number of Items : "))
    for it in range(noOfItems):
        item_dt=int(input("Enter The Item : "))
        imp_lst.append(str(item_dt))
    print("\nList of Items : ",imp_lst)
    smNum=float('inf')
    secSmNum=float('inf')
    for ni in imp_lst:
        flt_val=float(ni)
        if flt_val<=smNum:
             smNum,secSmNum=flt_val,smNum
        elif flt_val<secSmNum:
             secSmNum=flt_val
    print("\nSmallest Number : ",smNum)
    print("\nSecond Smallest Number : ",secSmNum)

findSmallestAndSecondSmallestNum()
