import ctypes
SHERB_NOCONFIRMATION = 0x00000001
SHERB_NOPROGRESSUI = 0x00000002
SHERB_NOSOUND = 0x00000004
try:
    resultado = ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, SHERB_NOCONFIRMATION | SHERB_NOPROGRESSUI | SHERB_NOSOUND)   
    if resultado == 0:
        print("Se vació la papelera correctamente.")
    else:
        print(f"No se vació correctamente. Codigo: {resultado}")
except Exception as e:
    print(f"Error inesperado: {e}")