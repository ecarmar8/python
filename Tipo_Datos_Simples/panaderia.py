pan_actual = 100
pan_anterior = pan_actual * 0.4  # 60% de descuento, paga solo el 40%

nombre = str(input("Introduce tu nombre: "))
cantidad_vendida = int(input("Introduce la cantidad de panes vendidos: "))
tipo_pan = bool(input("El tipo de pan es fresco? (s/n): ").strip().lower())
if tipo_pan == "s":
    total_venta = pan_actual * cantidad_vendida
else:
    total_venta = pan_anterior * cantidad_vendida
print(nombre, "El total de la venta es: ", round(total_venta, 2))