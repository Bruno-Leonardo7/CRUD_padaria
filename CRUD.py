import mysql.connector
import utilitarios
from time import sleep

conexao = mysql.connector.connect(
      host='localhost',
      user='root',
      password='@Conexao2812',
      database='crud_padaria'
)

cursor = conexao.cursor()

# CRUD - CREATE | READ | UPDATE | DELETE

print(f'{"SEJA BEM VINDO A PADARIA PYTHON!":^40}')
while True:
      print('-='*20)
      print(f'{"MENU":^40}')
      print('-='*20)
      print('1 - Adicionar um produto\n'
            '2 - Ver os produtos\n'
            '3 - Atualizar um produto\n'
            '4 - Apagar um produto\n'
            '5 - Sair')
      print('-='*20)
      resposta_acao = input('Digite o que deseja realizar: ').strip()
      if resposta_acao.isalpha() == True or int(resposta_acao) not in (1,2,3,4,5):
            print('Você digitou um valor inválido! Tente novamente!')
            sleep(2)
      else:
            if int(resposta_acao) == 1:
                  nome_produto = str(input('Digite o nome do produto: ').strip().capitalize())
                  while True:
                        valor_produto = input('Digite o valor do produto: ').strip()
                        valor_produto = utilitarios.validacaoNum(valor_produto)
                        if valor_produto > 0:
                              break
                        else:
                              print('O texto digitado não é um número! Tente novamente!')
                  comando_MySQL = f'INSERT INTO tabela_padaria(nome_produto, valor_produto) ' \
                                  f'VALUES ("{nome_produto}", {valor_produto})'
                  cursor.execute(comando_MySQL)
                  conexao.commit()
                  print('Produto registrado com sucesso!')
                  sleep(2)
            elif int(resposta_acao) == 2:
                  comando_MySQL = 'SELECT * FROM tabela_padaria'
                  cursor.execute(comando_MySQL)
                  ver_produtos = cursor.fetchall()
                  print(f'{"     COD     ":^15}',end='')
                  print(f'{"     NOME    ":^15}', end='')
                  print(f'{"    VALOR    ":^15}')
                  for linha in range(0,len(ver_produtos)):
                        for coluna in range(0,3):
                              print(f'{ver_produtos[linha][coluna]:^15}',end='')
                        print()
                  sleep(2)
            elif int(resposta_acao) == 3:
                  resposta_mudanca = 1
                  while True:
                        if resposta_mudanca > 0 and resposta_mudanca < 3:
                              cod_produto = input('Digite o código do produto que deseja atualizar: ').strip()
                              cod_produto = utilitarios.validacaoNum(cod_produto)
                              if cod_produto > 0:
                                    comando_MySQL = 'SELECT * FROM tabela_padaria'
                                    cursor.execute(comando_MySQL)
                                    ver_produtos = cursor.fetchall()
                                    if len(ver_produtos) == 0:
                                          print('O código digitado não existe! Tente novamente!')
                                    else:
                                          while True:
                                                utilitarios.linhas(14)
                                                print(f'{"POSSIBILIDADES DE MUDANÇAS":^20}')
                                                utilitarios.linhas(14)
                                                print('1 - NOME\n'
                                                      '2 - VALOR\n'
                                                      '3 - VOLTAR')
                                                resposta_mudanca = input('Digite o que deseja mudar: ').strip()
                                                resposta_mudanca = utilitarios.validacaoNum(resposta_mudanca)
                                                if resposta_mudanca > 0:
                                                      if resposta_mudanca == 1:
                                                            mudanca_nome = input('Digite o novo nome do produto: ').strip()
                                                            comando_MySQL = f'UPDATE tabela_padaria SET nome_produto = "{mudanca_nome}" WHERE cod_produto = {int(cod_produto)}'
                                                            print('Nome atualizado com sucesso!')
                                                            sleep(2)
                                                            break
                                                      elif resposta_mudanca == 2:
                                                            mudanca_valor = input('Digite o novo valor do produto: ').strip()
                                                            mudanca_valor = utilitarios.validacaoNum(mudanca_valor)
                                                            if mudanca_valor > 0:
                                                                  comando_MySQL = f'UPDATE tabela_padaria SET valor_produto = {mudanca_valor} WHERE cod_produto = {int(cod_produto)}'
                                                                  print('Valor atualizado com sucesso!')
                                                                  sleep(2)
                                                                  break
                                                            else:
                                                                  print('O texto digitado não é um número! Tente novamente!')
                                                      elif resposta_mudanca == 3:
                                                            break
                                                      else:
                                                            print('Você digitou um valor inválido! Tente novamente!')
                                                      cursor.execute(comando_MySQL)
                                                      conexao.commit()
                                                else:
                                                      print('Você digitou um valor inválido! Tente novamente!')

                              else:
                                    print('O texto digitado não é um número! Tente novamente!')
                        else:
                              sleep(2)
                              break
            elif int(resposta_acao) == 4:
                  while True:
                        cod_produto = input('Digite o código do produto que deseja apagar: ').strip()
                        cod_produto = utilitarios.validacaoNum(cod_produto)
                        if cod_produto > 0:
                              comando_MySQL = f'SELECT * FROM tabela_padaria WHERE cod_produto = {cod_produto}'
                              cursor.execute(comando_MySQL)
                              ver_produtos = cursor.fetchall()
                              if len(ver_produtos) == 0:
                                    print('O código digitado não existe! Tente novamente!')
                              else:
                                    comando_MySQL = f'DELETE FROM tabela_padaria WHERE cod_produto = {cod_produto}'
                                    cursor.execute(comando_MySQL)
                                    conexao.commit()
                                    print('Produto apagado com sucesso!')
                                    sleep(2)
                                    break
            else:
                  conexao.close()
                  cursor.close()
                  break
