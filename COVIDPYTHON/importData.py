import pandas as pd

class importData():

    def __init__(self, name):
        self.name=name#path del archivo a importar
        self.data=None

    def getDataframe(self, sheet):#Tomar un data frame del path del archivo
       #print()
       self.data=pd.read_excel(self.name, index_col=0, sheet_name=sheet)
       return self.data


    def getListfrom(self, column, tipo, df):#Crear una lista desde una columna seleccionada de un dataframe df

       is_tipo = df.loc[:, column] == tipo
       newList = df.loc[is_tipo]

       return newList


        
        
        
