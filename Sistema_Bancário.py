menu = """

 [d] Depositar
 [s] Sacar
 [e] Extrato
 [q] Sair

=> """

saldo = 0
extrato = ""
quantidade_saques = 0
valor_total_saque = 0
quantidade_deposito = 0
valor_total_deposito = 0
LIMITE_SAQUES = 3
LIMITE_POR_SAQUE = 500
while True:

     opcao = input(menu)

     if opcao == "d":
        valor_depositado = float(input("Digite quanto deseja depositar:\n"))
        while valor_depositado <= 0: 
         print("O valor digitado é inválido.")
         valor_depositado = 0
         valor_depositado +=  float(input("Digite quanto deseja depositar:\n"))
        print(f"Você depositou R${valor_depositado:.2f} na sua conta.")
        saldo += valor_depositado
        extrato += f"Deposito realizado no valor de R${valor_depositado:.2f}\n"
    
     elif opcao == "s":
         if saldo > 0 :
             if quantidade_saques == 3 :
                 print("Limite de saque diário atingido.")
                 
             else:
                 valor_saque = float(input(f""" Seu saldo atual é R${saldo}
 Digite o valor que deseja sacar:\n"""))
                 if valor_saque <= 0:
                     print("Valor inválido")
                 elif valor_saque <= 500:        
                      saldo -= valor_saque
                      quantidade_saques += 1
                      valor_total_saque += valor_saque
                      extrato += f"Saque realizado no valor de R${valor_saque:.2f}\n"
                      print(f"Você realizou {quantidade_saques} de {LIMITE_SAQUES} saques diários.")
                 else:
                     print("Valor desejado extrapola o limite de R$500,00")
                          
         else:
             print("Sua conta não permite ficar com saldo negativo")
         
     elif opcao == "e":
        print("            Extrato           ")
        print("--------------------------------------------")
        print(f"Seu saldo atual é R${saldo:.2f}")        
        print(extrato.center(10," "))
        print("--------------------------------------------")        
    
     elif opcao == "q":
        break
     
     else:
        print("Operação inválida, por favor selecione novamente a operação desejada")