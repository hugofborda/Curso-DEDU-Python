from .tarjeta import Tarjeta
from utilidades.archivos import existe_archivo, eliminar_archivo
import json

class Usuario():
    """ Clase que define un usuario de tarjetas de crédito """
    def __init__(self, nombre = None) -> None:
       self.__nombre = nombre
       self.__tarjetas = []
    
    @property
    def nombre(self) :
        """ Obtiene nombre de usuario """
        return self.__nombre

    @property
    def nombre_archivo(self) :
        """ Obtiene nombre de usuario """
        return self.__nombre.replace(" ","_")+"_tarjeta.json"
  
    @property
    def tarjetas(self) :
        """ Propiedad de listas de tarjetas """
        return self.__tarjetas

    @property
    def dict(self):
        """ Propiedad diccionario del objeto usuario"""
        dict = {}
        dict["nombre"] = self.nombre
        dict["tarjetas"] = []
        for tarjeta in self.tarjetas :
            dict["tarjetas"].append(tarjeta.dict)
        return dict

    def asignar_nombre(self,nombre) :
        """ Asignar nombre """
        self.__nombre = nombre
    
    def asigna_de_dict(self,usuario_dict) :
        self.asignar_nombre = usuario_dict["nombre"]

    def __agregar_tarjeta(self,tarjeta) :
        """ Agrega una nueva tarjeta """
        self.__tarjetas.append(tarjeta)
        self.guardar_json()
    
    def __eliminar_tarjeta(self, tarjeta_eliminar) :
        """ Eliminar una tarjeta """
        for tarjeta in self.__tarjetas :
            if tarjeta_eliminar.strip().lower() == tarjeta.obtener_nombre().strip().lower() :
                self.__tarjetas.remove(tarjeta)
                self.guardar_json()
                return True
        return False
                
    def imprimir_tarjetas(self) :
        for tarjeta in self.__tarjetas :
            tarjeta.generar_reporte()

    def eliminar_tarjeta(self) :
        """ Eliminar una tarjeta solicitada por entrada estándar"""
        tarjeta_eliminar :str = input("Digite el nombre de la tarjeta a eliminar: ")
        if self.__eliminar_tarjeta(tarjeta_eliminar):
            print(f"La tarjeta :{tarjeta_eliminar} ha sido eliminada.")
        else :
            print(f" No fue posible eliminar la tarjeta: {tarjeta_eliminar}, no se encuentra en el listado de tarjetas.")

    def eliminar_ultima_tarjeta(self) :
        tarjeta_eliminar = self.__tarjetas[-1].obtener_nombre()
        self.__tarjetas.pop()
        print("#"*50 +" Tarjeta eliminada "+ "#"*50)
        print(f"La tarjeta: {tarjeta_eliminar}, ha sido eliminada.")
        print("#"*50 +" Tarjeta eliminada "+ "#"*50)

    def agregar_tarjeta(self) :
        """ Agrega una nueva tarjeta """
        tarjeta = Tarjeta()
        tarjeta.capturar_tarjeta()
        self.__agregar_tarjeta(tarjeta)
    
    def agregar_tarjeta_flask(self,tarjeta) :
        """ Agrega una nueva tarjeta """
        self.__agregar_tarjeta(tarjeta)
    
    def eliminar_tarjeta_flask(self,tarjeta) :
        """ Elimina una tarjeta del usuario """
        self.__eliminar_tarjeta(tarjeta)    

    def guardar_json(self) :
        """
        Guarda la información del usuario en un archivo json
        """
        datos_dicts =[self.dict]

        with open(self.nombre_archivo,"w") as arch_salida :
            json.dump(datos_dicts,arch_salida,indent = 4)
   
    def eliminar_json(self) :
        """
        Eliminar archivo json
        """
        eliminar_archivo(self.nombre_archivo)

    def asigna_json_a_usuario(self,archivo_entrada) :
        """ asigna los datos de un arhivo json y los asigna al objeto usuario """        
        with open(archivo_entrada,"r") as arch_entrada :
            usuarios_json = json.load(arch_entrada)
            for usuario_json in usuarios_json :
                self.decode_json(usuario_json)
    
    def existe(self) :
        """ asigna los datos de un arhivo json y los asigna al objeto usuario """        
        return existe_archivo(self.nombre_archivo)

    def decode_json(self,usuario_json) :
        """ Pasa los datos de un json la objeto usuario"""
        self.asignar_nombre(usuario_json["nombre"])
        for tarjeta_json in usuario_json["tarjetas"] :
            tarjeta = Tarjeta()
            tarjeta.decode_json(tarjeta_json)
            self.tarjetas.append(tarjeta)
            
