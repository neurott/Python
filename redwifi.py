import subprocess

perfil_red = input('Introduce el nombre del perfil de red WIFI: ')
try: 
    resultados = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', perfil_red, 'key=clear'],
                                         shell=True).decode('utf-8', errors='backslashreplace')  
    if 'Contenido de la clave' in resultados:
        for line in resultados.split('\n'):
            if 'Contenido de la clave' in line:
                password = line.split(':')[1].strip()
                print(f'La contraseña de la red {perfil_red} es: {password}')
                break
    else:
        print(f'No se pudo encontrar la contraseña para la red {perfil_red}')
except subprocess.CalledProcessError:
    print(f'No se pudo obtener la información del perfil: {perfil_red}')