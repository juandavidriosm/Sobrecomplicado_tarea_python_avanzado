# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import certifi
from pymongo import MongoClient

# Esta tarea se pedía con programación estructurada, pero el profesor nos facilitó documentación opcional de POO
# me pareció un reto interesante y enriquecedor hacer la tarea utilizando la POO.

# La clase usuario crea de manera pseudoaleatoria un username compuesto por tres partes: sistema operativo,
# environment y país

class Usuario:
    lista_os = ["L"]*4 + ["S"]*3 + ["A"]*2 + ["H"]
    lista_env = ["D"]*10 + ["I"]*10 + ["T"]*25 + ["S"]*25 + ["P"]*30
    lista_land = ["NOR"]*6 + ["FRA"]*9 + ["ITA"]*16 + ["ESP"]*16 + ["DEU"]*23 + ["IRL"]*30
    def __init__(self):
        self.caracteristicas = ""
        self.caracteristicas += self.lista_os[random.randint(0, 9)]
        self.caracteristicas += self.lista_env[random.randint(0, 99)]
        self.caracteristicas += self.lista_land[random.randint(0, 99)]

    def get_os(self) -> str:
        # TODO

        if self.caracteristicas[0] == "L":
            return "Linux"
        elif self.caracteristicas[0] == "S":
            return "Solaris"
        elif self.caracteristicas[0] == "A":
            return "AIX"
        elif self.caracteristicas[0] == "H":
            return "HP-UX"
        else:
            return "Unknown"

    # Devuelve lista de los Environments de users
    def get_environment(self) -> str:
        # TODO
        if self.caracteristicas[1] == "D":
            return 'Development'
        elif self.caracteristicas[1] == "I":
            return 'Integration'
        elif self.caracteristicas[1] == "T":
            return "Testing"
        elif self.caracteristicas[1] == "S":
            return "Staging"
        elif self.caracteristicas[1] == "P":
            return "Production"

        else:
            return "Unknown"

    # Devuelve lista de los países de users
    def get_country(self) -> str:
        # TODO
        if self.caracteristicas[2:5] == "NOR":
            return "Norway"
        elif self.caracteristicas[2:5] == "DEU":
            return "Germany"
        elif self.caracteristicas[2:5] == "ITA":
            return "Italy"
        elif self.caracteristicas[2:5] == "ESP":
            return "Spain"
        elif self.caracteristicas[2:5] == "IRL":
            return "Ireland"
        elif self.caracteristicas[2:5] == "FRA":
            return "France"
        else:
            return "Unknown"

    #No era parte de la tarea pero al ver la documentación me pareció interesante incluirlo
    def __str__(self):
        return "user: "+ self.caracteristicas +"\n" +"Sistema operativo: "+ \
                     self.get_os() + "\n" + "Environment: "+self.get_environment() + "\n" + "País: "+ self.get_country()


#La clase PP toma como argumento el integer "cantidad", cantidad será el tamaño de la lista de usuarios de la clase.
#La clase también contiene la lista vacía "dataset" y el dataframe "df" los cuales se
# inicializan vacío y como None inicialmente para ser posteriormente alterados.
# Al final de la clase hay dos métodos que crean gráficos
#A lo largo de la tarea implementé conceptos que no se pedían ni se dieron en clase,
# pero el profesor nos ofreció material de este para aprender y aporveché
# Al final inclusive hay una implementación con MongoDB

