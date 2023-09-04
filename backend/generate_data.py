import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventario.settings')

import django
django.setup()
from articulos.factories import UserFactory
from sala.factories import SalaFactory
from reserva.factories import ReservaFactory

# Genera 10 instancias de modelo
for i in range(1):
    UserFactory()
    

for i in range(25):
     SalaFactory()
    
    
for i in range(25):
    ReservaFactory()