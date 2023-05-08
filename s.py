import datetime

fecha_inicio = datetime.datetime.now().date()
mañana = fecha_inicio + datetime.timedelta(days=30)
print(mañana)
print(type(fecha_inicio))
print(fecha_inicio)