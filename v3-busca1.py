nums = []
for i in range(10):
    nums.append(int(input(f"Digite o {i} número:\n>> ")))
    
search = int(input("\n\nDigite o número que deseja buscar:\n>> "))
qtd = 0

for i in range(len(nums)):
    if search == nums[i]:
        qtd+=1
        
print(f"O número {search} aparece '{qtd}' vezes na lista.")