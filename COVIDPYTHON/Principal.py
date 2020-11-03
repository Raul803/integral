from importData import importData
from DataPlot import DataPlot
import geopandas as gpd
from DataPlot import grafMapa
from DataPlot import grafMapaBog
import os

class principal():

    def __init__(self):#constructor de clase
        self.dataplot=DataPlot()#Creación de objeto tipo 'DataPlot'


    def importarDesde(self, path, sheet, tipo):#Función que importa los datos desde un path
        self.importar=importData(path)#Creación de Objeto tipo 'importData'
        Data=self.importar.getDataframe(sheet)#Obtener el dataframe de los datos importado
        return Data

    def importarDesdeBog(self, path, sheet, tipo):#Función que importa los datos desde un path
        self.importarBog=importData(path)#Creación de Objeto tipo 'importData'
        Data=self.importarBog.getDataframe(sheet)#Obtener el dataframe de los datos importado
        return Data

    def getListValorTotal(self, listData, col):#Función que obtiene la lista de valores acumulados
            try:
                    self.dataplot.getValorTotal(listData, col)#del objeto 'DataPlot' llamar la función que tomar el valor total de la suma de datos
                    return self.dataplot.getListTotal()#del objeto 'DataPlot' llamarla función que devuelve la lista acumulada
            except:
                    print()
                          

    def cargarGEODEP(self,name):#Función que permite la carga de los archivos tipo GeoJSon
        self.map_data = gpd.read_file(name)#Lectura del archivo
        self.DepartamentosPlot=grafMapa(self.map_data)#Creación de dataframe desde los datos de mapa

    
    def cargarGEOLOC(self,name):#Función que permite la carga de los archivos tipo GeoJSon
        self.map_dataBog = gpd.read_file(name)#Lectura del archivo
        self.DepartamentosPlotBog=grafMapaBog(self.map_dataBog)#Creación de dataframe desde los datos de mapa
    
    def setDatosCol(self, nameData, fecha, tipo, Column):#Asignación de datos al dataframe de mapa
        filenamesc = os.listdir('Datos/')#Toma de nombres desde la carpeta Datos

        for i in filenamesc:#Para cada nombre extraído
                        pathc='Datos/'+i;

                        Data=self.importarDesde(pathc, nameData, fecha)#Importar datos desde el path
                        if Data.empty==False:#Si el dataframe no esta vacío
                                if tipo==3:#Para datos tipo 3 (fecha,tipo,cantidad)
                                    try:
                                            #Esta explicación esta en el archivo GUIDE en la función de gráfica
                                            ListImportado=self.getListfrom('New Field','Importado',Data)
                                            ListImportadoT=self.getListValorTotal(ListImportado, 0)
                                            ListImportado=self.replaceColumnDF(ListImportado,ListImportadoT,1)
                                            ListImportado.columns=['Estado', 'Importado']
                                            
                                            ListEnEstudio=self.getListfrom('New Field','En estudio',Data)
                                            ListEnEstudioT=self.getListValorTotal(ListEnEstudio, 0)
                                            ListEnEstudio=self.replaceColumnDF(ListEnEstudio,ListEnEstudioT,1)
                                            ListEnEstudio.columns=['Estado', 'En Estudio']
                                            
                                            ListRelacionado=self.getListfrom('New Field','Relacionado',Data)
                                            ListRelacionadoT=self.getListValorTotal(ListRelacionado, 0)
                                            ListRelacionado=self.replaceColumnDF(ListRelacionado,ListRelacionadoT,1)
                                            ListRelacionado.columns=['Estado', 'Relacionado']
                                            
                                            if Column=='Importado':#Según el dato escogido en el combobox de variable de los datos
                                                    maxVal=self.dataplot.getValorTotal(ListImportado,0)#Se toma el valor total de la sumatoria de los datos
                                                    self.DepartamentosPlot.setCantidad(i.split('.')[0],maxVal)#Se asigna el valor a la columna del mapa 
                                            elif Column=='En estudio':
                                                    maxVal=self.dataplot.getValorTotal(ListEnEstudio,0)
                                                    self.DepartamentosPlot.setCantidad(i.split('.')[0],maxVal)
                                            elif Column=='Relacionado':
                                                    maxVal=self.dataplot.getValorTotal(ListEnEstudio,0)
                                                    self.DepartamentosPlot.setCantidad(i.split('.')[0],maxVal)
                                    except:
                                            continue
                              
                                elif tipo==4 or tipo==5:#Para tipos 4 y 5
                                        try:
                                                maxVal=Data.loc[Column,'Record Count']# se toma la columna 'Record Count' para calcular el valor máximo
                                                self.DepartamentosPlot.setCantidad(i.split('.')[0],maxVal)#Se asigna valor máximo a columna
                                        except:
                                                continue
                                else:#Para los demás tipos

                                    maxVal=self.dataplot.getValorTotal(Data,0)
                                    self.DepartamentosPlot.setCantidad(i.split('.')[0],maxVal)   
                                    
        return self.DepartamentosPlot.getGrafDep()
            
    def setDatosBog(self, nameData, fecha, tipo, Column):#Asignación de datos al dataframe de mapa
                filenamesc = os.listdir('Bogota/')#Toma de nombres desde la carpeta Datos
        
                for i in filenamesc:#Para cada nombre extraído
                                pathc='Bogota/'+i;
                                #print(pathc)
        
                                Data=self.importarDesde(pathc, nameData, fecha)#Importar datos desde el path
                                if Data.empty==False:#Si el dataframe no esta vacío
                                        if tipo==3:#Para datos tipo 3 (fecha,tipo,cantidad)
                                            try:
                                                    #Esta explicación esta en el archivo GUIDE en la función de gráfica
                                                    ListImportado=self.getListfrom('New Field','Importado',Data)
                                                    ListImportadoT=self.getListValorTotal(ListImportado, 0)
                                                    ListImportado=self.replaceColumnDF(ListImportado,ListImportadoT,1)
                                                    ListImportado.columns=['Estado', 'Importado']
                                                    
                                                    ListEnEstudio=self.getListfrom('New Field','En estudio',Data)
                                                    ListEnEstudioT=self.getListValorTotal(ListEnEstudio, 0)
                                                    ListEnEstudio=self.replaceColumnDF(ListEnEstudio,ListEnEstudioT,1)
                                                    ListEnEstudio.columns=['Estado', 'En Estudio']
                                                    
                                                    ListRelacionado=self.getListfrom('New Field','Relacionado',Data)
                                                    ListRelacionadoT=self.getListValorTotal(ListRelacionado, 0)
                                                    ListRelacionado=self.replaceColumnDF(ListRelacionado,ListRelacionadoT,1)
                                                    ListRelacionado.columns=['Estado', 'Relacionado']
                                                    
                                                    if Column=='Importado':#Según el dato escogido en el combobox de variable de los datos
                                                            maxVal=self.dataplot.getValorTotal(ListImportado,0)#Se toma el valor total de la sumatoria de los datos
                                                            self.DepartamentosPlotBog.setCantidad(i.split('.')[0],maxVal)#Se asigna el valor a la columna del mapa 
                                                    elif Column=='En estudio':
                                                            maxVal=self.dataplot.getValorTotal(ListEnEstudio,0)
                                                            self.DepartamentosPlotBog.setCantidad(i.split('.')[0],maxVal)
                                                    elif Column=='Relacionado':
                                                            maxVal=self.dataplot.getValorTotal(ListEnEstudio,0)
                                                            self.DepartamentosPlotBog.setCantidad(i.split('.')[0],maxVal)
                                            except:
                                                    continue
                                      
                                        elif tipo==4 or tipo==5:#Para tipos 4 y 5
                                                try:
                                                        maxVal=Data.loc[Column,'Record Count']# se toma la columna 'Record Count' para calcular el valor máximo
                                                        self.DepartamentosPlotBog.setCantidad(i.split('.')[0],maxVal)#Se asigna valor máximo a columna
                                                except:
                                                        continue
                                        else:#Para los demás tipos
        
                                            maxVal=self.dataplot.getValorTotal(Data,0)
                                            self.DepartamentosPlotBog.setCantidad(i.split('.')[0],maxVal)   
                                            
                return self.DepartamentosPlotBog.getGrafDep()

    def getListfrom(self, column, tipo, df):#tomar datos de una columa en específico desde un data frame df
            return self.importar.getListfrom(column, tipo, df)
    
    def getListfromBog(self, column, tipo, df):#tomar datos de una columa en específico desde un data frame df
            return self.importarBog.getListfrom(column, tipo, df)
    
    def replaceColumnDF(self, df, dataColumn, numColumn):#Reemplazar columna por datos nuevos.
            for i in range(len(df)):
                    df.iloc[i,numColumn]=dataColumn[i]
            return df
                   
            
            
        
