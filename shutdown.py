import os
shutdown = input('Quieres apagar el pc? (si / no): ').lower()
if shutdown.lower() == 'si':
    os.system('shutdown /s /t 1')
else:
    exit()
