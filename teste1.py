import sqlite3 #importa da biblioteca

try: # serve como sistema de validasao                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    banco = sqlite3.connect('banco.db') # cria conexão com banco de dados 

    cursor = banco.cursor() # cria cursor com conexao chamada banco 

    cursor.execute("CREATE TABLE aluno(id_aluno int, Nome text, idade int, email text)")# cria uma tabela com nome,idade e gmail

    cursor.execute("INSERT INTO aluno VALUES (1, 'JOÃO',20,'joaozinholeroy@gmail.com') ")# insere  na tabela nome , idade e gamil 
    cursor.execute("INSERT INTO aluno VALUES (2, 'jheimes',25,'rick@gmail.com') ") # insere  na tabela nome , idade e gami
    cursor.execute("INSERT INTO aluno VALUES (3, 'ricardo',26,'jheimesbrow@gmail.com') ") # insere  na tabela nome , idade e gami
    banco.commit()# comfirma e salva as altaracões no banco de dados 
    print("Os dados foram adicionados com sucesso!!")# mostra a mensagem na tela <-


    cursor.execute("Select *FROM aluno")# serve pra ver se tabela esta criada 
    print(cursor.fetchall()) #retorna todas a lihas restante do resultado

    cursor.execute("DELETE from aluno WHERE idade = 20")#deleta idade da sua tabela 

    banco.commit()# comfirma e salva as altaracões no banco de dados
    banco.close()#fecha conexão com banco
    print("Os dados foram removidos com sucesso!!")# mostra na tela <-

except sqlite3.Error as erro:# se codigo nao for validado automaticamente da erro
    print("Erro ao excluir: ", erro) #mostra na tela <-
