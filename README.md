# Structure by Python

Calculo estructural.

Indice:

1. DISEÑO DE ZAPATAS AISLADAS / CALCULO DEL ACERO DE REFUERZO

Criterios y fórmulas del estándar estadounidense ACI 318 (referido a las versiones ACI 318-14 / ACI 318-19).




---






## Proyectos

1. diccionario de busqueda de notación de **NORMAS TÉCNICAS
COMPLEMENTARIAS PARA EL DISEÑO Y CONSTRUCCIÓN DE
ESTRUCTURAS DE MAMPOSTERÍA**
2. Script de calculo de **Resistencia a compresión de las piezas**.
    * Comprensión de la norma
    * Creación del script
    * desarrollo de frontend y backend
    * 
3. Calculo de media, mediana y moda


2. Resistencia a comprensión - Script

~~~md
La resistencia en compresión de las piezas es el parámetro más importante del que dependen las propiedades
mecánicas de los muros de mampostería. Por ello se requiere su determinación para fines de control de calidad y
para deducir las otras propiedades cuando no se cuenta con determinaciones directas de las mismas. El valor de
diseño de la resistencia en compresión de las piezas se determina como un valor mínimo probable tomando en
cuenta la variabilidad de la propiedad en cuestión. En función de la media y coeficiente de variación determinados
en los ensayes se calcula, con la fórmula especificada en esta sección, un valor de diseño que corresponde
aproximadamente a una probabilidad de 2% de no ser alcanzado.
~~~

~~~md
La resistencia de diseño se determinará con base en la información estadística existente sobre el producto
o a partir de muestreos de la pieza, ya sea en planta o en obra. Si se opta por el muestreo, se obtendrán, al
menos, tres muestras, cada una de diez piezas, de lotes diferentes de la producción. Las 30 piezas así
obtenidas se ensayarán en laboratorios acreditados por la entidad de acreditación reconocida en los
términos de la Ley Federal sobre Metrología y Normalización. La resistencia de diseño se calculará como:
~~~

$$f'_p = \frac{\bar{f}_p}{1 + 2.5 c_p}$$

donde:

$\bar{f}_p$ resistencia media a compresión de las piezas, referida al área bruta.

$𝑐𝑝$ coeficiente de variación de la resistencia a compresión de las piezas, que en ningún caso será menor que 0.1. En caso de no contar con el número de ensayes requerido, el valor de 𝑐𝑝 no se tomará menor que 0.20 para piezas provenientes de plantas mecanizadas que evidencien un sistema de control de calidad como el requerido en la norma NMX-C-404-ONNCCE, ni que 0.30 para piezas de fabricación mecanizada, pero que no cuenten con un sistema de control de calidad, ni que 0.35 para piezas de producción artesanal. El sistema de control de calidad se refiere a los diversos procedimientos documentados de la línea de producción de interés, incluyendo los ensayes rutinarios y sus registros.

Las resistencias de diseño 𝑓𝑝′y la resistencia media 𝑓𝑝 a compresión de las piezas no deberá ser menor que las indicadas en la tabla 2.1.2.

Tabla 2.1.2 Valores mínimos permitidos de 𝒇𝒑
′
y 𝒇�

| Tipo de pieza y material | 𝑓𝑝′ MPa(kg/cm2) | 𝑓𝑝 MPa(kg/m2) |
|:-|:-:|:-:|
| Tabique macizo de arcilla artesanal | 6 (60) | 9 (90) |
| Tabique macizo o multiperforado de arcilla o de concreto  | 10 (100) | 15 (150) |
| Tabique hueco de arcilla o de concreto | 6 (60) | 9 (90) |
| Bloque macizo o multiperforado de arcilla o de concreto  | 10 (100) | 15 (150) |
| Bloque hueco de arcilla o de concreto | 6 (60) | 9 (90) |



