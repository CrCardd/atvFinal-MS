salmin = float(input("Informe o Salario Minimo atual:\n>> "))

salbruto = float(input("Informe o Salario bruto:\n>> "))

desc = float(input("Informe a porcentagem de imposto a ser pago:\n>> "))

desc = salbruto * desc
respliq = salbruto - desc


if desc <= salmin:
    print(f"O salario liquido {respliq} e seus impostos estão MENORES que um salario minimo. ")

else:
    print(f"O salario liquido {respliq} e seus impostos estão MAIORES que um salario minimo. ")

