menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

menu_extrato = """
Informe qual tipo de Extrato deseja:
[D] Somente Depositos
[R] Somente Saques
[S] Somente Saldo
[C] Extrato Completo
[Q] Sair

--> """

def verificar_saldo(valor1):
  print(f' ---> Saldo de R$ {valor1:.2f} <---')

def extrato_deposito(valor1):
  if len(valor1) == 0:
    print('Não foram realizadas movimentações do tipo Deposito.')
  else:
    print('Extrato de depósitos:')
    for i in range(len(valor1)):
      print(f'{i+1}º Deposito: R$ {valor1[i]:.2f}')

def extrato_saque(valor1):
  if len(valor1) == 0:
    print('Não foram realizadas movimentações do tipo Saque.')
  else:
    print('Extrato de Saques:')
    for i in range(len(valor1)):
      print(f'{i+1}º Saque: R$ {valor1[i]:.2f}')

saldo = 0
limite = 500
extrato = True
conta = []
depositos = []
saques = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
  extrato = True
  opcao = input(menu)

  if opcao == "1": #Deposito
    valor = float(input('Informe o valor que deseja depositar: '))
    if valor>0:
      saldo += valor
      depositos.append(valor)
      print('Depósito realizado com sucesso.')
    else:
      print('Valor inválido.')

  elif opcao == "2": #Saque
    valor = float(input('Informe o valor que deseja sacar: '))

    if valor>0:
      if numero_saques<LIMITE_SAQUES and valor<=saldo and valor<=limite:
        saldo -= valor
        numero_saques +=1
        saques.append(valor)
        print('Saque realizado com sucesso.')

      elif numero_saques>=LIMITE_SAQUES:
        print('Limite na quantidade de saques atingido, tente novamente amanhã.')

      elif valor>limite:
        print('Limite de R$ 500,00 por saque, tente novamente.')

      elif valor>saldo:
        print('Saldo insuficiênte para o valo desejado, tente novamente com outro valor.')
    else:
      print('Valor inválido.')

  elif opcao == "3": #Extrato

    while extrato:
      entrada = input(menu_extrato)

      if entrada == 'D': #Somente Depositos
        extrato_deposito(depositos)

      elif entrada == 'R': #Somente Saques
        extrato_saque(saques)

      elif entrada == 'S': #Somente Saldo
        verificar_saldo(saldo)

      elif entrada == 'C': #Extrato Completo
        if len(saques) + len(depositos) == 0:
          print('Não foram realizadas Movimentações.')
        else:
          print(f'Foram realizadas {len(saques) + len(depositos)} Operações: {len(saques)} Saque(s) e {len(depositos)} Deposito(s).')
          extrato_deposito(depositos)
          extrato_saque(saques)
          verificar_saldo(saldo)   

      elif  entrada == "Q": #Sair de Extratos
          extrato = False
      
      else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    
  elif opcao == "4":
    break

  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")