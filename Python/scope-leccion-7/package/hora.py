from datetime import datetime as dt


def ir_a_casa():
    hour = dt.now().hour
    minute = dt.now().minute
    if hour > 19 and minute > 0:
        return print("Son más de las 7! A volver a casa")
    else:
        hour_r = 19 - hour
        minute_r = 60 - minute
        return print(f"Faltan {hour_r} horas y {minute_r} minutos de trabajo")
