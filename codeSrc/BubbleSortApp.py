def doBubbleSortForMe():
    imp_lst=[]
    noOfItems=int(input("Enter Number of Items : "))
    for it in range(noOfItems):
        item_dt=int(input("Enter The Item : "))
        imp_lst.append(str(item_dt))
    print("\nList of Items : ",imp_lst)

    for i in range(len(imp_lst)):
        for j in range(len(imp_lst)):
            if imp_lst[i]<imp_lst[j]:
                   tem=imp_lst[i]
                   imp_lst[i]=imp_lst[j]
                   imp_lst[j]=tem
    print("\nBubble Sorted List : ",imp_lst)

doBubbleSortForMe()