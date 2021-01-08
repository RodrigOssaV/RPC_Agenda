from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode, Double, Array
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import csv

#Implementación de los servicios
class RPCService(ServiceBase):
    #Acá van (TODOS) los servicios de agenda

    #Servicio de Intercambio de Moneda
    @rpc(Double, Unicode, _returns = Double)
    def moneda_cambio(ctx, moneda, opcion):
        resultado_final = 0
        if opcion == 'Euro':
            resultado_final = moneda*(0.0011)
        elif opcion == 'Dolar':
            resultado_final = moneda*(0.0013)
        elif opcion == 'Yen':
            resultado_final = moneda*(0.14)
        else:
            #opcion = 'libra'
            resultado_final = moneda*(0.00099)
        return resultado_final

    #Servicio Ingreso Contactos
    @rpc(Unicode, Unicode, Unicode, Integer, _returns = Unicode)
    def ingreso_contacto(ctx, nombre, apellido, correo, telefono):
        myData = [[nombre, apellido, correo, telefono]]
        myFile = open('contactos.csv','a')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(myData)
            results = "Éxito"
        return results

    #Servicio Listar contactos
    @rpc(_returns = Iterable(Unicode))
    def listar_contactos(ctx):
        contacto = []
        with open('contactos.csv') as File:
            reader = csv.DictReader(File)
            for row in reader:
                #result = str(row)
                result = row['Nombre']+','+row['Apellido']+','+row['Correo']+','+row['telefono']
                yield result

    #Servicio Ingreso Recordatorio
    @rpc(Integer, Integer, Integer, Unicode, _returns = Unicode)
    def ingreso_recordatorio(ctx, dia, mes, year, recordatorio):
        myData = [[dia, mes, year, recordatorio]]
        myFile = open('recordatorio.csv','a')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(myData)
            results = "Éxito"
        return results

    #Servicio Listar recordatorio
    @rpc( _returns = Iterable(Unicode))
    def listar_recordatorios(ctx):
        recordatorio = []
        with open('recordatorio.csv') as File:
            reader = csv.DictReader(File)
            for row in reader:
                result = row['Dia']+','+row['Mes']+','+row['Anho']+','+row['Recordatorio']
                yield result

#Ejemplar de aplicacition indicando los protocolos de entrada
application = Application([RPCService],'spyne.examples.hello.soap',
                            in_protocol = Soap11(validator = 'lxml'),
                            out_protocol = Soap11())
#Servidor para modo debug
wsgi_application = WsgiApplication(application)
#Parámetros de inicio de la aplicacion
if __name__ == '__main__':
    import logging
    from wsgiref.simple_server import make_server
    logging.basicConfig(level = logging.DEBUG)
    server = make_server('127.0.0.1', 8000, wsgi_application)
    server.serve_forever()
