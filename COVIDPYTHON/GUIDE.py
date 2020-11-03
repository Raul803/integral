from tkinter import ttk
from tkinter import Tk
import os
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Principal import principal
import numpy as np


class DatosCovid(ttk.Frame):# Clase de tipo ttk.Frame

    def __init__(self, mainWindow):
        super().__init__(mainWindow)#constructor de padre tkk.Frame
        mainWindow.title("Datos COVID")#Titulo de la ventana principal
        mainWindow.configure(width=1000, height=700)#Tamaño de la ventana principal
        self.place(relwidth=1, relheight=1)#Ubicación del frame en la ventana principal
        self.ruta_completa = os.getcwd()#Ruta de la ubicación de la carpeta de proyecto
        self.Proces=principal()#Creación de objeto de clase "Principal"


    def setComboDep(self, listDep):#Creación de un Combobox para la selección de departamentos
        self.lblDep = ttk.Label(self, text="Selección de Visualización")#Creación de label
        self.lblDep.place(x=10, y=22)#Ubicación
        self.comboDep = ttk.Combobox(self)#Creación de Combobox
        self.comboDep['values']= listDep#Valores de la lista del combobox
        self.comboDep.current(0) #Asignación del valor por defecto
        self.comboDep.place(x=10, y=40)#Ubicación de combobox
        
    def setComboBog(self, listDep):#Creación de un Combobox para la selección de departamentos
        self.lblBog = ttk.Label(self, text="Selección de Visualización")#Creación de label
        self.lblBog.place(x=10, y=382)#Ubicación
        self.comboBog = ttk.Combobox(self)#Creación de Combobox
        self.comboBog['values']= listDep#Valores de la lista del combobox
        self.comboBog.current(0) #Asignación del valor por defecto
        self.comboBog.place(x=10, y=400)#Ubicación de combobox


    def setComboDatos(self):#Creación de un combobox para la selección de datos a visualizar
        self.lblDatos = ttk.Label(self, text="Selección de Datos")
        self.lblDatos.place(x=200, y=22)
        self.comboDat = ttk.Combobox(self)
        self.comboDat['values']= ('CasosD', 'MuertesD', 'EstadoP', 'AtencionP', 'TipoContagio', 'EdadVsGenero', 'EstadoVsGenero', 'AtencionVsEdad', 'EstadoVsAtencion')
        self.comboDat.current(0) #set the selected item
        self.comboDat.place(x=200, y=40)
        
    def setComboDatosBog(self):#Creación de un combobox para la selección de datos a visualizar
        self.lblDatosBog = ttk.Label(self, text="Selección de Datos")
        self.lblDatosBog.place(x=200, y=382)
        self.comboDatBog = ttk.Combobox(self)
        self.comboDatBog['values']= ('CasosD', 'MuertesD', 'EstadoP', 'AtencionP', 'TipoContagio', 'EdadVsGenero', 'EstadoVsGenero', 'AtencionVsEdad', 'EstadoVsAtencion')
        self.comboDatBog.current(0) #set the selected item
        self.comboDatBog.place(x=200, y=400)
        
    def setComboTipoDatos(self, datos):#Creación de combobox para la selección de opciones de datos (Depende del caso 
    #- si los datos no tienen opciones se asignan los casos Diarios Colombia)
        self.lblDatost = ttk.Label(self, text="Tipo de dato")
        self.lblDatost.place(x=650, y=22)
        self.comboDatt = ttk.Combobox(self)
        self.comboDatt['values']= datos;
        self.comboDatt.current(0) #set the selected item
        self.comboDatt.place(x=650, y=40)
        
    def setComboTipoDatosBog(self, datos):#Creación de combobox para la selección de opciones de datos (Depende del caso 
    #- si los datos no tienen opciones se asignan los casos Diarios Bogotá)
        self.lblDatostBog = ttk.Label(self, text="Tipo de dato")
        self.lblDatostBog.place(x=650, y=382)
        self.comboDattBog = ttk.Combobox(self)
        self.comboDattBog['values']= datos;
        self.comboDattBog.current(0) #set the selected item
        self.comboDattBog.place(x=650, y=400)
        

    def setPlotDatosDep(self, tipo, dfDep):#Graficación de los datos
        figure1 = plt.Figure(figsize=(10,5),dpi=55)#Creación de un figure con tamaño figsize y un dpi(Pocentaje de proporción de tamaño)
        ax1 = figure1.add_subplot(111)#Asignación de subplot a la figure, el subplot se almacena en ax1
        bar1 = FigureCanvasTkAgg(figure1, self)#Asignación de figure al frame actual
        bar1.get_tk_widget().place(x=10, y=80)#Ubicación del elemento agregado al frame

        if(tipo==1 or tipo==2 ):#Para los datos tipo 1 y 2 (Fecha y cantidad)
                try:#Protección de errores de falta de datos para visualziar
                        dfDep.plot(kind='line', legend=True, ax=ax1)#Graficar los datos de forma lineal en el ax1
                        ax1.grid(color='grey', ls = '-.', lw = 0.15)#Asignación de cuadrícula de cierto color, tipo de línea y grosor.
                        if tipo==1:
                                ax1.set_title('Número de Casos a nivel nacional')#titulo para caso 1
                        else:
                                ax1.set_title('Número de Fallecidos a nivel nacional') #titulo para caso 2
                        ax1.set_xlabel('Fecha', fontsize=10)#Asignación de nombre de axesX
                        ax1.set_ylabel('# Casos', fontsize=10)#asignación de nombre de axesY
                        ax1.legend(loc=2)#Ubicación de los tag de la gráfica (Esquina superior izquierda)
                        
                except:
                        print()
                
        elif tipo==3:#Para los datos tipo 3 (fecha, tipo, cantidad)

                ListImportado=self.Proces.getListfrom('New Field','Importado',dfDep)#Del objeto tipo "Principal" usar la funcion getListfrom 
                #(tomar ciertos datos de un Datframe - Explicación en clase "Principal")
                ListImportadoT=self.Proces.getListValorTotal(ListImportado, 1)#Del Objeto tipo "Principal" usar la funcion getListValorTotal
                #(tomar la sumatoria de los datos en el tiempo)
                ListImportado=self.Proces.replaceColumnDF(ListImportado,ListImportadoT,1)#Del objeto tipo "Principal" usar la funcion replaceColumnDF
                #(Remplazar una columna de un data frame por la columna de otro dataframe)
                ListImportado.columns=['Estado', 'Importado']#Asignación de columnas al data frame final
                
                ListEnEstudio=self.Proces.getListfrom('New Field','En estudio',dfDep)
                ListEnEstudioT=self.Proces.getListValorTotal(ListEnEstudio, 1)
                ListEnEstudio=self.Proces.replaceColumnDF(ListEnEstudio,ListEnEstudioT,1)
                ListEnEstudio.columns=['Estado', 'En Estudio']
                
                ListRelacionado=self.Proces.getListfrom('New Field','Relacionado',dfDep)
                ListRelacionadoT=self.Proces.getListValorTotal(ListRelacionado, 1)
                ListRelacionado=self.Proces.replaceColumnDF(ListRelacionado,ListRelacionadoT,1)
                ListRelacionado.columns=['Estado', 'Relacionado']
                
                try:#Protección contra falta de datos
                        ListImportado.plot(kind='line', ax=ax1, label='Importado')#Gráficar el data frame en formato línea bajo un label
                        
                        ListEnEstudio.plot(kind='line', ax=ax1, label='En Estudio')
                        
                        ListRelacionado.plot(kind='line', ax=ax1, label='Relacionado')
                        
                        ax1.grid(color='grey', ls = '-.', lw = 0.15)
                        ax1.set_title('Tipo de Contagio')
                        ax1.set_xlabel('Fecha', fontsize=10)
                        ax1.set_ylabel('# Casos', fontsize=10)
                        ax1.legend(loc=2)
                        
                except:
                        print()
                
        elif tipo==4 or tipo==5:#Para tipo 4 y 5 (tipo, cantidad)
                try: #Protección contra falta de datos
                        dfDep.plot(kind='pie', subplots=True, ax=ax1, fontsize=8)#Graficar el dataframe en formato Pie(Torta de porcentajes)
                        if tipo==4:
                                ax1.set_title('Estado de Pacientes')#Titulo para caso 4
                        else:
                                ax1.set_title('Atención de Pacientes')#Titulo para caso 5
                        ax1.set_ylabel('', fontsize=10)
                        ax1.legend(loc=1)
                except:
                        print()
                
        elif tipo==6 or tipo==7:#Para caso 6 o 7 (tipo, sexo, cantidad)
                
                M=self.Proces.getListfrom('Sexo','M',dfDep)#Del objeto tipo "Principal" usar la funcion getListfrom 
                #(tomar ciertos datos de un Datframe - Explicación en clase "Principal")
                F=self.Proces.getListfrom('Sexo','F',dfDep)
                
                large=0;
                if len(M)>len(F):#De acuerdo a cual de los dos dataframe es más largo se almacena en large el largo
                        large=len(M)
                else:
                        large=len(F)
                
                
                dataBar=[]
                index_=[]
                for i in range(large):#Para el largo escogido
                        dataV=[]
                        try:#Protección contra falta de datos
                                dataV.append(M.iloc[i,1])#Adición de elemento a la lista dataV
                                index_=M.index.values#Se escogen los index de la lista en curso
                        except: 
                                dataV.append(0)#Si no hay datos dentro del data frame se asigna un 0 a la lista
                        try:
                                dataV.append(F.iloc[i,1])
                                index_=F.index.values
                        except: 
                                dataV.append(0)
                                                                
                        dataBar.append(dataV)#Adición de los datos referentes a M y F de la lsita dataV, a la lsita dataBar
                                
           
                try:#Protección conrta falta de datos
                        dfBar=DataFrame(data=dataBar, columns=['M','F'], index=index_)#Creación de data frame para gráfica
                        #print(dfBar)
                        
                        dfBar[['M', 'F']].plot(kind="bar", stacked=True, ax=ax1)#Gráfica de los datos en formato Barras con visualización agrupada
                
                        ax1.grid(color='grey', ls = '-.', lw = 0.15)
                        if tipo==6:
                                ax1.set_title('Edad Vs Género')#titulo para caso 6
                        else:
                                ax1.set_title('Estado Vs Género')#titulo para caso 7
                        ax1.set_xlabel('Fecha', fontsize=10)
                        ax1.set_ylabel('# Casos', fontsize=10)
                        ax1.legend(loc=2)
                        
                except:
                        print()                                

                
                #df=Dataframe(dfDep)
                
                
        elif tipo==8 or tipo==9:#Para datos tipo 8 o 9 (tipo tipo, cantidad)
                
                #Crear dataframes desde la extracción de datos específicos del dataframe principal
                Casa=self.Proces.getListfrom('Atención','Casa',dfDep)
                Recuperado=self.Proces.getListfrom('Atención','Recuperado',dfDep)
                Hospital=self.Proces.getListfrom('Atención','Hospital',dfDep)
                HospitalUCI=self.Proces.getListfrom('Atención','Hospital UCI',dfDep)
                Fallecidos=self.Proces.getListfrom('Atención','Fallecido',dfDep)
                
                #Creación de lista de los largos de cada lsita anterior
                dataLen=[len(Casa), len(Recuperado), len(Hospital), len(HospitalUCI), len(Fallecidos)]
                maxLen=np.amax(dataLen)#Tomar el valor máz grande de la lista de largos
                pos=dataLen.index(maxLen)#buscar en que posición se encuentra el valor más grande
                #print(pos)
               
                #Según la lista de mayor largo se asigna a un dataframe temporal de referencia
                dfTemp=[]
                if pos==0:
                        dfTemp=Casa
                elif pos ==1:
                        dfTemp=Recuperado
                elif pos ==2:
                        dfTemp=Hospital
                elif pos==3:
                        dfTemp=HospitalUCI
                elif pos==4:
                        dfTemp=Fallecidos
                
                dataBar=[]
                for i in range(maxLen):#Para cada dato según el largo escogido
                        dataV=[]

                        for x in range(len(Casa)):#Para el caso del dataframe de tipo "CASA"

                                if dfTemp.index.values[i] == Casa.index.values[x]:#si el index del dataframe de referencia es el mismo del data frame evaluado (CASA)
                                        dat=Casa.iloc[x,1] #Asignar el valor de casa a la variable dat y romper el for
                                        break
                                else:# si no coinciden los index 
                                        dat=0#asignar a dat=0 hasta que se encuentre coincidencia o termine el for
                        dataV.append(dat)#Asignar el valor de dat a la lista dataV
                        
                        #Se repite el proceso para los otros tipos de datos
                        for x in range(len(Recuperado)):
                                
                                if dfTemp.index.values[i] == Recuperado.index.values[x]:
                                        dat=Recuperado.iloc[x,1]
                                        break
                                else:
                                        dat=0
                        dataV.append(dat)

                        for x in range(len(Hospital)):
                                
                                if dfTemp.index.values[i] == Hospital.index.values[x]:
                                        dat=Hospital.iloc[x,1]
                                        break
                                else:
                                        dat=0
                        dataV.append(dat)

                        for x in range(len(HospitalUCI)):
                                
                                if dfTemp.index.values[i] == HospitalUCI.index.values[x]:
                                        dat=HospitalUCI.iloc[x,1]
                                        break
                                else:
                                        dat=0
                        dataV.append(dat)

                        for x in range(len(Fallecidos)):
                                
                                if dfTemp.index.values[i] == Fallecidos.index.values[x]:
                                        dat=Fallecidos.iloc[x,1]
                                        break
                                else:
                                        dat=0
                        dataV.append(dat)


                        dataBar.append(dataV)#Asignar a databar los valores de la lsita dataV
                try:#Protección contra falta de datos
                        #Creación de data frame final para graficar
                        dfBar=DataFrame(data=dataBar, columns=['Casa','Recuperado', 'Hospital', 'Hospital UCI','Fallecido'], index=dfTemp.index.values)

                        #Gráfica de los datos en formato Barras con visualización agrupada
                        dfBar[['Casa','Recuperado', 'Hospital', 'Hospital UCI','Fallecido']].plot(kind="bar", stacked=True, ax=ax1)
                        
                        ax1.grid(color='grey', ls = '-.', lw = 0.15)
                        if tipo==8:
                                ax1.set_title('Estado Vs Edad')#titulo para caso 8
                        else:
                                ax1.set_title('Estado Vs Atención')#titulo para caso 9
                        ax1.set_xlabel('Fecha', fontsize=10)
                        ax1.set_ylabel('# Casos', fontsize=10)
                        ax1.legend(loc=2)
                except:
                        print()
                        
    def setPlotDatosLocal(self, tipo, dfDep):#Graficación de los datos
           figure1 = plt.Figure(figsize=(10,5),dpi=55)#Creación de un figure con tamaño figsize y un dpi(Pocentaje de proporción de tamaño)
           ax1 = figure1.add_subplot(111)#Asignación de subplot a la figure, el subplot se almacena en ax1
           bar1 = FigureCanvasTkAgg(figure1, self)#Asignación de figure al frame actual
           bar1.get_tk_widget().place(x=10, y=430)#Ubicación del elemento agregado al frame
           print(tipo)
           if(tipo==1 or tipo==2 ):#Para los datos tipo 1 y 2 (Fecha y cantidad)
                   try:#Protección de errores de falta de datos para visualziar
                           dfDep.plot(kind='line', legend=True, ax=ax1)#Graficar los datos de forma lineal en el ax1
                           ax1.grid(color='grey', ls = '-.', lw = 0.15)#Asignación de cuadrícula de cierto color, tipo de línea y grosor.
                           if tipo==1:
                                   ax1.set_title('Número de Casos en Bogotá')#titulo para caso 1
                           else:
                                   ax1.set_title('Número de Fallecidos en Bogotá') #titulo para caso 2
                           ax1.set_xlabel('Fecha', fontsize=10)#Asignación de nombre de axesX
                           ax1.set_ylabel('# Casos', fontsize=10)#asignación de nombre de axesY
                           ax1.legend(loc=2)#Ubicación de los tag de la gráfica (Esquina superior izquierda)
                           
                   except:
                           print()
                   
           elif tipo==3:#Para los datos tipo 3 (fecha, tipo, cantidad)
   
                   ListImportado=self.Proces.getListfromBog('New Field','Importado',dfDep)#Del objeto tipo "Principal" usar la funcion getListfrom 
                   #(tomar ciertos datos de un Datframe - Explicación en clase "Principal")
                   ListImportadoT=self.Proces.getListValorTotal(ListImportado, 1)#Del Objeto tipo "Principal" usar la funcion getListValorTotal
                   #(tomar la sumatoria de los datos en el tiempo)
                   ListImportado=self.Proces.replaceColumnDF(ListImportado,ListImportadoT,1)#Del objeto tipo "Principal" usar la funcion replaceColumnDF
                   #(Remplazar una columna de un data frame por la columna de otro dataframe)
                   ListImportado.columns=['Estado', 'Importado']#Asignación de columnas al data frame final
                   
                   ListEnEstudio=self.Proces.getListfromBog('New Field','En estudio',dfDep)
                   ListEnEstudioT=self.Proces.getListValorTotal(ListEnEstudio, 1)
                   ListEnEstudio=self.Proces.replaceColumnDF(ListEnEstudio,ListEnEstudioT,1)
                   ListEnEstudio.columns=['Estado', 'En Estudio']
                   
                   ListRelacionado=self.Proces.getListfromBog('New Field','Relacionado',dfDep)
                   ListRelacionadoT=self.Proces.getListValorTotal(ListRelacionado, 1)
                   ListRelacionado=self.Proces.replaceColumnDF(ListRelacionado,ListRelacionadoT,1)
                   ListRelacionado.columns=['Estado', 'Relacionado']
                   
                   try:#Protección contra falta de datos
                           ListImportado.plot(kind='line', ax=ax1, label='Importado')#Gráficar el data frame en formato línea bajo un label
                           
                           ListEnEstudio.plot(kind='line', ax=ax1, label='En Estudio')
                           
                           ListRelacionado.plot(kind='line', ax=ax1, label='Relacionado')
                           
                           ax1.grid(color='grey', ls = '-.', lw = 0.15)
                           ax1.set_title('Tipo de Contagio')
                           ax1.set_xlabel('Fecha', fontsize=10)
                           ax1.set_ylabel('# Casos', fontsize=10)
                           ax1.legend(loc=2)
                           
                   except:
                           print()
                   
           elif tipo==4 or tipo==5:#Para tipo 4 y 5 (tipo, cantidad)
                   try: #Protección contra falta de datos
                           dfDep.plot(kind='pie', subplots=True, ax=ax1, fontsize=8)#Graficar el dataframe en formato Pie(Torta de porcentajes)
                           if tipo==4:
                                   ax1.set_title('Estado de Pacientes')#Titulo para caso 4
                           else:
                                   ax1.set_title('Atención de Pacientes')#Titulo para caso 5
                           ax1.set_ylabel('', fontsize=10)
                           ax1.legend(loc=1)
                   except:
                           print()
                   
           elif tipo==6 or tipo==7:#Para caso 6 o 7 (tipo, sexo, cantidad)
                   
                   M=self.Proces.getListfrom('Sexo','M',dfDep)#Del objeto tipo "Principal" usar la funcion getListfrom 
                   #(tomar ciertos datos de un Datframe - Explicación en clase "Principal")
                   F=self.Proces.getListfrom('Sexo','F',dfDep)
                   
                   large=0;
                   if len(M)>len(F):#De acuerdo a cual de los dos dataframe es más largo se almacena en large el largo
                           large=len(M)
                   else:
                           large=len(F)
                   
                   
                   dataBar=[]
                   index_=[]
                   for i in range(large):#Para el largo escogido
                           dataV=[]
                           try:#Protección contra falta de datos
                                   dataV.append(M.iloc[i,1])#Adición de elemento a la lista dataV
                                   index_=M.index.values#Se escogen los index de la lista en curso
                           except: 
                                   dataV.append(0)#Si no hay datos dentro del data frame se asigna un 0 a la lista
                           try:
                                   dataV.append(F.iloc[i,1])
                                   index_=F.index.values
                           except: 
                                   dataV.append(0)
                                                                   
                           dataBar.append(dataV)#Adición de los datos referentes a M y F de la lsita dataV, a la lsita dataBar
                                   
              
                   try:#Protección conrta falta de datos
                           dfBar=DataFrame(data=dataBar, columns=['M','F'], index=index_)#Creación de data frame para gráfica
                           #print(dfBar)
                           
                           dfBar[['M', 'F']].plot(kind="bar", stacked=True, ax=ax1)#Gráfica de los datos en formato Barras con visualización agrupada
                   
                           ax1.grid(color='grey', ls = '-.', lw = 0.15)
                           if tipo==6:
                                   ax1.set_title('Edad Vs Género')#titulo para caso 6
                           else:
                                   ax1.set_title('Estado Vs Género')#titulo para caso 7
                           ax1.set_xlabel('Fecha', fontsize=10)
                           ax1.set_ylabel('# Casos', fontsize=10)
                           ax1.legend(loc=2)
                           
                   except:
                           print()                                
   
                   
                   #df=Dataframe(dfDep)
                   
                   
           elif tipo==8 or tipo==9:#Para datos tipo 8 o 9 (tipo tipo, cantidad)
                   
                   #Crear dataframes desde la extracción de datos específicos del dataframe principal
                   Casa=self.Proces.getListfrom('Atención','Casa',dfDep)
                   Recuperado=self.Proces.getListfrom('Atención','Recuperado',dfDep)
                   Hospital=self.Proces.getListfrom('Atención','Hospital',dfDep)
                   HospitalUCI=self.Proces.getListfrom('Atención','Hospital UCI',dfDep)
                   Fallecidos=self.Proces.getListfrom('Atención','Fallecido',dfDep)
                   
                   #Creación de lista de los largos de cada lsita anterior
                   dataLen=[len(Casa), len(Recuperado), len(Hospital), len(HospitalUCI), len(Fallecidos)]
                   maxLen=np.amax(dataLen)#Tomar el valor máz grande de la lista de largos
                   pos=dataLen.index(maxLen)#buscar en que posición se encuentra el valor más grande
                   #print(pos)
                  
                   #Según la lista de mayor largo se asigna a un dataframe temporal de referencia
                   dfTemp=[]
                   if pos==0:
                           dfTemp=Casa
                   elif pos ==1:
                           dfTemp=Recuperado
                   elif pos ==2:
                           dfTemp=Hospital
                   elif pos==3:
                           dfTemp=HospitalUCI
                   elif pos==4:
                           dfTemp=Fallecidos
                   
                   dataBar=[]
                   for i in range(maxLen):#Para cada dato según el largo escogido
                           dataV=[]
   
                           for x in range(len(Casa)):#Para el caso del dataframe de tipo "CASA"
   
                                   if dfTemp.index.values[i] == Casa.index.values[x]:#si el index del dataframe de referencia es el mismo del data frame evaluado (CASA)
                                           dat=Casa.iloc[x,1] #Asignar el valor de casa a la variable dat y romper el for
                                           break
                                   else:# si no coinciden los index 
                                           dat=0#asignar a dat=0 hasta que se encuentre coincidencia o termine el for
                           dataV.append(dat)#Asignar el valor de dat a la lista dataV
                           
                           #Se repite el proceso para los otros tipos de datos
                           for x in range(len(Recuperado)):
                                   
                                   if dfTemp.index.values[i] == Recuperado.index.values[x]:
                                           dat=Recuperado.iloc[x,1]
                                           break
                                   else:
                                           dat=0
                           dataV.append(dat)
   
                           for x in range(len(Hospital)):
                                   
                                   if dfTemp.index.values[i] == Hospital.index.values[x]:
                                           dat=Hospital.iloc[x,1]
                                           break
                                   else:
                                           dat=0
                           dataV.append(dat)
   
                           for x in range(len(HospitalUCI)):
                                   
                                   if dfTemp.index.values[i] == HospitalUCI.index.values[x]:
                                           dat=HospitalUCI.iloc[x,1]
                                           break
                                   else:
                                           dat=0
                           dataV.append(dat)
   
                           for x in range(len(Fallecidos)):
                                   
                                   if dfTemp.index.values[i] == Fallecidos.index.values[x]:
                                           dat=Fallecidos.iloc[x,1]
                                           break
                                   else:
                                           dat=0
                           dataV.append(dat)
   
   
                           dataBar.append(dataV)#Asignar a databar los valores de la lsita dataV
                   try:#Protección contra falta de datos
                           #Creación de data frame final para graficar
                           dfBar=DataFrame(data=dataBar, columns=['Casa','Recuperado', 'Hospital', 'Hospital UCI','Fallecido'], index=dfTemp.index.values)
   
                           #Gráfica de los datos en formato Barras con visualización agrupada
                           dfBar[['Casa','Recuperado', 'Hospital', 'Hospital UCI','Fallecido']].plot(kind="bar", stacked=True, ax=ax1)
                           
                           ax1.grid(color='grey', ls = '-.', lw = 0.15)
                           if tipo==8:
                                   ax1.set_title('Estado Vs Edad')#titulo para caso 8
                           else:
                                   ax1.set_title('Estado Vs Atención')#titulo para caso 9
                           ax1.set_xlabel('Fecha', fontsize=10)
                           ax1.set_ylabel('# Casos', fontsize=10)
                           ax1.legend(loc=2)
                   except:
                           print()

    def setPlotMapaDep(self, dfGEO):#Asignación de datos para la gráfica de mapa
  
        figure3 = plt.Figure(figsize=(5,5),dpi=55)#Creación de un figure con tamaño figsize y un dpi(Pocentaje de proporción de tamaño)
        ax3 = figure3.add_subplot(111)#Asignación de subplot a la figure, el subplot se almacena en ax3
        bar3 = FigureCanvasTkAgg(figure3, self)#Asignación de figure al frame actual
        bar3.get_tk_widget().place(x=650, y=65)#Ubicación del elemento agregado al frame
        dfGEO.plot(column='DATAinfo',cmap='afmhot',ax=ax3, zorder=10)#Grafica de datos a partir de formato GeojSon con tipo de colores 'afmhot'  asignación a ax3 y 10 capas de profundidad
        ax3.set_title('Departamentos de Colombia', 
             pad = 10, 
             fontdict={'fontsize':16, 'color': '#4873ab'})#Asignación de titulo de la gráfica
        ax3.set_xlabel('Longitud')
        ax3.set_ylabel('Latitud')
        
    def setPlotMapaLoc(self, dfGEO):#Asignación de datos para la gráfica de mapa
  
        figure3 = plt.Figure(figsize=(5,5),dpi=55)#Creación de un figure con tamaño figsize y un dpi(Pocentaje de proporción de tamaño)
        ax3 = figure3.add_subplot(111)#Asignación de subplot a la figure, el subplot se almacena en ax3
        bar3 = FigureCanvasTkAgg(figure3, self)#Asignación de figure al frame actual
        bar3.get_tk_widget().place(x=650, y=430)#Ubicación del elemento agregado al frame
        dfGEO.plot(column='DATAinfo',cmap='afmhot',ax=ax3, zorder=10)#Grafica de datos a partir de formato GeojSon con tipo de colores 'afmhot'  asignación a ax3 y 10 capas de profundidad
        ax3.set_title('Localidades de Bogotá', 
             pad = 10, 
             fontdict={'fontsize':16, 'color': '#4873ab'})#Asignación de titulo de la gráfica
        ax3.set_xlabel('Longitud')
        ax3.set_ylabel('Latitud')
        

        
    def setBotonGraf(self):#Creación de botón para gráficas los datos escogidos
        self.buttonLocal = ttk.Button(self, text="Graficar Datos Dep.", command=self.clickGraf)#command es apra asignar la función que se activa al hacer click
        self.buttonLocal.place(x=400, y=38)
        
    def setBotonGrafBog(self):#Creación de botón para gráficas los datos escogidos
        self.buttonLocalBog = ttk.Button(self, text="Graficar Datos Loc.", command=self.clickGrafBog)#command es apra asignar la función que se activa al hacer click
        self.buttonLocalBog.place(x=400, y=400)

    def clickGraf(self):#función que se activa con el boton de gráficar datos
            
        self.fileDep=self.ruta_completa+"/Datos/"+self.comboDep.get()+".xlsx";# se toma el path de la carpeta datos a partir de la selección del combbox de departamentos
        #print("Graficar")
        
        if(self.comboDat.get()=='CasosD' or
           self.comboDat.get()=='MuertesD' or
           self.comboDat.get()=='TipoContagio'):#Para los casos 1 2 3
                
            dfDep=self.Proces.importarDesde(self.fileDep,self.comboDat.get(), 'fecha')#Desde el objeto tipo "Principal" usar la función importar desde
            #(Importar desde un path el archivo escogido)
            
            
            if(self.comboDat.get()=='CasosD'):#Según el valor excogido del combobox de tipos de datos a gráficar
                    self.setPlotDatosDep(1, dfDep)#Llamado a la función setPlotDatosDep para graficar los datos dfDep
                    datos=self.Proces.setDatosCol(self.comboDat.get(),'fecha',1,None)
                    app.setComboTipoDatos([''])
            elif(self.comboDat.get()=='MuertesD'):
                    self.setPlotDatosDep(2,dfDep)
                    datos=self.Proces.setDatosCol(self.comboDat.get(),'fecha',2,None)
                    app.setComboTipoDatos([''])
            elif(self.comboDat.get()=='TipoContagio'):              
                    self.setPlotDatosDep(3, dfDep)
                    app.setComboTipoDatos(['Importado','En estudio', 'Relacionado'])#Asignación de opciones del combobox de las variables de datos según el tipo
                    datos=self.Proces.setDatosCol(self.comboDat.get(),'fecha',3,'Importado')#Por medio de la función 'setDatosCol' del objeto "Principal" 
                    #Se asignan los valores al objeto GeoJson para la grafica de mapa
                    
            self.setPlotMapaDep(datos)#Se actualizan los datos en el mapa
            
        else:#Para el resto de casos
                dfDep=self.Proces.importarDesde(self.fileDep,self.comboDat.get(), None)
                
                if(self.comboDat.get()=='EstadoP'):
                    self.setPlotDatosDep(4,dfDep)

                    datosT=dfDep.index.values.tolist()#Se toman los index de los datos importados
                    app.setComboTipoDatos(datosT)#Se envían al combobox de las variales de los tipos de datos
                    datos=self.Proces.setDatosCol(self.comboDat.get(),None,'Leve','Record Count')#Por medio de la función 'setDatosCol' del objeto "Principal" 
                    #Se asignan los valores al objeto GeoJson para la grafica de mapa
                    self.setPlotMapaDep(datos)#Se grafican los datos obtenidos
   
                elif(self.comboDat.get()=='AtencionP'):                   
                    self.setPlotDatosDep(5,dfDep)

                    datosT=dfDep.index.values.tolist()
                    app.setComboTipoDatos(datosT)
                    datos=self.Proces.setDatosCol(self.comboDat.get(),None,'Casa','Record Count')
                    self.setPlotMapaDep(datos)  
                    
                elif(self.comboDat.get()=='EdadVsGenero'): #De este caso en adelante no se actualiza el mapa por el tipo de datos          
                    self.setPlotDatosDep(6,dfDep)#Gráfica de datos 
                    app.setComboTipoDatos([' '])
                    
                elif(self.comboDat.get()=='EstadoVsGenero'):
                    self.setPlotDatosDep(7,dfDep)
                    app.setComboTipoDatos([' '])
                    
                elif(self.comboDat.get()=='AtencionVsEdad'):
                    self.setPlotDatosDep(8,dfDep)
                    app.setComboTipoDatos([' '])
                    
                elif(self.comboDat.get()=='EstadoVsAtencion'):
                    self.setPlotDatosDep(9,dfDep)
                    app.setComboTipoDatos([' '])
                    
                    
    def clickGrafBog(self):#función que se activa con el boton de gráficar datos
            
        self.fileDep=self.ruta_completa+"/Bogota/"+self.comboBog.get()+".xlsx";# se toma el path de la carpeta datos a partir de la selección del combbox de departamentos
        #print("Graficar")
        
        if(self.comboDatBog.get()=='CasosD' or
           self.comboDatBog.get()=='MuertesD' or
           self.comboDatBog.get()=='TipoContagio'):#Para los casos 1 2 3
                
            dfDep=self.Proces.importarDesdeBog(self.fileDep,self.comboDatBog.get(), 'fecha')#Desde el objeto tipo "Principal" usar la función importar desde
            #(Importar desde un path el archivo escogido)
            
            
            if(self.comboDatBog.get()=='CasosD'):#Según el valor excogido del combobox de tipos de datos a gráficar
                    self.setPlotDatosLocal(1, dfDep)#Llamado a la función setPlotDatosDep para graficar los datos dfDep
                    datos=self.Proces.setDatosBog(self.comboDatBog.get(),'fecha',1,None)
                    app.setComboTipoDatosBog([''])
            elif(self.comboDatBog.get()=='MuertesD'):
                    self.setPlotDatosLocal(2,dfDep)
                    datos=self.Proces.setDatosBog(self.comboDatBog.get(),'fecha',2,None)
                    app.setComboTipoDatosBog([''])
            elif(self.comboDatBog.get()=='TipoContagio'):              
                    self.setPlotDatosLocal(3, dfDep)
                    app.setComboTipoDatosBog(['Importado','En estudio', 'Relacionado'])#Asignación de opciones del combobox de las variables de datos según el tipo
                    datos=self.Proces.setDatosBog(self.comboDatBog.get(),'fecha',3,'Importado')#Por medio de la función 'setDatosCol' del objeto "Principal" 
                    #Se asignan los valores al objeto GeoJson para la grafica de mapa
                    
            self.setPlotMapaLoc(datos)#Se actualizan los datos en el mapa
            
        else:#Para el resto de casos
                dfDep=self.Proces.importarDesde(self.fileDep,self.comboDatBog.get(), None)
                
                if(self.comboDatBog.get()=='EstadoP'):
                    self.setPlotDatosLocal(4,dfDep)

                    datosT=dfDep.index.values.tolist()#Se toman los index de los datos importados
                    app.setComboTipoDatosBog(datosT)#Se envían al combobox de las variales de los tipos de datos
                    datos=self.Proces.setDatosBog(self.comboDatBog.get(),None,'Leve','Record Count')#Por medio de la función 'setDatosCol' del objeto "Principal" 
                    #Se asignan los valores al objeto GeoJson para la grafica de mapa
                    self.setPlotMapaLoc(datos)#Se grafican los datos obtenidos
   
                elif(self.comboDatBog.get()=='AtencionP'):                   
                    self.setPlotDatosLocal(5,dfDep)

                    datosT=dfDep.index.values.tolist()
                    app.setComboTipoDatosBog(datosT)
                    datos=self.Proces.setDatosBog(self.comboDatBog.get(),None,'Casa','Record Count')
                    self.setPlotMapaLoc(datos)  
                    
                elif(self.comboDatBog.get()=='EdadVsGenero'): #De este caso en adelante no se actualiza el mapa por el tipo de datos          
                    self.setPlotDatosLocal(6,dfDep)#Gráfica de datos 
                    app.setComboTipoDatosBog([' '])
                    
                elif(self.comboDatBog.get()=='EstadoVsGenero'):
                    self.setPlotDatosLocal(7,dfDep)
                    app.setComboTipoDatosBog([' '])
                    
                elif(self.comboDatBog.get()=='AtencionVsEdad'):
                    self.setPlotDatosLocal(8,dfDep)
                    app.setComboTipoDatosBog([' '])
                    
                elif(self.comboDatBog.get()=='EstadoVsAtencion'):
                    self.setPlotDatosLocal(9,dfDep)
                    app.setComboTipoDatosBog([' '])                
                    
    def setBotonGrafMap(self):#Creación de boton para actualizar los datos gráficados en el mapa
        self.buttonDep = ttk.Button(self, text="Actualizar Mapa/Tipo.", command=self.clickBotonGrafMap)
        self.buttonDep.place(x=800, y=38)  
        
    def setBotonGrafMapBog(self):#Creación de boton para actualizar los datos gráficados en el mapa
        self.buttonDep = ttk.Button(self, text="Actualizar Mapa/Tipo.", command=self.clickBotonGrafMapBog)
        self.buttonDep.place(x=800, y=398)   
            

    def clickBotonGrafMap(self):#Función que se activa al presionar el boton de actualización de mapa
            
           #Según el tipo de dato escogido desde el combobox se envía por medio de la función 'setdDatosCol' de "Principal" la información 
           #Actualizar del mapa.
            if(self.comboDat.get()=='CasosD'):
                    datos=self.Proces.setDatosCol(self.comboDat.get(),'fecha',1,None)
            elif self.comboDat.get()=='MuertesD':
                    datos=self.Proces.setDatosCol(self.comboDat.get(),'fecha',2,self.comboDatt.get())
            elif self.comboDat.get()=='TipoContagio':
                    datos=self.Proces.setDatosCol(self.comboDat.get(),'fecha',3,self.comboDatt.get())
            elif self.comboDat.get()=='EstadoP':
                    datos=self.Proces.setDatosCol(self.comboDat.get(),None,4,self.comboDatt.get())
            elif self.comboDat.get()=='AtencionP':
                    datos=self.Proces.setDatosCol(self.comboDat.get(),None,5,self.comboDatt.get())       
            elif self.comboDat.get()=='EdadVsGenero':
                    datos=self.Proces.setDatosCol(self.comboDat.get(),None,6,self.comboDatt.get())       
            elif self.comboDat.get()=='EstadoVsGenero':
                    datos=self.Proces.setDatosCol(self.comboDat.get(),None,7,self.comboDatt.get())               
            elif self.comboDat.get()=='AtencionVsEdad':
                    datos=self.Proces.setDatosCol(self.comboDat.get(),None,8,self.comboDatt.get())   
            elif self.comboDat.get()=='EstadoVsAtencion':
                    datos=self.Proces.setDatosCol(self.comboDat.get(),None,9,self.comboDatt.get())  
    
            self.setPlotMapaDep(datos)#Gráficas los datos actualizados
              
    def clickBotonGrafMapBog(self):#Función que se activa al presionar el boton de actualización de mapa
            
           #Según el tipo de dato escogido desde el combobox se envía por medio de la función 'setdDatosCol' de "Principal" la información 
           #Actualizar del mapa.
            if(self.comboDatBog.get()=='CasosD'):
                    datos=self.Proces.setDatosBog(self.comboDatBog.get(),'fecha',1,None)
            elif self.comboDatBog.get()=='MuertesD':
                    datos=self.Proces.setDatosBog(self.comboDatBog.get(),'fecha',2,self.comboDattBog.get())
            elif self.comboDatBog.get()=='TipoContagio':
                    datos=self.Proces.setDatosBog(self.comboDatBog.get(),'fecha',3,self.comboDattBog.get())
            elif self.comboDatBog.get()=='EstadoP':
                    datos=self.Proces.setDatosBog(self.comboDatBog.get(),None,4,self.comboDattBog.get())
            elif self.comboDatBog.get()=='AtencionP':
                    datos=self.Proces.setDatosBog(self.comboDatBog.get(),None,5,self.comboDattBog.get())       
            elif self.comboDatBog.get()=='EdadVsGenero':
                    datos=self.Proces.setDatosBog(self.comboDatBog.get(),None,6,self.comboDattBog.get())       
            elif self.comboDatBog.get()=='EstadoVsGenero':
                    datos=self.Proces.setDatosBog(self.comboDatBog.get(),None,7,self.comboDattBog.get())               
            elif self.comboDatBog.get()=='AtencionVsEdad':
                    datos=self.Proces.setDatosBog(self.comboDatBog.get(),None,8,self.comboDattBog.get())   
            elif self.comboDatBog.get()=='EstadoVsAtencion':
                    datos=self.Proces.setDatosBog(self.comboDatBog.get(),None,9,self.comboDattBog.get())  
    
            self.setPlotMapaLoc(datos)#Gráficas los datos actualizados
            
    def cargaInicial(self):#Función de carga incial - apenas abre la GUIDE
        self.fileDep=self.ruta_completa+"/Datos/Colombia.xlsx";#tomar el path del archivo colombia
        dfDep=self.Proces.importarDesde(self.fileDep,'CasosD', 'fecha')#Importar los datos
        self.setPlotDatosDep(1, dfDep)#Graficar datos
        
        #print(self.ruta_completa+"/colombia-municipios.geojson")
        self.Proces.cargarGEODEP(self.ruta_completa+'/colombia-municipios.geojson')#Carga de datos GeoJSon para la gráfica de mapa
        datos=self.Proces.setDatosCol('CasosD','fecha',1,None)#Asignación de datos al mapa
        self.setPlotMapaDep(datos)#graficación de datos de mapa
        
        filenamesc = os.listdir('Datos/')#Se toman los nombres de los ficheros de la carpeta Datos
        for i in filenamesc:
                if(i!="Colombia.xlsx"):# para todos los ficheros diferentes a 'Colombia'
                        listDep.append(i.split('.')[0])#Asignación a lista 
      
        app.setComboDep( listDep) #Asignación de lista al combobox de departamentos  
        
        
    def cargaInicialBog(self):#Función de carga incial - apenas abre la GUIDE
        self.fileDep=self.ruta_completa+"/Bogota/Bogota.xlsx";#tomar el path del archivo colombia
        dfDep=self.Proces.importarDesdeBog(self.fileDep,'CasosD', 'fecha')#Importar los datos
        self.setPlotDatosLocal(1, dfDep)#Graficar datos
        
        #print(self.ruta_completa+"/colombia-municipios.geojson")
        self.Proces.cargarGEOLOC(self.ruta_completa+'/poligonos-localidades.geojson')#Carga de datos GeoJSon para la gráfica de mapa
        datos=self.Proces.setDatosBog('CasosD','fecha',1,None)#Asignación de datos al mapa
        self.setPlotMapaLoc(datos)#graficación de datos de mapa
        
        filenamesc = os.listdir('Bogota/')#Se toman los nombres de los ficheros de la carpeta Datos
        for i in filenamesc:
                if(i!="Bogota.xlsx"):# para todos los ficheros diferentes a 'Colombia'
                        listLocal.append(i.split('.')[0])#Asignación a lista 
      
        app.setComboBog( listLocal) #Asignación de lista al combobox de departamentos  

      
#Listas inciales
listDep=['Colombia']
listLocal=['Bogota']
df1=[]
datos=['NoTiene']

mainWindow = Tk()#Creación de ventana de GUIDE
app = DatosCovid(mainWindow)#Creación de objeto classe DatosCovid 
#Creación de elementos dentro del frame creado
app.setComboDep(listDep)
app.setComboDatos()
app.setComboBog(listLocal)
app.setComboDatosBog()
app.setComboTipoDatos(datos)
app.setComboTipoDatosBog(datos)
app.setBotonGraf()
app.setBotonGrafMap()
app.setBotonGrafBog()
app.setBotonGrafMapBog()
app.cargaInicial()
app.cargaInicialBog()
app.mainloop()#Necesario para que la ventana se mantenga 