La media (promedio) indica el centro de los datos, mientras que la varianza y la desviación estándar miden cuánto se dispersan respecto a ese centro. La desviación estándar, que es la raíz cuadrada de la varianza, ofrece una medida en las mismas unidades originales. El coeficiente de variación mide la dispersión relativa (%) para comparar conjuntos distintos. 

Media (Promedio): Es la suma de todos los valores dividida por el número total de datos.

Varianza: Promedio de las diferencias al cuadrado entre cada dato y la media. Indica qué tan dispersos están los datos; una varianza alta significa mayor dispersión.

Desviación Estándar: Raíz cuadrada positiva de la varianza. Mide la dispersión promedio en las mismas unidades que los datos originales.

Coeficiente de Variación (CV): Se calcula dividiendo la desviación estándar por la media. Generalmente se expresa en porcentaje y es útil para comparar la variabilidad de conjuntos de datos con diferentes escalas o unidades. 

Diferencias Clave:
Varianza vs. Desviación Estándar: La varianza utiliza unidades al cuadrado, mientras que la desviación estándar utiliza las mismas unidades que los datos, facilitando la interpretación.
Desviación Estándar vs. CV: La desviación estándar mide dispersión absoluta, mientras que el CV es una medida relativa, independiente de la escala de medición.

---

Como experto en ingeniería estructural, te diré que este párrafo es la "columna vertebral" de la filosofía de diseño moderna, específicamente del método de **Diseño por Factores de Carga y Resistencia (LRFD)**, que es el estándar en las Normas Técnicas Complementarias (NTC).

Aquí te desgloso el concepto para que lo domines como un profesional:

---

## 1. El Concepto de "Estados Límite"

Un **estado límite** es una etapa en la que una estructura deja de cumplir su función. Se dividen en dos:

* **Estados Límite de Falla:** Cuando la estructura colapsa (ruptura, pandeo, volcamiento).
* **Estados Límite de Servicio:** Cuando la estructura sigue en pie, pero vibra demasiado, se agrieta o se deforma de forma inaceptable para el usuario.

## 2. La Ecuación de la Seguridad

El texto describe una desigualdad fundamental que debe cumplirse siempre. Matemáticamente, se expresa así:

$$\sum (Q_i \cdot F_C) \leq R_n \cdot F_R$$

Donde:

* **Efecto de las acciones ($Q_i \cdot F_C$):** Son las fuerzas (peso, sismo, viento) multiplicadas por un **Factor de Carga ($F_C$)**. Este factor "infla" las cargas reales para cubrir la incertidumbre de que, en el futuro, las cargas sean mayores a las previstas. Como bien dice el texto, estos factores suelen ser iguales para cualquier material (acero, concreto, madera) porque la incertidumbre viene del exterior (la naturaleza).
* **Resistencia de diseño ($R_n \cdot F_R$):** Es la capacidad de la estructura multiplicada por un **Factor de Reducción ($F_R$)**. Este factor "castiga" la resistencia teórica del material. A diferencia de la carga, este **sí depende del material** y del tipo de falla, porque no es lo mismo la incertidumbre de la calidad del concreto hecho en obra que la del acero hecho en fábrica.

---

## 3. Requisitos Geométricos y de Refuerzo (El "Saber Hacer")

Esta es la parte más interesante del texto. La norma admite que **las matemáticas no lo son todo**.

Aunque el cálculo diga que una columna de 15 cm de ancho soporta el peso, la norma te impondrá un mínimo (digamos, 30 cm) y una cantidad mínima de acero. ¿Por qué?

* **Experiencia histórica:** Se ha observado que estructuras que cumplen con los cálculos pero son muy "esbeltas" o tienen poco refuerzo fallan de forma frágil durante sismos.
* **Ductilidad:** Estos requisitos aseguran que, si la estructura llega a fallar, lo haga lentamente (avisando con grietas) y no de forma explosiva.

---

### En resumen:

El diseño estructural según las NTC no es solo "hacer cuentas" para que la carga sea menor a la resistencia. Es un sistema de dos capas:

