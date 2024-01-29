class MiExcepcion():
    def __init__(self, err):
        print(f'Wep, cometiste el siguiente error: {err}')

try:
    raise ZeroDivisionError('Que error loco! division por cero no se puede man!')
except:
    print('No pods cometer un error tan básico! LoL')

raise ZeroDivisionError('Que error loco! division por cero no se puede man!')
