List=[21,43,46,72,76,87]
x=int(input("enter the search value"))
low=0
high=len(List)-1
while low<=high:
    mid=(low+high)//2
    if x==List[mid]:
        print("value found")
        break
    if x>List[mid]:
        low=mid+1
    if x<List[mid]:
        high=mid-1
    if low>high:
        print("not found")