class Menu:
    opcion=None
    def __init__(self):
        self.__opcion=0
    def mostrarmenu(self,objetomanejador):
        while self.__opcion!=-1:
            print('1')
            print('2')
            print('3')
            print('4')
            self.__opcion=input('Ingrese numero: ')
            if self.__opcion=='1':
                objetomanejador.Actualizar()
            if self.__opcion=='2':
                objetomanejador.ImporteCuota()
            if self.__opcion=='3':
                objetomanejador.MostrarMonto()
            if self.__opcion=='4':
                objetomanejador.ModificarCuotas()
