class PlanAhorro:
    __codplan=''
    __modelo=''
    __vehiversion=''
    __valorvehiculo=''
    __cantcuotas=''
    __cantcuotaslic=''
    def __init__(self,codplan,modelo,vehiversion,cantcuotas,cantcuotaslic):
        self.__codplan=codplan
        self.__modelo=modelo
        self.__vehiversion=vehiversion
        self.__cantcuotas=cantcuotas
        self.__cantcuotaslic=cantcuotaslic
    def getCodigo(self):
        return self.__codplan
    def getModelo(self):
        return self.__modelo
    def getVersion(self):
        return self.__vehiversion
    def getvalorvehiculo(self):
        return self.__valorvehiculo
    def getCantCuotas(self):
        return self.__cantcuotas
    def getCantCuotaslic(self):
        return self.__cantcuotaslic
    def guardarvar(self,act):
        self.__valorvehiculo=act