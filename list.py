list1=[1,2,3,2,1]
list2=[3,4,5,6,3]

copy_list1=list1.copy()
copy_list2=list2.copy()

copy_list1.reverse()
copy_list2.reverse()
print(copy_list1)
print(copy_list2)

if copy_list1==list1:
    print("list1 is a palindrome")
else:
    print("list1 is not a palindrome")

if copy_list2==list2:
    print("list2 is a palindrome")
else:
    print("list2 is not a palindrome")