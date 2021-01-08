from wtforms import Form
from wtforms import DecimalField, IntegerField, StringField, FieldList, TextField, SelectField, DateField


class CambioMoneda(Form):
    Moneda_a_Cambiar = DecimalField('Moneda a Cambiar')
    #tipo_cambio_moneda = IntegerField('Tipo Cambio Moneda')
    tipo_cambio_moneda = SelectField('Seleccione el tipo de moneda',choices = [
        ('Euro'), ('Dolar'), ('Yen'), ('Libra')
    ])

class IngresoPostIt(Form):
    dia = IntegerField('Día')
    mes = IntegerField('Mes')
    year = IntegerField('Año')
    recordatorio = StringField('Recordatorio')

class IngresoContacto(Form):
    nombre = StringField('Nombre contacto')
    apellido = StringField('Apellido contacto')
    correo = StringField('Correo electrónico Contacto')
    telefono = IntegerField('Teléfono Contacto')
