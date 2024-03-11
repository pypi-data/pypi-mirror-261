import sqlite3 as sql

class Database():

    def __init__(self, path:str) -> None:
        """
        Creates the link to the database, 
        and will act as if it was the database
        """
        self.cnx = None
        try:
            self.cnx = sql.connect(path)
        except sql.Error as e:
            print(e)
        finally:
            if self.cnx:
                self.path = path
                self.cnx.close()
            else:
                del self


    def CreateTable(self, tableName:str, *columns:tuple):
        """
        Creates table called tableName with columns in columns.
        Each arg is a tuple and represent a column, apart from first wich is the tableName string.
        First arg of one column tuple is column name, second is type, the rest are optional sql specifics like AUTO INCREMENT or PRiMARY KEY or NOT NULL ...
        """
        self.__Connect__()
        try:#                                      |   transform culumn tuple to line of names                 |   |does it for every tuple  |   | removes parenthesises on side and others |
            command = f"CREATE TABLE {tableName} ({f"{[f"{self.__list_to_sql_str__(columns[i]).replace(",", "")}" for i in range(len(columns))]}"[1:-2].replace("'", "").replace('"', "")});"
            self.cnx.execute(command)
            self.cnx.commit()
        except sql.Error as e:
            print(e)
        finally:
            self.__Disconnect__()    

    
    def AddLine(self, tableName:str, *values:tuple) -> None:
        """
        Adds values to table tableName
        """
        self.__Connect__()
        try:
            command = f"INSERT INTO {tableName} VALUES {self.__list_to_sql_str__(values)};"
            self.cnx.execute(command)
            self.cnx.commit()
        except sql.Error as e:
            print(e)
        finally:
            self.__Disconnect__()


    def Select(self, columns:tuple=("*"), tableName:str="", ANDConditions:dict={}, ORConditions:dict={}, orderBy:tuple=("", "ASC"), customWHEREStatement:str="") -> list:
            """
            Requests to database.
            """        
            assert tableName != ""

            self.__Connect__()

            try: # if statement is empty (ex: customWHEREStatement, we multiply its part by False to remove it)
                command = f"Select {self.__list_to_sql_str__(columns)} FROM {tableName} " + \
                                        f"WHERE {self.__dict_to_sql_condition_str__("AND", **ANDConditions)} {self.__dict_to_sql_condition_str__("OR ", **ORConditions)}" * (customWHEREStatement == "") + \
                                        customWHEREStatement + \
                                        f"ORDER BY {orderBy[0]} {orderBy[1]}" * (orderBy[0] != "")+ ";"
                
                return self.cnx.execute(command).fetchall()
                #TODO add recursive call support
            except sql.Error as e:
                print(e)
            finally:
                self.__Disconnect__()


    def __list_to_sql_str__(self, *tuple):
        """
        Transforms array of values to string on values separated by ',', and each value is between " ' "  
        """
        # keeps ' and ,
        return f"{[tuple[i] for i in range(len(tuple))]}"[1:-1]#.replace("'", "")
    
    def __dict_to_sql_condition_str__(self, keyword:str, **dico):
        """
        Transforms dico to string with format: "key = value keyword" and we do it for each line of dico
        keyword is either "AND" or "OR"
        last keyword is deleted from string on return
        """
        conditionList = [ f"{key} = {f"{[value]}"[1:-1]} {keyword} " for key, value in dico.items()]
        command = ""
        for condition in conditionList:
            command += condition

        return command[:-5]
    
    def __del__(self):
        print(f"Database connection destroyed, database is still in files at: {self.path}")

    def __Connect__(self):
        self.cnx = sql.connect(self.path)

    def __Disconnect__(self):
        self.cnx.close()
        self.cnx = None
    

if __name__ == "__main__":

    test = Database("./data/test.db")

    test.CreateTable("hello", ("key","INT", "PRIMARY KEY"), ("blu", "TEXT", "NOT NULL"))

    test.AddLine("hello", (1, "booo"), (2, "cccc"))

    print(test.Select(tableName="hello", ANDConditions={"key":1, "blu":"cccc"}))