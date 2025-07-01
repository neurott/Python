import os

shutdown = input('Quieres apagar el pc? (Si / no): ')

if shutdown.lower() == 'si':
    os.system('shutdown /s /t 1')
else:
    exit()