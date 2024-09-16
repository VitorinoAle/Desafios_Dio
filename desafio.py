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

def depo(valor,depositos,saldo,/):#Posição 
  if valor>0:
    saldo += valor
    depositos.append(valor)
    print('Depósito realizado com sucesso.')
  else:
    print('Valor inválido.')

  return saldo,depositos

def saque(*,valor,numero_saques,limites_saques,saldo,limite,saques):#keyword only
  if valor>0:
    if numero_saques<limites_saques and valor<=saldo and valor<=limite:
      saldo -= valor
      numero_saques +=1
      saques.append(valor)
      print('Saque realizado com sucesso.')
    elif numero_saques>=limites_saques:
          print('Limite na quantidade de saques atingido, tente novamente amanhã.')
    elif valor>limite:
      print('Limite de R$ 500,00 por saque, tente novamente.')

    elif valor>saldo:
      print('Saldo insuficiênte para o valo desejado, tente novamente com outro valor.')
    else:
      print('Valor inválido.')

  return saldo, numero_saques, saques
  
def ext_completo(saldo,/,*,saque,deposito):#Posição e Keyword
  if len(saque) + len(deposito) == 0:
    print('Não foram realizadas Movimentações.')
  else:
    print(f'Foram realizadas {len(saque) + len(deposito)} Operações: {len(saque)} Saque(s) e {len(deposito)} Deposito(s).')
    extrato_deposito(deposito)
    extrato_saque(saque)
    verificar_saldo(saldo)

saldo = 0
limite = 500
extrato = True
depositosT = []
saquesT = []
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:
  extrato = True
  opcao = input(menu)

  if opcao == "1": #Deposito
    valor = float(input('Informe o valor que deseja depositar: '))

    saldo, depositosT = depo(valor,depositosT,saldo)

  elif opcao == "2": #Saque
    valor = float(input('Informe o valor que deseja sacar: '))

    saldo, numero_de_saques, saquesT = saque(
      valor=valor,
      numero_saques=numero_de_saques,
      limites_saques=LIMITE_SAQUES,
      saldo=saldo,
      limite=limite,
      saques=saquesT
    )

  elif opcao == "3": #Extrato

    while extrato:
      entrada = input(menu_extrato)

      if entrada == 'D': #Somente Depositos
        extrato_deposito(depositosT)

      elif entrada == 'R': #Somente Saques
        extrato_saque(saquesT)

      elif entrada == 'S': #Somente Saldo
        verificar_saldo(saldo)

      elif entrada == 'C': #Extrato Completo
        ext_completo(saldo,saque=saquesT,deposito=depositosT)

      elif  entrada == "Q": #Sair de Extratos
          extrato = False
      
      else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    
  elif opcao == "4":
    break

  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")