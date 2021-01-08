from flask import Flask, render_template, request
from zeep import Client, Settings
import forms
import csv

wsdl = 'http://localhost:8000/?wsdl'
settings = Settings(strict = True, xml_huge_tree = True)
rpc_client = Client(wsdl = wsdl, settings = settings)

app = Flask(__name__)

#main page
@app.route('/')
def hello_word():
    return render_template('index.html')

#say_hello_examble page
@app.route('/service1', methods = ['GET','POST'])
def service1():
    cambio_moneda = forms.CambioMoneda(request.form)
    data = 0
    if request.method == 'POST':
        data = rpc_client.service.moneda_cambio(cambio_moneda.Moneda_a_Cambiar.data, cambio_moneda.tipo_cambio_moneda.data)
    return render_template('services/cambio_moneda.html', form = cambio_moneda, data = data)

#contact page
@app.route('/service2', methods = ['GET','POST'])
def service2():
    contacto = forms.IngresoContacto(request.form)
    data = None
    if request.method == 'POST':
        data = rpc_client.service.ingreso_contacto(contacto.nombre.data, contacto.apellido.data, contacto.correo.data, contacto.telefono.data)
    return render_template('services/contact.html', form = contacto, data = data)

#post-it page
@app.route('/service3', methods = ['GET', 'POST'])
def service3():
    fecha = forms.IngresoPostIt(request.form)
    data = None
    if request.method == 'POST':
        data = rpc_client.service.ingreso_recordatorio(fecha.dia.data, fecha.mes.data, fecha.year.data, fecha.recordatorio.data)
    return render_template('services/post_it.html', form = fecha, data = data)

#List contact page
@app.route('/service4', methods =['GET','POST'])
def service4():
    data = []
    if request.method == 'GET':
        data = rpc_client.service.listar_contactos()
        data2 = []
        for value in data:
            data2.append(value.split(sep=','))
    return render_template('services/listar_contacto.html', data = data2)

#List post it page
@app.route('/service5', methods =['GET','POST'])
def service5():
    data = []
    if request.method == 'GET':
        data = rpc_client.service.listar_recordatorios()
        data2 = []
        for value in data:
            data2.append(value.split(sep=','))
    return render_template('services/listar_recordatorios.html', data = data2)


if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
