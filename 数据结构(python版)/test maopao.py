# coding:gbk
def bubblesort(list):
    if list!=None:
       if len(list)==1:
          pass
       else:
          for i in range(len(list)):
                print('[',i,']')
                for j in range(len(list)-1):
                    if list[j]>list[j+1]:
                       list[j],list[j+1]=list[j+1],list[j]
                       print("'",list,"'")
                    else:
                            print("*",list,"*")
                    print('"',list,'"')
    print (list)
list1=[2,5,4,8,6,1,5]
bubblesort(list1)