class PP:
    # Constructor de la clase
    def __init__(self, cantidad: int):
        self.cantidad = cantidad
        self.users = []
        self.create_users(cantidad)

        self.dataset = []
        self.df = None
    #llena la lista users
    def create_users(self, cantidad: int):
        lista_alpha = []
        for i in range(cantidad):
            user = Usuario().caracteristicas
            lista_alpha.append(user)
            cuenta= lista_alpha.count(user)
            if cuenta >= 999:
                cuenta = str(999)
            else:
                cuenta = str(cuenta).zfill(3)

            self.users.append(user+cuenta)

    def get_users(self):
        return self.users

    #devuelve lista de las partes de los usuarios que se refieren al OS
    def get_os(self) -> str:
        # TODO

        limpio = []
        for sucio in self.users:
            if sucio[0] == "L":
                limpio.append("Linux")
            elif sucio[0] == "S":
                limpio.append("Solaris")
            elif sucio[0] == "A":
                limpio.append("Aix")
            elif sucio[0] == "H":
                limpio.append("HP-UX")
            else:
                limpio.append("Unknown")

        return limpio

    #devuelve lista de las partes de los usuarios que se refieren al environment
    def get_environment(self) -> str:
        # TODO
        limpio = []

        for sucio in self.users:
            if sucio[1] == "D":
                limpio.append("Development")
            elif sucio[1] == "I":
                limpio.append("Integration")
            elif sucio[1] == "T":
                limpio.append("Testing")
            elif sucio[1] == "S":
                limpio.append("Staging")
            elif sucio[1] == "P":
                limpio.append("Production")

            else:
                limpio.append("Unknown")

        return limpio

    #devuelve lista de las partes de los usuarios que se refieren al país
    def get_country(self) -> str:
        # TODO
        limpio = []

        for sucio in self.users:

            if sucio[2:5] == "NOR":
                limpio.append("Norway")
            elif sucio[2:5] == "DEU":
                limpio.append("Germany")
            elif sucio[2:5] == "ITA":
                limpio.append("Italy")
            elif sucio[2:5] == "ESP":
                limpio.append("Spain")
            elif sucio[2:5] == "IRL":
                limpio.append("Ireland")
            elif sucio[2:5] == "FRA":
                limpio.append("France")
            else:
                limpio.append("Unknown")

        return limpio

    # Método no solicitado, pero al verla en la documentación de POO me dio curiosidad y quise intentarlo.
    def __str__(self):
        parte_os = np.array(self.get_os())
        parte_env = np.array(self.get_environment())
        parte_land = np.array(self.get_country())
        parte_num = [w[5:8] for w in self.users]


        parte_os = np.char.add(parte_os, " ")
        parte_env = np.char.add(parte_env, " ")
        parte_os_env = np.char.add(parte_os, parte_env)

        parte_os_env_land = np.char.add(parte_os_env, parte_land)
        parte_os_env_land = np.char.add(parte_os_env_land, " ")

        parte_os_env_land_num = np.char.add(parte_os_env_land, parte_num)
        parte_os_env_land_num = np.char.add(parte_os_env_land_num,", \n ")

        return ' '.join(parte_os_env_land_num)

    # genero una lista de diccionarios con las cualidades de cada user para convertirlo en dataframe de Pandas
    def set_dataframe(self):
        # TODO
        lista_users = self.users
        lista_os = self.get_os()
        lista_env = self.get_environment()
        lista_country = self.get_country()

        for i in range(len(self.users)):
            dicc_temporal = {}
            dicc_temporal["hostname"] = lista_users[i]
            dicc_temporal["os"] = lista_os[i]
            dicc_temporal["environment"] = lista_env[i]
            dicc_temporal["country"] = lista_country[i]
            node = self.users[i][5:8]
            dicc_temporal["node"] = int(node)

            self.dataset.append(dicc_temporal)

        self.df = pd.DataFrame(self.dataset)

        return self.df


    # Crea el bar plot pedido y eleva una excepción si self.df es aún None
    #Elevar una excepción no era parte de la tarea. Pero la documentación adicional lo explicaba y me
    #pareció interesante incluirlo.
    def grafico_env_per_country(self):
        try:
            self.df.groupby(['country', 'environment']).size().unstack().plot(kind="bar")
            return plt.show()
        except KeyError:
            print("la función grafico_env_per_country() no se puede ejecutar con un dataframe vacío")
        except AttributeError:
            print("es necesario llamar al método set_dataframe() antes de crear un gráfico")


    #También sigue el formato try-except del método pasado.
    def grafico_resumen(self):
        try:
            fig, axs = plt.subplots(2, 2)

            # primer gráfico
            #-----------------------------------------------------------------------------------------------
            self.df.groupby(['country', 'os']).size().unstack().plot(kind="barh",
                                                                     ax=axs[0, 0])
            axs[0, 0].set_title("Type of OS grouped by country")

            # Segundo gráfico
            # -----------------------------------------------------------------------------------------------
            df_para_Pie = pd.DataFrame(self.df.groupby(['os']).size())
            df_para_Pie.reset_index(inplace=True)
            df_para_Pie.columns = ["os", "cantidad"]
            df_para_Pie["porcentaje"] = df_para_Pie["cantidad"] / df_para_Pie["cantidad"].sum()

            axs[0, 1].pie(df_para_Pie['cantidad'], labels=df_para_Pie['cantidad'])

            L = axs[0, 1].legend()
            L.set_bbox_to_anchor((1, 1))

            for index, row in df_para_Pie.iterrows():
                primero = row["os"]
                segundo = str(round(row["porcentaje"], ndigits=4))
                L.get_texts()[index].set_text(primero + " (" + segundo + "%" + ")")


            axs[0, 1].set_title("Total Operating Systems")

            # tercer gráfico
            # -----------------------------------------------------------------------------------------------

            df_Host_per_Country = pd.DataFrame(self.df.value_counts("country"))
            # df_Host_per_Country.reset_index(inplace = True)
            df_Host_per_Country.columns = ["number of hosts"]

            # df_Host_per_Country.plot(kind = "barh",ax = axs[1,0],legend = False)

            df_Host_per_Country.reset_index(inplace=True)
            df_Host_per_Country.sort_values('number of hosts', ascending=True, inplace=True)

            sns.barplot(x="number of hosts", y="country",
                        data=df_Host_per_Country,
                        ax=axs[1, 0],
                        palette="YlGn")

            for index, value in enumerate(df_Host_per_Country["number of hosts"]):
                axs[1, 0].text(value, index,
                               str(value))

            axs[1, 0].set_xlim(0, df_Host_per_Country['number of hosts'].max() + 100)
            axs[1, 0].set_ylabel('Country')
            axs[1, 0].set_title("Total hosts by country")

            # Cuarto gráfico
            # -----------------------------------------------------------------------------------------------
            df_cuarto = self.df.groupby(["country", "environment"]).size().unstack(0).plot(kind="bar",
                                                                                           ax=axs[1, 1])

            axs[1,1].legend(loc='upper left')
            axs[1, 1].set_ylabel('Number of Hosts')
            axs[1, 1].set_title("Hosts by Country grouped by environment")

            fig.tight_layout()

            return plt.show()
        except KeyError:
            print("la función grafico_resumen() no se puede ejecutar con un dataframe vacío")
        except AttributeError:
            print("es necesario llamar al método set_dataframe() antes de crear un gráfico")

