import numpy as np

class DataPlot:

    def __init__(self):
        self.ListTotal=[]
        
    def getValorTotal(self,df, column):#Obtener el valor total de la sumatoria de valores de la columna del data frame df
        self.ListTotal=[]
        self.ListTotal=[df.iloc[0, column]]#Asignar el primer valor del dataframe a la nueva lista
        suma=df.iloc[0, column];#Ininiar la variable que acumula las sumas
        for i in range(1,len(df)):#Recorrido del dataframe
            suma+=df.iloc[i,column]#Aumento de la variable suma
            self.ListTotal.append(suma)#Asifnación a la lista de valores de acumulación

        return suma


    def getListTotal(self):#Retorna la lista de valores acumulados
        return self.ListTotal
            
class grafMapa:#Clase para el mapa 

  def __init__(self, geoInfo):#constructor
    self.Geo=geoInfo
    self.Geo['DATAinfo']=np.zeros(len(geoInfo.loc[:, 'dpt'])).tolist();#Inicialziación de nla nueva columnda del dataframe de mapa


  def setCantidad(self, nameDep, cant):#Asignación de datos a la nueva columna (Se sobreescribe según el dato a graficar)
    for i in range(len(self.Geo.loc[:,'dpt'])):

      if self.Geo.loc[i,'dpt'] == nameDep:#Para los departamentos con el mismo nombre que nameDep
                 
              self.Geo.loc[i,'DATAinfo']=cant#Asignar la cantidad dada
 
  def getGrafDep(self):#Obtener el dataframe de mapa actualizado
          return self.Geo


class grafMapaBog:#Clase para el mapa 

  def __init__(self, geoInfo):#constructor
    self.Geo=geoInfo
    # is_tipo = geoInfo.loc[:, 'Nombre de la localidad'] != 'SUMAPAZ'
    # self.Geo = geoInfo.loc[is_tipo]
    # print(self.Geo.head())
    self.Geo['DATAinfo']=np.zeros(len(self.Geo.loc[:, 'Nombre de la localidad'])).tolist();#Inicialziación de nla nueva columnda del dataframe de mapa


  def setCantidad(self, nameDep, cant):#Asignación de datos a la nueva columna (Se sobreescribe según el dato a graficar)
    for i in range(len(self.Geo.loc[:,'Nombre de la localidad'])):

      if self.Geo.loc[i,'Nombre de la localidad'] == nameDep:#Para los departamentos con el mismo nombre que nameDep
                 
              self.Geo.loc[i,'DATAinfo']=cant#Asignar la cantidad dada
 
  def getGrafDep(self):#Obtener el dataframe de mapa actualizado
          return self.Geo
  
  


            
