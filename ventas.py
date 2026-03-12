import matplotlib.pyplot as plt

dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
ventas = [120, 85, 150, 200, 170]

plt.bar(dias, ventas, color='blue')

#personalizar el gráfico
plt.title('Ventas Semanales')
plt.xlabel('Días de la Semana')
plt.ylabel('Cantidad de productos vendidos')

#mostrar el gráfico
plt.show()