#En esta clase apliqué la herencia(lo que me faltaba implementar de POO)
#Además jugué un poco con el material adicional de Mongo.
class PP_conMongo(PP):
    usuario = "testuser"
    password = "testpass"
    cluster = "cluster0.1g32scv.mongodb.net"
    params = "?retryWrites=true&w=majority"
    ca = certifi.where()

    #connection_string = f"mongodb+srv://{usuario}:{password}@{cluster}/{params}"
    #client = MongoClient(connection_string, tlsCAFile=ca)

    def mongo_connect(self,database_name):
        connection_string = f"mongodb+srv://{self.usuario}:{self.password}@{self.cluster}/{self.params}"
        client = MongoClient(connection_string, tlsCAFile = self.ca)

        return client[database_name]

    def uno_to_mongo(self):
        database = self.mongo_connect("listaUsuarios")
        collection = database["intento"]
        collection.insert_one(random.choice(self.dataset))

    def todo_to_mongo(self):
        database = self.mongo_connect("listaUsuarios")
        collection = database["intento_grande"]
        collection.insert_many(self.dataset)

    def retrieve_mongo(self):
        usuarios_en_mongo = []
        database = self.mongo_connect("listaUsuarios")
        collection = database["intento_grande"]

        for item in collection.find():
            usuarios_en_mongo.append(item)

        return usuarios_en_mongo

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #Función que crea hostnames:
    primer_usuario = Usuario()
    print(primer_usuario.get_os(),primer_usuario.get_environment(),primer_usuario.get_country())
    print(primer_usuario) #Usa el método __str__ me pareció interesante incluirlo

   #Se puede lograr un resultado similar llamando a PP(1) pero los métodos devuelven listas en ese caso
    #Hice que si len == 1 devolviese string en vez de lista pero eso traería problemas a la hora de llamar
    #a set_dataframe
    unHostName = PP(1)
    print(unHostName.get_users(),unHostName.get_os(),unHostName.get_environment(),unHostName.get_country())
    print(unHostName)

   #Función que genera dataframe:
    Demo_set_dataframe = PP_conMongo(1500)
    #print(Demo_set_dataframe) comentado porque va a imprimir 1500 users
    Demo_set_dataframe.set_dataframe().to_csv("/Users/juandavid/Documents/Master_DS/csv_practica_python_avanzado.csv",
                                              header=True,index=False)

    hosts_df = pd.read_csv("/Users/juandavid/Documents/Master_DS/csv_practica_python_avanzado.csv")
    print(hosts_df.head())


    #Función que genera primer gráfico
    #Para ambas funciones de gráficos apliqué lo aprendido en la documentación adicional de excepciones
    demo_grafico1 = PP(0)
    demo_grafico1.grafico_env_per_country()

    demo_grafico1.set_dataframe()
    demo_grafico1.grafico_env_per_country()

    demo_grafico1 = PP(1500)
    demo_grafico1.set_dataframe()
    demo_grafico1.grafico_env_per_country()


    # Función que genera segundo gráfico
    # Para ambas funciones de gráficos apliqué lo aprendido en la documentación adicional de excepciones
    demo_grafico2 = PP(0)
    demo_grafico2.grafico_resumen()

    demo_grafico2.set_dataframe()
    demo_grafico2.grafico_resumen()

    demo_grafico2 = PP(1500)
    demo_grafico2.set_dataframe()
    demo_grafico2.grafico_resumen()

    #Prueba de conectarme, subir y descargar documentos a Mongo
    prueba = PP_conMongo(5)
    prueba.set_dataframe()
    prueba.uno_to_mongo()
    prueba.todo_to_mongo()
    print("prueba mongo:")
    print(prueba.retrieve_mongo())

