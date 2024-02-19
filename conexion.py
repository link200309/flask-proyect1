import MySQLdb
from flask_mysqldb import MySQL


class conexion:
    def __init__(self,app):
        app.config['MYSQL_HOST'] = 'localhost'
        app.config['MYSQL_USER'] = 'root'
        app.config['MYSQL_PASSWORD'] = 'link79743114200309'
        app.config['MYSQL_DB'] = 'administracion_personal'
        self.mysql = MySQL(app)
    
    def add_contact(self, fullname, phone, email):
        cursor = self.mysql.connection.cursor()
        cursor.execute('INSERT INTO contacts values (NULL,%s,%s,%s)', (fullname, phone, email))
        self.mysql.connection.commit()
        
    def get_contacts(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute('SELECT * FROM contacts')
        return cursor.fetchall()
    
    def delete_contact(self, id):
        cursor = self.mysql.connection.cursor()
        cursor.execute(f'DELETE FROM contacts WHERE id={id}')
        self.mysql.connection.commit()
        
    def get_contact(self, id):
        cursor = self.mysql.connection.cursor()
        cursor.execute(f'SELECT * FROM contacts WHERE id={id}')
        return cursor.fetchall()[0]
    
    def update_contact(self, id, fullname, phone, email):
        cursor = self.mysql.connection.cursor()
        cursor.execute("""
        UPDATE contacts 
        SET fullname=%s, phone=%s,email=%s
        WHERE id=%s
        """, (fullname, phone, email, id))
        self.mysql.connection.commit()
        
        
        
            
        
