import MySQLdb
import json

from API import Api


class Db():

    def __init__(self):

        self.country = Api("None")
        self.country.getApi()


    def setPais(self):

        self.mycursor = mydb.cursor()
        sql = "INSERT INTO datos (nombre,capital,habitantes) VALUES(%s,%s,%s)"
        val = (self.country.nombre, self.country.capital, self.country.poblacion)
        self.mycursor.execute(sql, val)
        mydb.commit()
        print(self.mycursor.rowcount, "registro ha sido insertado con exito.")

    def getDatos(self):

        self.mycursor = mydb.cursor()
        self.mycursor.execute("SELECT * FROM datos")
        self.myresult = self.mycursor.fetchall()
        """for result in self.myresult:
            self.lista = list(result)
            #print(self.lista)
            self.lista_json = json.dumps(self.lista)
            print(self.lista_json)


        #return self.lista"""

mydb = MySQLdb.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "pais"
)


#db = Db()
#db.getDatos()