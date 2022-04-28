from ModuloMenu import Menu
from ManejadorPlanes import ManejadorPlanes
if __name__=='__main__':
    ObjMenu=Menu()
    ObjManejador=ManejadorPlanes()
    ObjMenu.mostrarmenu(ObjManejador)