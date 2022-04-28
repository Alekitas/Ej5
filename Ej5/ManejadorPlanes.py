from ClasePlanes import PlanAhorro
import csv
class ManejadorPlanes:
    __lista=[]
    def __init__(self):
        self.iniciar()
        
    def iniciar(self):
        archivo=open('planes.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            vehiculo=PlanAhorro(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.__lista.append(vehiculo)
    def Actualizar(self):
        for i in range(len(self.__lista)):
            print('\nCodigo de plan: {}',self.__lista[i].getCodigo())
            print('\nModelo: ',self.__lista[i].getModelo())
            print('\nVersion del vehiculo: {}',self.__lista[i].getVersion())
            act=input('Ingrese nuevo valor del vehiculo: ')
            self.__lista[i].guardarvar(act)
    def ImporteCuota(self):
        pass