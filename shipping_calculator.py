def calculate_shipping_cost(weight, distance):
    """
    Calcula el costo de envío basado en el peso (kg) y la distancia (km).
    Fórmula simple para ejemplo: costo base + costo por kg + costo por km.
    """
    base_cost = 5.00  # Costo fijo
    cost_per_kg = 1.20
    cost_per_km = 0.05

    total_cost = base_cost + (cost_per_kg * weight) + (cost_per_km * distance)
    return round(total_cost, 2)

def estimate_delivery_time(distance):
    """
    Estima el tiempo de entrega (en días) basado en la distancia.
    Supongamos velocidad promedio de 500 km/día.
    """
    speed_per_day = 500
    days = distance / speed_per_day
    return round(days)

if __name__ == "__main__":
    print("=== Shipping Calculator ===")
    weight = float(input("Ingrese el peso del paquete (kg): "))
    distance = float(input("Ingrese la distancia del envío (km): "))

    cost = calculate_shipping_cost(weight, distance)
    days = estimate_delivery_time(distance)

    print(f"Costo estimado: ${cost}")
    print(f"Tiempo estimado de entrega: {days} días")
