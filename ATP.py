def style():
 print(25 * '\033[34m<>')
def espaco():
 print('')
from datetime import datetime
from time import sleep
def obter_limite():
 style()
 espaco()
 print('\033[34mOlá!! Seja bem vindo a lojas Especiais Ferreira...\033[34m')
 espaco()
 style()
 sleep(2)
 print('')
 print('Para continuar será preciso fazer uma análize de crédito...')
 espaco()
 style()
 espaco()
 sleep(2)
 print('Por favor, insira as seguintes informações _ ')
 style
 espaco()
 sleep(1)
 cargo_empresa = str(input('Cargo na empresa em que trabalha: ')).upper()
 salario = float(input('Salário: '))
 data_nascimento = str(input('Data de nascimento: dd/mm/aaaa - '))
 ano_nasc = int(data_nascimento.split('/')[2])
 hoje = datetime.now()
 ano_atual = int(hoje.strftime('%Y')) # Busca o ano atual
 idade = ano_atual - ano_nasc
 Limite_credito = salario * (idade / 1000) + 100
 return Limite_credito, idade
 print(f'Cargo: {cargo_empresa}\nNascimento: {ano_nasc}\nSalário: R${salario}\nidade: {idade} anos')
 espaco()
 print(f'Seu limite de crédito para gastar\nem quaisquer produtos nas\nlojas Ferreira é de R${Limite_credito} ')
 espaco()
 style()
 espaco()
def verificar_produto(Limite):
 nome_completo = 'Fabio Ferreira dos Santos'
 tam_nome_completo = len(nome_completo)
 primeiro_nome = (nome_completo.split()[0])
 tam_primeiro_nome = len(primeiro_nome)
 produto = str(input('Por favor, digite o nome do produto que deseja escolher: ')).upper()
 espaco()
 print(produto)
 espaco()
 valor = float(input('Agora digite o valor do produto escolhido: '))
 print(f'R${valor}')
 desconto = 0
 bloqueado = 0
 if valor < Limite * (0.6):
 print('\033[33mLiberado')
 elif valor < (Limite * 0.9):
 print('\033[33mLiberado ao parcelar em até 2 vezes')
 elif valor < Limite:
 print('\033[33mLiberado ao parcelar em 3 ou mais vezes')
 else:
 print('\033[34mBloqueado')
 bloqueado = 1
 if (not bloqueado):
 if valor > tam_nome_completo and valor < idade:
 valor_desconto = valor - tam_primeiro_nome
 espaco()
 print(
 f'\33[32mVocê terá um desconto igual à R${valor_desconto} pois o primeiro nome do nome escolhido para o sorteio tem
{tam_primeiro_nome} caracteres')
 espaco()
 print('O valor com desconto será de R${}'.format(valor_desconto))
 else:
 print('Desconto inexistente')
 Limite -= valor
 espaco()
 return(Limite)
Limite, idade = obter_limite()
qtd_produtos = int(input('Por favor... Digite a quantidade de produtos escolhidos: '))
print(qtd_produtos)
for i in range(qtd_produtos):
 Limite = verificar_produto(Limite)
 print(f'Valor do limite atualizado = R${Limite:.2f}')
print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print('\33[35mFIM DA ANÁLIZE')
