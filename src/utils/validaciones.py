import re
def validate_photo(photo):
    if not photo:
        print("Error: La URL de la foto no puede estar vacía.")
        return False
    return True
def validate_nombre(nombre):
       
    if not re.match("^[a-zA-Z\s]+$", nombre):
        print("Error: El nombre solo puede contener letras y espacios.")
        return False
    return True
    
def validate_email(email):
    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        print("Error: Formato de correo electrónico inválido.")
        return False
    return True
    
def validate_description(description):
    if len(description) < 5:
        print("Error: La descripción debe tener al menos 5 letras.")
        return False
    elif len(description) > 255:
        print("Error: La descripción no puede tener más de 255 letras.")
        return False
    return True
    
def validate_contact(contact):
    if not re.match("^\d{9,12}$", contact):
        print("Error: El número de contacto debe tener entre 9 y 12 dígitos.")
        return False
    return True


def validate_room_number(room_number):
    if not re.match(r'^[1-9]\d{0,2}$', room_number) or not (1 <= int(room_number) <= 999):
        print("Error: El número de habitación debe estar entre 001 y 999.")
        return False
    return True

def validate_rate(rate):
    try:
        rate_float = float(rate)
        if rate_float < 20.00:
            print("Error: El valor de la tarifa debe ser igual o mayor a 20.00.")
            return False
        elif rate_float != round(rate_float, 2):
            print("Error: La tarifa debe tener siempre dos decimales.")
            return False
        return True
    except ValueError:
        print("Error: Ingresa un número válido para la tarifa.")
        return False