precio = input("Introduce el precio del producto con dos decimales: ")
print(precio[:precio.find('.')], 'pesos y', precio[precio.find('.')+1:], 'centavos.')