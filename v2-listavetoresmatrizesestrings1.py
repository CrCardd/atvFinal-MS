names = []

nums = []

for i in range(5):
    names.append(input(f'Insira o {i}° nome:\n>> '))
    nums.append(float(input(f'Insira o {i}° valor:\n>> ')))
    
print('--------------------------------------')
for i in range(len(nums)):
    print(f'{names[i]} com o valor x2 = {nums[i] * 2}')