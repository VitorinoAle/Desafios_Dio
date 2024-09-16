menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Cliente
[5] Listar dados do Cliente
[6] Criar Conta
[9] Sair

=> """

clientes = {}

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

def check_usuario(doc,listagem):
  for item in listagem:
    if item ['cpf'] == doc:
      return True
  return False

def criar_usuarios(listagem):
  print('Informe os seguintes dados do cliente:')
  cpf = input('CPF: ').replace('.','').replace('-','')
  if check_usuario(cpf,listagem):print('Cliente já cadastrado.')
  else:
    nome = input('Nome completo: ')
    nasc = input('Data de nascimento (dd-mm-aaaa): ')
    end = input('Endereço(logradouro, nro - bairro - cidade/sigla estado): ')

    listagem.append({'cpf':cpf,'nome':nome,'data_nascimento':nasc,'endereco':end})
    print('Cliente cadastrado com sucesso.')

def listar_dados(listagem):
  cpf = input('Informe o CPF do cliente: ').replace('.','').replace('-','')
  if not check_usuario(cpf,listagem):print('Cliente inexistente.')
  else:
    for item in listagem:
      if item['cpf'] == cpf:
        nome = item.get('nome')
        nasc = item.get('data_nascimento')  
        end = item.get('endereco')

    print('===> Dados do Cliente <===')
    print(f'Cliente: {nome} ')
    print(f'Data de Nascimento: {nasc} - CPF: {cpf}')
    print(f'Endereço: {end}')


saldo = 0
limite = 500
extrato = True
depositosT = []
saquesT = []
usuarios = []
numero_de_saques = 0
LIMITE_SAQUES = 3
AGENCIA = '0001'

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
    
  elif opcao == '4': #Criar cliente
    criar_usuarios(usuarios)
  
  elif opcao == '5': #Exibir dados do cliente
    listar_dados(usuarios)

  elif opcao == "9": #Sair
    break

  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")