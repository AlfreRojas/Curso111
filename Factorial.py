'''
Created on Nov 4, 2017

@author: Federico Javier Dueñas
'''
def mostrarProductos(matriz):
    for i in range(0, len(matriz[0])):
        print(str(i)+"-> "+matriz[0][i]+" = $"+str(matriz[1][i]));
        
nombre = "Juan";
t1 = 20;
t2 = 5;
a = "Hola"+" "+nombre+", tenes "+str((t1 + t2))+" años tabajando"
print(a);
productos = [["Yerba", "Azucar", "Leche", "Pan"], [70, 15, 25, 26]];

mostrarProductos(productos);

ticket = [[], [], []];

termina = 'no';

while termina == 'no':
    mostrarProductos(productos);
    codigo = input("ingresar codigo de articulo ");
    cantidad = input("ingresar cantidad de articulo ");
    ticket[0] .append(int(cantidad));
    ticket[1] .append(productos[0][int(codigo)]);
    ticket[2] .append(int(cantidad)* productos[1][int(codigo)]);
    termina = input("termina? si/no");

print(ticket);