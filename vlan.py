def verificar_vlan():
    try:
        vlan = int(input("Ingrese el número de VLAN: "))

        if 1 <= vlan <= 1005:
            print(f"La VLAN {vlan} pertenece al rango normal.")
        elif 1006 <= vlan <= 4094:
            print(f"La VLAN {vlan} pertenece al rango extendido.")
        else:
            print("El número de VLAN ingresado no es válido. Debe estar entre 1 y 4094.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    verificar_vlan()