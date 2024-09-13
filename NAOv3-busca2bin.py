nums = []

for i in range(10):
    nums.append(int(input(f'Informe o {i}° valor:\n>> ')))
    
print(nums)
search = int(input('Informe um valor a ser procurado:\n>> '))
found = False
low = 0
high = 9


while low <= high and not found:
    mid = int((high+low) / 2)
    
    if search < nums[mid]:
        high = mid+1
    elif search > nums[mid]:
        low = mid+1
    else:
        found = True

if found:
    print('Foi encontrado!')
else:
    print('Não foi encontrado!')