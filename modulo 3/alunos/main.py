'''import sqlite3
from datetime import datetime
from database import DatabaseConnection

class UserModel:

    def __init__(self):
        self.db_conn = DatabaseConnection()
        self._create_table()

    def _create_table(self):
        self.db_conn.connect()
        self.db_conn.cursor.execute(
        
         """
            CREATE TABLE aluno(
                PRIMARY KEY id_aluno INTEGER
            );
        """
        """
            CREATE TABLE endereco(
                PRIMARY KEY id INTEGER,
                local TEXT NOT NULL,
                FOREIGN KEY (id_aluno) reference alunos(id)

            );
        """
        )
        self.db_conn.close()

    def create_user(self, id_aluno, local):
        """Cria um novo usuário."""
        self.db_conn.connect()
        try:
            self.db_conn.cursor.execute(
                """
                INSERT INTO usuarios (id, local)
                VALUES (?,?);
            """,
                (id_aluno, local)
            )
            print("Usuário criado com sucesso!")
        except sqlite3.IntegrityError:
            print(f"Erro: O id '{id_aluno}' já está em uso.")
        finally:
            self.db_conn.close()

    def find_user_by_id(self, user_id):
        """Busca um usuário pelo ID."""
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM usuarios WHERE id = ?;", (user_id,))
        user = self.db_conn.cursor.fetchone()
        self.db_conn.close()
        return user
   

    def get_all_users(self):
        """Retorna todos os usuários."""
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM usuarios;")
        users = self.db_conn.cursor.fetchall()
        self.db_conn.close()
        return users'''