1. **Capa Cuantitativa:** Aplicar factores de seguridad estadísticos ($F_C$ y $F_R$).
2. **Capa Cualitativa:** Seguir reglas de "buena práctica" geométrica basadas en décadas de observación de desastres y éxitos reales.

¿Te gustaría que analizáramos algún factor de carga o de reducción específico para un material, como el concreto reforzado o el acero?








---

# Process - calculo de acero en zapata aislada central.

1. documentar process
    - Revisar valores y resultados del proceso
2. Desarrollar modelo
    - implementar valores y resultados del proceso en el modelo
3. Desarrollar Script

## Elemplo aplicativo

Diseño de zapata de una columna central de un edificio de 4 pisos, si se conocen los siguientes datos:

1. Pu = 74.31 $tn$ (Carga ultima de diseño amplificado)
2. f'c = 210 $\frac{kg}{cm^2}$
3. fy = 4200 $\frac{kg}{cm^2}$
4. Columna 30x50

5. Diametro de barra $db = 5/8"$
6. Dimension de zapatas: 1.50x1.8x0.50 [m] $A*B*C$

### Calculo de la reacción última del suelo

$q_u=\frac{Pu}{A*B}$

$q_u=\frac{74.31}{1.50*1.80}$

$q_u=27.52\frac{tn}{m^2}$

### Calculo de peralte efectivo "d"

$d=C-re-db$

$d=50-7.5-1.59$

$d=40.9cm$

### Verificación por cortante a flexión

El esfuerzo cortante actúa a una distancia del peralte efectivo "d" desde la cara de la columna.

---

###### Análisis para la dimensión $A=1.50m$

$Lv=(A-a)/2$

$Lv=(1.50-0.30)/2$

$Lv=0.60m$

### Cálculo del esfuerzo cortante actuante $Vua$

$Vua=q_u*(Lv-d)*B$

$Vua=27.52*(0.6-0.409)*1.80$

$Vua=9.46 tn$

### Cálculo del esfuerzo cortante admisible Vu (Esfuerzo máximo que puede resistir la zapta)

$\emptyset= 0.85$ 

$Vu = \emptyset*Vc$

