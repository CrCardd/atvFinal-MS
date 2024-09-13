idade = 1
conttotal = 0
contIA = 0
contIB = 0
contJA = 0
contJB = 0
contADUL = 0

while idade > 0:
    idade = int(input("Qual a idade do nadador? (0 - sair)\n>> "))
    if idade >=18:
        contADUL+=1
        print("ADULTO \n")
    elif idade >=5 and idade<=7:
        contIA+=1
        print("infantil A \n")
        
    elif idade>=8 and idade<=10: 
        contIB+=1
        print("infantil B \n")
        
    elif idade>=11 and idade<=13:
        contJA+=1
        print("Juvenil A \n")
        
    elif idade>=14 and idade<=17:
        contJB+=1
        print("Juvenil B \n")
    
    conttotal+=1
    
                            
        
    


print(f" Categoria infantil A sao: {contIA} \n")
print(f" Categoria infantil B sao: {contIB} \n")
print(f" Categoria juvenil A sao: {contJA} \n")
print(f" Categoria juvenil B sao: {contJB} \n")
print(f" Categoria Adultos sao: {contADUL} \n")

print(f"total: {conttotal} \n")

