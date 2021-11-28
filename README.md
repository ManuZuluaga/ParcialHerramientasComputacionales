## ParcialHerramientasComputacionales
### Descuento en las cafeterías

1. #### Problema   
Las cafeterías están dando un descuento del 20% a los profesores y del 50% de los estudiantes.
Para realizar esto se debe preguntar el **número de cédula**, si es **profesor o estudiante**, el **código
del producto**, las **unidades a llevar** y el **precio**. A partir de esta información se calcula lo que se
debe pagar, incluyendo el descuento. 

2. #### Modelo Computacional  
Para resolver el problema se realizó un modelo computacional, que pide los **datos al usuario** y calcula el **precio total a pagar**.  
 - Para realizar esto se desarrolló un código que recibe como entrada el **número de cédula**, el **rol** (si es estudiante
o profesor), el **código de producto**, la **cantidad** y el **precio**. 
- Como salida se imprime un **texto** donde dice si es profesor o estudiante, el número de cédula,  el **precio total** a pagar incluyendo
el descuento y el código del producto. 

3. #### ¿Como se realizó?  
Para esto se le piden los datos de entrada al usuario, por consola, y en el rol, la cantidad de productos y el precio, se le
agrega un _try except_, para que si se ingresa un valor inesperado, salga un mensaje que diga que que el valor no es válido y se
vuelve a pedir. Después de esto se calcula el total a pagar y dependiendo si es profesor o estudiante se le hace el descuento 
correspondiente, para que finalmente se imprima un pequeño texto diciendo el rol de la persona, la cédula, el producto a llevar
y lo que se debe pagar. Para calcular el valor a total a pagar, se calcula un valor total, multiplicando el número de productos
por el precio y despues dependiendo si es profesor o estudiante se multiplica este valor total inicial por 0.8, en caso de los 
profesores, ya que tendrian que pagar el 80% del valor total y por 0.5 el el caso de los estudiantes, pues tendiran que pagar 
el 50%. Además, se le pregunta al usuario si va a agregar a otra persona que va a comprar en la cafeteria o si ya no se desea 
agregar a nadie más, esto mediante un _while_ que ternima cuando el usuario ingresa "2", que es el codigo para acabar esta repetición.    

La implementación en Python puede verse en el archivo:  _“descuento_cafeterias.py”_