$Vu = \emptyset*0.53*\sqrt{f'c}*b_0*d$

$Ecuación 11.3, articulo 11.1.2.3.1 Norma E-060$

$B_0=B=1.80m$

$Vu = 0.85*0.53*\sqrt{210}*180*40.91$

$Vu = 48073.57 kg \approxeq
 48.1 tn$

$Vua < Vu$

$9.46 < 48.1$

$Si Vua > Vu debemos aumentar la altura de la zapata$

---

###### Análisis para la dimensión $A=1.80m$

$Lv=(B-b)/2$

$Lv=(1.80-0.50)/2$

$Lv=0.65m$

### Cálculo del esfuerzo cortante actuante $Vua$

$Vua=q_u*(Lv-d)*A$

$Vua=27.52*(0.65-0.409)*1.50$

$Vua=9.95tn$

### Cálculo del esfuerzo cortante admisible Vu (Esfuerzo máximo que puede resistir la zapta)

$\emptyset= 0.85$ 

$Vu = \emptyset*Vc$

$Vu = \emptyset*0.53*\sqrt{f'c}*b_0*d$

$Ecuación 11.3, articulo 11.1.2.3.1 Norma E-060$

$B_0=A=1.50m$

$Vu = 0.85*0.53*\sqrt{210}*150*40.91$

$Vu = 48061.31 kg \approxeq
 40.1 tn$

$Vua < Vu$

$9.95 < 40.6$

$Si Vua > Vu debemos aumentar la altura de la zapata$

---

Para ambas direcciones cumple con el esfuerzo cortante máximo.

### Verificación a corte por punzonamiento

El esfuerzo por punzonamiento actúa a una distancia media del peralte efectivo $d/2$ desde las caras de la columna.

Cálculo del perímetro crítico $(b_0)$

$m = 0.30+2*d/2$

$m = 0.30+0.409\approxeq0.709m$

$n= 0.50+2*d/2$

$n=0.50+0.409\approxeq0.909m$

$b_0=2*(m+n)$

$b_0=2*(0.709+0.909)=3.24m$

#### Cálculo de Área crítica de punzonamiento $(Ac)$

$Ac=b_0*d$

$Ac=3.24*0.409=1.32m^2$

#### Cálculo de fuerza última de punzonamiento $(Fvu)$

$Fvu=Pu-q_u*m*n$

$Fvu=74.31-27.52*0.709*0909$

$Fvu=56.57tn$

#### Calculo del esfuerzo de punzonamiento admisible Vu (Esfuerzo máximo que puede resistit la zapata)

$\emptyset= 0.85$ 

Vu= $\emptyset*Vc$

El menor de:

$Vc1=\emptyset*0.53*\left(1+\frac{2}{\beta}\right)*\sqrt{f'c}*b_0*d$

$Vc2=\emptyset*0.27*\left(\frac{a_s*d}{b_0}+2\right)*\sqrt{f'c}*b_0*d$

$a_s=40(Columnas interiores)$

$a_s=30(Columnas de borde)$

$a_s=20(Columnas de esquina)$

$Vc3=\emptyset*1.06*\sqrt{f'c}*b_0*d$


$Vc1=0.85*0.53*\left(1+\frac{2}{\frac{50}{30}}\right)*\sqrt{210}*324*40.9$ 

$Vc1=190324.83kg\approxeq190.3tn$

$Vc2=0.85*0.27*\left(\frac{40*40.9}{324}+2\right)*\sqrt{210}*324*40.9$

$Vc2=310678.89kg\approxeq310.7tn$

$Vc3=0.85*1.06*\sqrt{210}*324*40.9$

$Vc3=173022.59kg\approxeq173.0tn$

$El menor es Vc3=170.3tn$

Comparamos: $Fvu<Vu$

$56.57<170.3$

### Diseño de acero de refuerzo
---
#### Cálculo de momento $Mu$ en la dirección $B=1.80m$

* analisis a un largo transverssal de 1m

#### Calculo de reacción por m

$q_u=\frac{Pu}{B*A}\rightarrow\frac{74.31}{1.80*1}=41.28\frac{tn}{m^2}$


$Mu = \frac{q_u*Lv^2*A}{2}$

$Mu = \frac{41.28*0.65^2*1}{2}$

$Mu=8.72\frac{tn.m}{m}$

$As=\frac{0.85*f'c*b*d}{fy}-\sqrt{\frac{1.7*f'c*b}{fy^2}*\left(\frac{0.85*f'c*b*b^2}{2}-\frac{Mu}{\emptyset}\right)}$

$\emptyset=0.9(Vigas y losas controladas por tensión)$

$As=\frac{0.85*210*100*40.9}{4200}-\sqrt{\frac{1.7*210*100}{4200^2}*\left(\frac{0.85*210*100*40.9^2}{2}-\frac{8.72*10^5}{0.9}\right)}$


$As=5.74\frac{cm^2}{m}$

#### Verificación del acero mínimo

##### Para losas y zapata $\rho_{\min}$=0.0018

$Asmin=0.0018*b*d$

$Asmin=0.0018*100*40.9$

$Asmin=7.36\frac{cm^2}{m}$

$Asmin>As, usar Asmin$

Entonces:

$As=7.36\frac{cm^2}{m}$

$Usando barras de \frac{5}{8}", Área de barra= 1.99cm^2$

$Cantidad(n)=\frac{As}{Ab}=\frac{7.36}{1.99}=3.69\approxeq4$

$Espaciamiento(S)=\frac{100}{n}=\frac{100}{4}=25cm$

$Usar \emptyset \frac{5}{8}" @ 25cm$
---
#### Cálculo de momento $Mu$ en la dirección $A=1.50m$

* analisis a un largo transverssal de 1m

#### Calculo de reacción por m

$q_u=\frac{Pu}{A*B}\rightarrow\frac{74.31}{1.50*1}=49.54\frac{tn}{m^2}$


$Mu = \frac{q_u*Lv^2*B}{2}$

$Mu = \frac{49.54*0.6^2*1}{2}$

$Mu=8.91\frac{tn.m}{m}$

$As=\frac{0.85*f'c*b*d}{fy}-\sqrt{\frac{1.7*f'c*b}{fy^2}*\left(\frac{0.85*f'c*b*b^2}{2}-\frac{Mu}{\emptyset}\right)}$

$\emptyset=0.9(Vigas y losas controladas por tensión)$

$As=\frac{0.85*210*100*40.9}{4200}-\sqrt{\frac{1.7*210*100}{4200^2}*\left(\frac{0.85*210*100*40.9^2}{2}-\frac{8.91*10^5}{0.9}\right)}$


$As=5.86\frac{cm^2}{m}$

#### Verificación del acero mínimo

##### Para losas y zapata $\rho_{\min}$=0.0018

$Asmin=0.0018*b*d$

$Asmin=0.0018*100*40.9$

$Asmin=7.36\frac{cm^2}{m}$

$Asmin>As, usar Asmin$

Entonces:

$As=7.36\frac{cm^2}{m}$

$Usando barras de \frac{5}{8}", Área de barra= 1.99cm^2$

$Cantidad(n)=\frac{As}{Ab}=\frac{7.36}{1.99}=3.69\approxeq4$
$Espaciamiento(S)=\frac{100}{n}=\frac{100}{4}=25cm$

$Usar \emptyset \frac{5}{8}" @ 25cm$

---

El espaciamiento máximo debe ser el de las dos siguientes condiciones:

$s\leq3d\rightarrow3*40.9=122.7cm$

$s\leq40cm$

#### Longitud de desarrollo en refuerzo de zapata

Revisar para el lado A = 1.50m

La longitud de desarrollo se mide desde la cara de la columna.

* Si el valor de x>Ld las barras de la zapata NO necesitan ganchos.

* Si el valor de X<Ld las barras de la zapara SI necesiran ganchos.

Calculo de x

$x=[(Lado\ de\ zapata-Ancho\ de\ columna)/2]-Recubrimiento$

$x=[(150-30)/2]-7.5$

$x=52.5cm$

* De acuerdo a las disposiciones de la Norma E060 determinamos el valor de "Ld". teniendoen cuenta el diámetro de barra y resistencia.

Se concsulta el cuadro de longitud de Desarrollo para barras a tracción.

El refuerzo de la zapata esta en la zona inferior, usamos en la tanbla la posición <300mm

Para $f'c=210\frac{kg}{cm^2}, \emptyset\frac{5}{8}"\rightarrow Ld=56.20cm$

x < Ld

52.50 < 56.20, Necesita ganchos en los extremos adoptamos 30cm.












#### Referencia

[Video Youtube](https://www.youtube.com/watch?v=AlYx0Nuy5k0)



El Pantone 11-4201 Cloud Dancer, el Color del Año 2026, es un blanco sutil y sereno, cuyas equivalencias aproximadas son RGB: 240, 238, 233 y HEX: #F0EEE9, mientras que su valor CMYK más cercano es 0% C, 1% M, 3% Y, 6% K, representando una base neutra ideal para la calma y la claridad en el diseño. 
Datos de Conversión:
RGB: 240, 238, 233 (Rojo, Verde, Azul)
HEX: #F0EEE9
CMYK (aproximado): 0% Cian, 1% Magenta, 3% Amarillo, 6% Negro 
Significado y Uso:
Color del Año 2026: Simboliza la simplicidad, la reflexión y un nuevo comienzo, ofreciendo un lienzo limpio para la creatividad y la armonía.
Versatilidad: Funciona como un color estructural clave, permitiendo que otros colores destaquen y creando sensación de ligereza y serenidad en cualquier aplicación.
Aplicaciones: Ideal para diseño de interiores, moda, belleza y cualquier proyecto que busque una estética fresca, minimalista y tranquilizadora. 