from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app, Counter
from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, REGISTRY
import time
import random

    #environment: 
     # - "TZ=Europe/Madrid"

# Create my app
app = Flask(__name__)

# Add prometheus wsgi middleware to route /metrics requests
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

ropajes = dict(Zara = 0, Primark = 0, Pull = 0, Mango = 0)
tecno = dict(Mediamarkt = 0, Xiaomi = 0, Samsung = 0)
entretenimiento = dict(Game = 0, Poly = 0, Juguetos = 0)
chiquitiendas = dict(TeaShop = 0, Animales = 0, PeluqueriaCalvos = 0)

hora_actual = time.localtime()[3] + 2
# Usamos una variable para cambiar la zona horaria.
# hora_actual = hora_actual + 2

class GenteTotal(object):
    def collect(self):
        if 0 <= hora_actual <= 9:
            value = 6
        elif 9 <= hora_actual <= 11:
            value = random.randrange(60, 150)
        elif 11 <= hora_actual <= 12:
            value = random.randrange(150, 200)
        elif 12 <= hora_actual <= 14:
            value = random.randrange(200, 300)
        elif 14 <= hora_actual <= 16:
            value = random.randrange(500, 700)
        elif 16 <= hora_actual <= 19:
            value = random.randrange(400, 600)
        elif 19 <= hora_actual <= 24:
            value = random.randrange(800, 1250)
    
        yield GaugeMetricFamily('gente_total', 'Nº de personas en el CC', value = value)

class ParkingOcupado(object):
    def collect(self):
        if 0 <= hora_actual <= 9:
            value = 3
        elif 9 <= hora_actual <= 11:
            value = random.randrange(40, 90)
        elif 11 <= hora_actual <= 12:
            value = random.randrange(75, 125)
        elif 12 <= hora_actual <= 14:
            value = random.randrange(100, 160)
        elif 14 <= hora_actual <= 16:
            value = random.randrange(100, 200)
        elif 16 <= hora_actual <= 19:
            value = random.randrange(200, 350)
        elif 19 <= hora_actual <= 24:
            value = random.randrange(500, 800)
    
        yield GaugeMetricFamily('parking_ocupado', 'Nº de coches en el parking del CC', value = value)

class SectorTecnologia(object):
    def collect(self):
        if 9 <= hora_actual <= 11:
            value = random.randrange(1, 2)
        elif 11 <= hora_actual <= 14:
            value = random.randrange(1, 5) 
        elif 14 <= hora_actual <= 16:
            value = random.randrange(1, 7) 
        elif 16 <= hora_actual <= 19:
            value = random.randrange(1, 5) 
        elif 19 <= hora_actual <= 0:
            value = random.randrange(2, 10)
        
        if 0 <= hora_actual <= 9:
            tecno['Mediamarkt'] = 0
            tecno['Xiaomi'] = 0
            tecno['Samsung'] = 0
        else:    
            tecno['Mediamarkt'] = value + random.randint(5, 10)
            tecno['Xiaomi'] = value + random.randint(0, 5)
            tecno['Samsung'] = value

        gm = GaugeMetricFamily('Sector_tecnologia', 'Tiendas de Tecnología', labels = ['tecno'])
        gm.add_metric(['Mediamarkt'], tecno['Mediamarkt'])
        gm.add_metric(['Xiaomi'], tecno['Xiaomi'])
        gm.add_metric(['Samsung'], tecno['Samsung'])

        yield gm
        
        
