valor_por_dia = 30.00
dias_trabalhados = int(input("Digite o número de dias trabalhados pelo encanador: "))
valor_bruto = valor_por_dia * dias_trabalhados
imposto_de_renda = 0.08 * valor_bruto
valor_liquido = valor_bruto - imposto_de_renda
print(f"A quantia líquida a ser paga é: R${valor_liquido:.2f}")