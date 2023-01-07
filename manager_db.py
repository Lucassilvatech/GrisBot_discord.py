"""Modulo para gerenciar tabelas de DB. a conexão tem que aceitar gerenciador de contexto"""
import mysql.connector 
from log import log

class Conexao:
    def __init__(self, host, user, password, database=None):
        self.__my_connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    def __enter__(self):
        return self.__my_connection


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__my_connection.close()





class Manager_DB:
    """Gerencia o banco de dados."""


    def create_database(self, name_database:str):
        """Cria um novo banco de dados"""
        with Conexao(**log) as conexao:
            with conexao.cursor() as cursor:
                sql = f'CREATE DATABASE {name_database};'
                cursor.execute(sql)
                conexao.commit()


    def create_table(self, name_table:str, columns:str):
        """Cria uma nova tabela"""
        with Conexao(**log) as conexao:
            with conexao.cursor() as cursor:
                sql = f'CREATE TABLE {name_table} {columns};'
                cursor.execute(sql)
                conexao.commit()


    def atualiza(self,table, column, new_value, id):
        """Atualiza um valor na (column) especificada com (new_value)
            onde tiver o (id) que for passado."""
        with Conexao(**log) as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(f'UPDATE {table} SET {column} = "{new_value}" WHERE (id = {id});')
                conexao.commit()


    def insert(self, table:str, keys:str, values:tuple):
        """Inseri os (values) na tabela passada em suas respctivas (keys == columns)."""
        with Conexao(**log)as conexao:
            with conexao.cursor() as cursor:
                sql = f"INSERT INTO {table} {keys} VALUES {values};"
                cursor.execute(sql)
                conexao.commit()
        return

    def select(self, table:str, column=None, value=None):
        """Retorna todos os registros da tabela passada ou apenas valores expecificos
        passando os parametros (column) para a coluna que quer selecionar
        (value) o valor quea coluna deve ter."""
        with Conexao(**log) as conexao:
            with conexao.cursor(dictionary=True) as cursor:
                if value:
                    sql = f'SELECT *FROM {table} WHERE {column} = "{value}";'
                else:
                    sql = f'SELECT *FROM {table};'
                cursor.execute(sql)
                result = cursor.fetchall()
                return result

                

    def add_column(self,table, name_column, definition_column):
        """Adiciona uma nova coluna na tabela passada."""
        with Conexao(**log) as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(f'ALTER TABLE {table} ADD COLUMN {name_column} {definition_column};')
                conexao.commit()


    def delete_column(self, table, name_column):
        """Dropa uma coluna da tabela"""
        with Conexao(**log) as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(f'ALTER TABLE {table} DROP COLUMN {name_column};')
                conexao.commit()


    def delete_record(self, table, id_colunm):
        """Deleta um registro da tabela"""
        with Conexao(**log) as conexao:
            with conexao.cursor() as cursor:
                sql = f'DELETE FROM {table} WHERE id = {id_colunm};'
                cursor.execute(sql)
                conexao.commit()


    def delete_database(self, name_database:str):
        """Deleta uma tabela"""
        with Conexao(**log) as conexao:
            with conexao.cursor() as cursor:
                confirmar = input(f'Essa ação ira deletar permanentimete o banco {name_database}\n' \
                                  f'e todas suas tabelas e registros. Deseja realmente continuar [y = Sim | n = não]')
                if confirmar.lower() == 'y':
                    sql = f'DROP DATABASE {name_database};'
                    cursor.execute(sql)
                    conexao.commit()
                    print(f'database {name_database} foi exclido!')
                    return
                print('A ação foi cancelada.')


    def delete_table(self, name_table:str):
        """Deleta uma tabela"""
        with Conexao(**log) as conexao:
            with conexao.cursor() as cursor:
                confirmar = input(f'Essa ação ira deletar permanentimete a tabela {name_table}\n' \
                                  f'e todos os seus registros. Deseja realmente continuar [y = Sim | n = não]')
                if confirmar.lower() == 'y':
                    sql = f'DROP TABLE {name_table};'
                    cursor.execute(sql)
                    conexao.commit()


    def show_tables(self):
        """Exibe as tabelas existentes no banco."""
        with Conexao(**log) as conexao:
            with conexao.cursor(dictionary=True) as cursor:
                cursor.execute('SHOW TABLES')
                result = cursor.fetchall()
                for valor in result:
                    print(valor)


    def show_databases(self):
        """Exibe os bancos"""
        with Conexao(**log) as conexao:
            with conexao.cursor(dictionary=True) as cursor:
                cursor.execute('SHOW DATABASES')
                result = cursor.fetchall()
                for valor in result:
                    print(valor)


if __name__ == '__main__':
    # keys = '(nome, ataque, defesa, vida, nivel, exp)'
    # values = ('Yuki', 25, 20, 100, 1, 0)
    # nome = ('Subin',)
    # val = '(nome)'
    # colunas = '(id INT PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(50))'
    print(log)
    gerente = Manager_DB()
    gerente2 = Manager_DB()


    # gerente.delete_table('teste')
    # gerente.show_tables()
    # gerente.show_databases()
    # gerente.create_database('meu_banco')
    # gerente.delete_database('meu_banco')
    # gerente.select('login','nome', 'Yukine')
    # gerente.delete_column('teste', 'bug')
    # gerente.delete_record('login', 479781826161016833)
    # gerente.create_table('teste', colunas)
    
    # gerente.add_column('teste', 'bug', 'VARCHAR(80)')
    # gerente.insert('login', keys, values)
    # gerente.insert('login', keys, values)
    # gerente.insert('teste', '(nome)', ('Subin',))
    # gerente.atualiza('ataque','20', 1)




    
    # print(gerente2.delete_record('login', 479781826161016833))
    # print(gerente2.select('manager'))
    # print(gerente2.delete_record('mochila', 479781826161016833))
    # gerente.atualiza('manager', '_status', 'ativo', 479781826161016833)

