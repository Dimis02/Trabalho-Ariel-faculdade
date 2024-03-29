#Uma companhia de carros paga a seus empregados um salário de R$ 500,00 por mês mais uma comissão de R$ 50,00 para cada carro 
#vendido e mais 5% do valor da venda. Elabore um algoritmo para calcular e imprimir o salário do vendedor num dado mês recebendo 
#como dados de entrada o nome do vendedor, o número de carros vendidos e o valor total das vendas. 

vendedor = (input("Nome do Vendedor: "))
carros = int(input("Quantidade de carros vendidos : "))
valortotal = int(input("O valor total de vendas :"))

calculo = carros* 50.00
comicao = valortotal* 0.5
salario = carros + comicao + 500
print (f"o salario do vendedor {vendedor} é R$ {salario:,}")