class SectorRopa(object):
    def collect(self):
        if 9 <= hora_actual <= 11:
            value = random.randrange(2, 6)
        elif 11 <= hora_actual <= 14:
            value = random.randrange(1, 10)
        elif 14 <= hora_actual <= 16:
            value = random.randrange(3, 11) 
        elif 16 <= hora_actual <= 19:
            value = random.randrange(1, 10) 
        elif 19 <= hora_actual <= 0:
            value = random.randrange(3, 12) 
        
        if 0 <= hora_actual <= 9:
            ropajes['Zara'] = 0
            ropajes['Primark'] = 0 
            ropajes['Pull'] = 0
            ropajes['Mango'] = 0
        else:
            ropajes['Zara'] = value + random.randint(1, 10)
            ropajes['Primark'] = value + random.randint(1, 15)
            ropajes['Pull'] = value + random.randint(0, 7)
            ropajes['Mango'] = value + random.randint(0, 5)
        
        gm = GaugeMetricFamily('Sector_ropa', 'Tiendas de ropa', labels = ['ropajes'])
        gm.add_metric(['Zara'], ropajes['Zara'])
        gm.add_metric(['Primark'], ropajes['Primark'])
        gm.add_metric(['Pull'],  ropajes['Pull'])
        gm.add_metric(['Mango'], ropajes['Mango'])

        yield gm   
        
        
class SectorEntretenimiento(object):
    def collect(self):
        if 9 <= hora_actual <= 11:
            value = random.randrange(2, 6)
        elif 11 <= hora_actual <= 14:
            value = random.randrange(1, 10)
        elif 14 <= hora_actual <= 16:
            value = random.randrange(5, 15) 
        elif 16 <= hora_actual <= 19:
            value = random.randrange(1, 10) 
        elif 19 <= hora_actual <= 0:
            value = random.randrange(5, 15) 
        
        if 0 <= hora_actual <= 9:
            entretenimiento['Game'] = 0
            entretenimiento['Poly'] = 0
            entretenimiento['Juguetos'] = 0
        else:
            entretenimiento['Game'] = value + random.randint(0, 4)
            entretenimiento['Poly'] = value + random.randint(2, 6)
            entretenimiento['Juguetos'] = value + random.randint(1, 3)

        gm = GaugeMetricFamily('Sector_entretenimiento', 'Tiendas de entretenimiento', labels = ['entretenimiento'])
        gm.add_metric(['Game'], entretenimiento['Game'])
        gm.add_metric(['Poly'], entretenimiento['Poly'])
        gm.add_metric(['Juguetos'],  entretenimiento['Juguetos'])

        yield gm     
        
class ChiquiTiendas(object):
    def collect(self):
        if 0 <= hora_actual <= 9:
            value = 0
        elif 9 <= hora_actual <= 11:
            value = random.randrange(0, 1)
        elif 11 <= hora_actual <= 14:
            value = random.randrange(0, 2)
        elif 14 <= hora_actual <= 16:
            value = random.randrange(1, 3)
        elif 16 <= hora_actual <= 19:
            value = random.randrange(0, 3)
        elif 19 <= hora_actual <= 0:
            value = random.randrange(1, 4)
        
        if 0 <= hora_actual <= 9:
            chiquitiendas['TeaShop'] = 0
            chiquitiendas['Animales'] = 0
            chiquitiendas['PeluqueriaCalvos'] = 0
        else:
            chiquitiendas['TeaShop'] = value + random.randint(0, 1)
            chiquitiendas['Animales'] = value + random.randint(0, 2)
            chiquitiendas['PeluqueriaCalvos'] = value + random.randint(0, 1)
        

        gm = GaugeMetricFamily('Chiquitiendas', 'Tiendas pequeñicas', labels = ['chiquitiendas'])
        gm.add_metric(['TeaShop'], chiquitiendas['TeaShop'])
        gm.add_metric(['Animales'], chiquitiendas['Animales'])
        gm.add_metric(['PeluqueriaCalvos'],  chiquitiendas['PeluqueriaCalvos'])
        
        yield gm     
        
REGISTRY.register(GenteTotal())
REGISTRY.register(ParkingOcupado())
REGISTRY.register(SectorTecnologia())
REGISTRY.register(SectorRopa())
REGISTRY.register(SectorEntretenimiento())
REGISTRY.register(ChiquiTiendas())
