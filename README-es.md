<span style="float: right;">[🌐 EN](README-en.md)</span>



# Diseño de Refuerzo para Zapatas Aisladas (ACI 318)

Script en Python para el diseño automatizado y verificación de refuerzo en zapatas aisladas rectangulares sometidas a carga axial concéntrica, fundamentada en los criterios del Código del American Concrete Institute (**ACI 318**).

---

## 📋 Descripción General

Este script realiza el análisis estructural y el dimensionamiento del acero de refuerzo principal y secundario para una zapata aislada central. Evalúa de forma secuencial las condiciones límite de servicio y resistencia última exigidas por la normativa vigente, incluyendo:
1. **Verificación de peralte por cortante en una dirección** (cortante por flexión) en ambas direcciones ortogonales.
2. **Verificación por punzonamiento (cortante en dos direcciones)** considerando una columna interior ($\alpha_s = 40$) y los límites normativos.
3. **Cálculo del momento último** y área de acero requerida ($A_s$) por metro de ancho.
4. **Determinación del acero mínimo** ($\rho_{min} = 0.0018$) y espaciamiento óptimo de barras con redondeo constructivo.
5. **Verificación de requisitos de desarrollo y ganchos estándar a $90^\circ$** debido a las restricciones geométricas del voladizo.

---

## 📐 Parámetros de Entrada del Script

Los datos de diseño se configuran directamente en las variables globales del script:

| Variable | Descripción | Valor por Defecto | Unidades |
| :--- | :--- | :--- | :--- |
| `Pu` | Carga última de servicio amplificada | $74.31$ | $\text{ton}$ |
| `fc` | Resistencia especificada a la compresión del concreto | $210$ | $\text{kg/cm}^2$ |
| `fy` | Esfuerzo de fluencia del acero de refuerzo | $4200$ | $\text{kg/cm}^2$ |
| `A` | Lado corto de la zapata | $1.50$ | $\text{m}$ |
| `B` | Lado largo de la zapata | $1.80$ | $\text{m}$ |
| `C` | Peralte total de la zapata | $0.50$ | $\text{m}$ |
| `a` | Lado corto de la columna | $0.30$ | $\text{m}$ |
| `b` | Lado largo de la columna | $0.50$ | $\text{m}$ |
| `D` | Diámetro de la barra de refuerzo (ej. #5) | $0.0159$ | $\text{m}$ |
| `re` | Recubrimiento libre inferior | $0.075$ | $\text{m}$ |
| `f_red` | Factor de reducción de resistencia ($\phi$) | $0.85$ | - |

---

## ⚙️ Requisitos del Sistema y Ejecución

* **Python:** Versión 3.8 o superior.
* **Dependencias:** Utiliza exclusivamente la biblioteca estándar de Python (`math`), por lo que no requiere instalación de paquetes externos (`pip`).

### Ejecución en Terminal:
```bash
python zapata_aislada.py
```

---

## 🔬 Fundamento Normativo (ACI 318)

El script implementa los siguientes controles de seguridad estructural:

1. **Cortante en Una Dirección:**
   Se evalúa en las secciones críticas ubicadas a una distancia $d$ de la cara de la columna en ambas direcciones. El cortante nominal del concreto se calcula mediante:
   $$V_c = 0.53 \lambda \sqrt{f'_c} b_w d$$
   Si la fuerza cortante última $V_{ua}$ supera la resistencia de diseño $\phi V_c$, el script detiene la ejecución y emite una advertencia para incrementar el peralte $C$.

2. **Punzonamiento (Dos Direcciones):**
   Se evalúa en un perímetro crítico $b_0$ situado a $d/2$ de las caras de la columna. El cortante resistente se define como el valor mínimo entre tres expresiones normativas del ACI 318:
   * $V_{c1} = \phi \times 0.53 \left(1 + \frac{2}{\beta_c}\right) \sqrt{f'_c} b_0 d$
   * $V_{c2} = \phi \times 0.27 \left(\frac{\alpha_s d}{b_0} + 2\right) \sqrt{f'_c} b_0 d$
   * $V_{c3} = \phi \times 1.06 \sqrt{f'_c} b_0 d$

3. **Flexión y Acero Requerido:**
   Se emplea el equilibrio de fuerzas internas para secciones rectangulares sometidas a flexión, determinando el área de acero por metro lineal ($A_s$) mediante la resolución de la ecuación cuadrática de equilibrio. Se compara directamente contra el acero mínimo por temperatura y contracción:
   $$A_{s,\min} = 0.0018 \, b \, d$$

---

## ⚠️ Advertencia y Limitación de Responsabilidad Profesional

> **Aviso Importante:** Este software es una herramienta de cálculo auxiliar destinada exclusivamente a ingenieros civiles y calculistas experimentados. Los resultados generados por el script **deben ser verificados y validados de manera independiente** mediante criterio profesional, memoria de cálculo formal y cumplimiento estricto de las normativas locales vigentes. El autor no asume responsabilidad legal por fallas estructurales derivadas del uso directo de esta herramienta sin supervisión experta.

---

## 🚀 Áreas de Oportunidad y Roadmap de Mejora

Para evolucionar esta herramienta hacia un entorno de diseño modular y de nivel industrial, se proponen las siguientes mejoras técnicas:

* **Modularización y Programación Orientada a Objetos (POO):** Refactorizar el script en clases (`ZapataAislada`, `SeccionCritica`, `Materiales`) para permitir múltiples corridas y validaciones iterativas.
* **Soporte para Cargas Excéntricas ($P-M_x-M_y$):** Incorporar la distribución de presiones trapezoidal/triangular bajo zapatas sometidas a momentos flectores biaxiales.
* **Interfaz de Usuario (CLI Interactiva / GUI):** Migrar el ingreso de datos estáticos a un script interactivo con `argparse` o una interfaz web ligera usando Streamlit.
* **Optimización Económica Automatizada:** Implementar un bucle iterativo que varíe automáticamente las dimensiones en planta ($A, B$) y el peralte ($C$) para buscar la solución más económica cumpliendo con las relaciones de demanda/capacidad ($D/C \le 1.0$).
* **Generación de Reportes Automáticos:** Exportar los resultados detallados y diagramas de distribución de acero a formatos normalizados como PDF o Markdown estructurado.

---

## 📝 Autor

* **erwindevdesign**
* *Fecha de última actualización:* Enero de 2026
