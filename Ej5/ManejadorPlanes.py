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
        valor=float(input('Ingrese un valor: '))
        for i in range(len(self.__lista)):
            valorcuota=(self.__lista[i].getvalorvehiculo/self.__lista[i].getCantCuotas)+self.__lista[i].getvalorvehiculo* 0.10
            if valor>valorcuota:
                print('\nCodigo del plan: ',self.__lista[i].getCodigo())
                print('\nModelo: ',self.__lista[i].getModelo())
                print('\nVersion del vehiculo: ',self.__lista[i].getVersion())
    def MostrarMonto(self,valorcuota):
        for i in range(len(self.__lista)):
            monto=self.__lista[i].getCantCuotaslic*valorcuota
            print('Monto que se debe pagar para licitar el vehiculo: ',monto)
    def ModificarCuotas(self):
        cod=int(input('\nIngrese un codigo de plan: '))
        for i in range(len(self.__lista)):
            mod=input('Ingrese cantidad de cuotas a modificar: ')
            self.__lista[cod-1].getCantCuotaslic=mod
