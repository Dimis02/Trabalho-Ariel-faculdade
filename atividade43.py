def calcular_conta(hamburguer, cheeseburger, fritas, refrigerante, milkshake):
    preco_hamburguer = 3.00
    preco_cheeseburger = 2.50
    preco_fritas = 2.50
    preco_refrigerante = 1.00
    preco_milkshake = 3.00
    
    total_hamburguer = hamburguer * preco_hamburguer
    total_cheeseburger = cheeseburger * preco_cheeseburger
    total_fritas = fritas * preco_fritas
    total_refrigerante = refrigerante * preco_refrigerante
    total_milkshake = milkshake * preco_milkshake
    
    total_conta = total_hamburguer + total_cheeseburger + total_fritas + total_refrigerante + total_milkshake
    return total_conta

def main():
    hamburguer = int(input("Quantos hambúrgueres você consumiu? "))
    cheeseburger = int(input("Quantos cheeseburgers você consumiu? "))
    fritas = int(input("Quantas porções de fritas você consumiu? "))
    refrigerante = int(input("Quantos refrigerantes você consumiu? "))
    milkshake = int(input("Quantos milkshakes você consumiu? "))
    
    conta_final = calcular_conta(hamburguer, cheeseburger, fritas, refrigerante, milkshake)
    
    print("O valor total da sua conta é R$ {:.2f}".format(conta_final))

if __name__ == "__main__":
    main()
