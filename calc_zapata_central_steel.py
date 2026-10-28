import math
"""
Diseño de Refuerzo para Zapatas Aisladas
DESCRIPCIÓN: 
    Calcula el acero de refuerzo, verifica cortante por flexión (una dirección) 
    y punzonamiento para una zapata aislada central sometida a carga axial.
NORMATIVA: Basado en criterios de ACI 318.
AUTOR: erwindevdesign
FECHA: 02/01/2026   
"""
# --- FUNCIÓN DE UTILIDAD ---
def round_down_to_multiple(value, multiple):
    """Redondea un valor hacia abajo al múltiplo dado."""
    return math.floor(value / multiple) * multiple

# --- DATOS DE ENTRADA ---
Pu = 74.31  # Carga Última de la columna (ton)
fc = 210    # Resistencia del concreto (kg/cm^2)
fy = 4200   # Esfuerzo de fluencia del acero (kg/cm^2)
A = 1.50    # Lado Corto de la Zapata (m)
B = 1.80    # Lado Largo de la Zapata (m)
C = 0.50    # Peralte total de la Zapata (m)
a = 0.30    # Lado Corto de la Columna (m)
b = 0.50    # Lado Largo de la Columna (m)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
D = 0.0159  # Diámetro de la barra de refuerzo (m)
re = 0.075  # Recubrimiento libre (m)
f_red = 0.85 # Factor de reducción para cortante y flexión (phi)
# Nota: 1 ton = 1000 kg

# --- CÁLCULOS DE PARÁMETROS BÁSICOS ---
d = C - re - D / 2  # Peralte efectivo (m). Usando D/2 para el centroide.
qu = Pu / (A * B)  # Esfuerzo de contacto Último (ton/m^2)

# Conversión de unidades para consistencia en fórmulas (kg y cm)
Pu_kg = Pu * 1000  # Carga Última (kg)
d_cm = d * 100     # Peralte efectivo (cm)
A_cm = A * 100     # Lado A (cm)
B_cm = B * 100     # Lado B (cm)
a_cm = a * 100     # Lado a (cm)
b_cm = b * 100     # Lado b (cm)
b_cm_flexion = 100 # Ancho de análisis para flexión (1m)

# ====================================================================
## 1. VERIFICACIÓN DE PERALTE POR CORTANTE EN UNA DIRECCIÓN
# ====================================================================

# --- Dirección Corta (Sección crítica paralela a B) ---
Lv_B = (A - a) / 2  # Voladizo en dirección corta (m)
Vua_B = qu * (Lv_B - d) * B # Cortante Último (Vua) en la sección crítica (ton)
Vua_B_kg = Vua_B * 1000 # (kg)
b_w_B = B_cm # Ancho de la sección crítica (cm)

Vc_B = 0.53 * math.sqrt(fc) * b_w_B * d_cm # Cortante nominal del concreto (kg)
Vu_B = f_red * Vc_B  # Cortante resistente del concreto (kg)

print("--- 1. VERIFICACIÓN DE PERALTE (CORTANTE EN UNA DIRECCIÓN) ---")
print(f"Peralte efectivo 'd': {d_cm:.2f} cm")
print(f"Dirección Corta (Paralela a B={B:.2f}m): Vua={Vua_B_kg:.2f} kg, Vu={Vu_B:.2f} kg")

seguir_analisis = True

# Petición 1: Detener si Vua > Vu
if Vua_B_kg > Vu_B:
    print("❌ CORTANTE DIR. CORTA: Vua > Vu. Se requiere incrementar el peralte efectivo (C o d) para continuar con el análisis.")
    seguir_analisis = False
else:
    print("✅ CORTANTE DIR. CORTA: El peralte efectivo es suficiente.")
    
if seguir_analisis:
    # --- Dirección Larga (Sección crítica paralela a A) ---
    Lv_A = (B - b) / 2
    Vua_A = qu * (Lv_A - d) * A
    Vua_A_kg = Vua_A * 1000
    b_w_A = A_cm
    
    Vc_A = 0.53 * math.sqrt(fc) * b_w_A * d_cm
    Vu_A = f_red * Vc_A

    print(f"Dirección Larga (Paralela a A={A:.2f}m): Vua={Vua_A_kg:.2f} kg, Vu={Vu_A:.2f} kg")

    if Vua_A_kg > Vu_A:
        print("❌ CORTANTE DIR. LARGA: Vua > Vu. Se requiere incrementar el peralte efectivo (C o d) para continuar con el análisis.")
        seguir_analisis = False
    else:
        print("✅ CORTANTE DIR. LARGA: El peralte efectivo es suficiente.")

if seguir_analisis:
    
    # ====================================================================
    ## 2 & 3. CÁLCULO Y VERIFICACIÓN POR PUNZONAMIENTO
    # ====================================================================

    # Dimensiones de la sección crítica de punzonamiento
    m_cm = a_cm + d_cm   # Lado de la columna a + d (cm)
    n_cm = b_cm + d_cm   # Lado de la columna b + d (cm)
    b_0 = 2 * (m_cm + n_cm) # Perímetro de la sección crítica (cm)

    # Esfuerzo Último por Punzonamiento (Fvu)
    Ac = (m_cm/100) * (n_cm/100) # Área dentro del perímetro crítico (m^2)
    Fvu = Pu - qu * Ac # Fuerza Última por Punzonamiento (ton)
    Fvu_kg = Fvu * 1000 # (kg)

    print("\n--- 2 & 3. CÁLCULO Y VERIFICACIÓN POR PUNZONAMIENTO ---")
    print(f"Fvu (Fuerza Última): {Fvu_kg:.2f} kg")
    
    # Parámetro beta_c: relación lado largo a lado corto de la columna
    beta_c = max(a, b) / min(a, b)

    # Vc1: Fórmula 0.53 * (1 + 2/beta_c) * sqrt(fc) * b0 * d * f_red
    Vc1 = (f_red * 0.53 * (1 + (2 / beta_c)) * math.sqrt(fc) * b_0 * d_cm)
    
    # Vc2: Fórmula 0.27 * ( (alpha_s * d / b0) + 2 ) * sqrt(fc) * b0 * d * f_red
    # Petición 2: Se asume columna interior (alpha_s=40)
    alpha_s = 40 
    Vc2 = (f_red * 0.27 * (((alpha_s * d_cm) / b_0) + 2) * math.sqrt(fc) * b_0 * d_cm)
    
    # Vc3: Fórmula 1.06 * sqrt(fc) * b0 * d * f_red
    Vc3 = (f_red * 1.06 * math.sqrt(fc) * b_0 * d_cm)

    # Petición 2: Vu Admisible es el menor de los tres.
    Vu_punch_kg = min(Vc1, Vc2, Vc3) # Fuerza Resistente por Punzonamiento (kg)

    print(f"Vc1: {Vc1:.2f} kg | Vc2 (alpha_s={alpha_s}): {Vc2:.2f} kg | Vc3: {Vc3:.2f} kg")
    print(f"Vu (Fuerza Resistente - Menor de Vc's): {Vu_punch_kg:.2f} kg\n")

    # Petición 3: Verificar Fvu < Vu
    if Fvu_kg > Vu_punch_kg:
        print("❌ PUNZONAMIENTO: Fvu > Vu. Se requiere incrementar el peralte efectivo o usar estribos.")
        seguir_analisis = False
    else:
        print("✅ PUNZONAMIENTO: La sección es adecuada contra punzonamiento.")

    # ====================================================================
    ## 4 & 6. CÁLCULO Y ESPACIAMIENTO DEL ACERO (Flexión)
    # ====================================================================

    if seguir_analisis:
        print("\n--- 4 & 6. CÁLCULO DEL ACERO DE REFUERZO Y ESPACIAMIENTO ---")

        # --- FÓRMULAS COMUNES PARA EL CÁLCULO DE AS ---
        
        # Momento Último (Mu) en la sección crítica (por metro de ancho)
        qu_kg_m2 = qu * 1000 # Esfuerzo de contacto (kg/m^2)

        # 1. DIRECCIÓN CORTA (Refuerzo principal - Voladizo Lv_A, ancho A=1.50m)
        Lv_A_m = (B - b) / 2  # Voladizo en dirección corta (m)
        Mu_A = (qu_kg_m2 * (Lv_A_m**2) / 2) * 1 # Mu en la dirección corta por metro de ancho (kg·m/m)
        Mu_A_kg_cm = Mu_A * 100 # (kg·cm/m)
        Ancho_A_cm = A_cm
        
        # 2. DIRECCIÓN LARGA (Refuerzo secundario - Voladizo Lv_B, ancho B=1.80m)
        Lv_B_m = (A - a) / 2  # Voladizo en dirección larga (m)
        Mu_B = (qu_kg_m2 * (Lv_B_m**2) / 2) * 1 # Mu en la dirección larga por metro de ancho (kg·m/m)
        Mu_B_kg_cm = Mu_B * 100 # (kg·cm/m)
        Ancho_B_cm = B_cm
        
        # Término 1 (T1) de la ecuación de As (válido para ambas direcciones, con b=100cm)
        T1 = (0.85 * fc * b_cm_flexion * d_cm) / fy
        
        # --- Cálculo del Área de Acero por metro (As/m) ---
        
        # As para Dirección Corta (As_A)
        R_sq_A = math.sqrt(
            ((1.7 * fc * b_cm_flexion) / (fy**2))
            * (((0.85 * fc * b_cm_flexion * (d_cm**2)) / 2) - (Mu_A_kg_cm / 0.9))
        )
        As_A = T1 - R_sq_A  # Área de acero requerida (cm^2/m)

        # As para Dirección Larga (As_B)
        R_sq_B = math.sqrt(
            ((1.7 * fc * b_cm_flexion) / (fy**2))
            * (((0.85 * fc * b_cm_flexion * (d_cm**2)) / 2) - (Mu_B_kg_cm / 0.9))
        )
        As_B = T1 - R_sq_B  # Área de acero requerida (cm^2/m)

        # Área Mínima de Acero (Asmin)
        Asmin = 0.0018 * b_cm_flexion * d_cm  # 0.0018 * b * d (cm^2/m)

        # Petición 4: Usar el mayor entre As y Asmin (práctica correcta)
        As_uso_A = max(As_A, Asmin) # cm^2/m
        As_uso_B = max(As_B, Asmin) # cm^2/m
        
        # Área de la barra individual (D=0.0159m = 1.59cm)
        Ab = (math.pi * (D * 100)**2) / 4 # cm^2

        # --- Espaciamiento y Número de Barras (Dirección Corta) ---
        S_A_calc = 100 / (As_uso_A / Ab) # Espaciamiento calculado (cm)
        S_A_final = round_down_to_multiple(S_A_calc, 5.0) # Redondeo al múltiplo de 5cm hacia abajo (Petición 6)
        
        # El espaciamiento no puede ser cero, si el cálculo es muy pequeño (p.ej. < 5cm), fijarlo a 5cm.
        if S_A_final < 5:
            S_A_final = 5.0

        N_A = math.ceil(Ancho_A_cm / S_A_final) + 1 # Total de barras (+1 para el inicio)

        # --- Espaciamiento y Número de Barras (Dirección Larga) ---
        S_B_calc = 100 / (As_uso_B / Ab) # Espaciamiento calculado (cm)
        S_B_final = round_down_to_multiple(S_B_calc, 5.0) # Redondeo al múltiplo de 5cm hacia abajo (Petición 6)
        
        if S_B_final < 5:
            S_B_final = 5.0

        N_B = math.ceil(Ancho_B_cm / S_B_final) + 1 # Total de barras (+1 para el inicio)

        print(f"\n* Área de Acero Mínima (Asmin): {Asmin:.2f} cm^2/m")
        print("\n--- Dirección Corta (Refuerzo en Sentido A=1.50m) ---")
        print(f"As (requerido): {As_A:.2f} cm^2/m. As de uso: {As_uso_A:.2f} cm^2/m")
        print(f"Espaciamiento Calculado (S_calc): {S_A_calc:.2f} cm")
        print(f"Espaciamiento Final (S_A): {S_A_final:.2f} cm (Redondeado a mult. de 5cm hacia abajo)")
        print(f"Número Total de Barras (N_A): {N_A} barras.")
        
        print("\n--- Dirección Larga (Refuerzo en Sentido B=1.80m) ---")
        print(f"As (requerido): {As_B:.2f} cm^2/m. As de uso: {As_uso_B:.2f} cm^2/m")
        print(f"Espaciamiento Calculado (S_calc): {S_B_calc:.2f} cm")
        print(f"Espaciamiento Final (S_B): {S_B_final:.2f} cm (Redondeado a mult. de 5cm hacia abajo)")
        print(f"Número Total de Barras (N_B): {N_B} barras.")
        
        
        # ====================================================================
        ## 5. REQUISITOS DE DESARROLLO (GANCHOS)
        # ====================================================================
        
        # Longitud de Desarrollo Disponible (Ld_disp)
        Ld_disp_A = Lv_A_m * 100 - re * 100 # (cm)
        Ld_disp_B = Lv_B_m * 100 - re * 100 # (cm)
        D_cm = D * 100 # Diámetro en cm
        
        # Longitud de Desarrollo con Gancho Estándar (Ldh) ACI 318 (Fórmula simplificada)
        Ldh_req = (0.24 * D_cm * fy) / math.sqrt(fc) # cm 
        
        # Dimensiones mínimas del gancho a 90°
        L_recto_min = max(8 * D_cm, 15) # cm (Longitud recta después de la cara de la columna)
        L_gancho_min = 12 * D_cm # cm (Longitud de la extensión recta del gancho, 12db)

        print("\n--- 5. REQUISITOS DE GANCHOS EN LOS EXTREMOS ---")
        print(f"Longitud de desarrollo disponible (Dir. Corta): {Ld_disp_A:.2f} cm")
        print(f"Longitud de desarrollo disponible (Dir. Larga): {Ld_disp_B:.2f} cm")
        print("Debido a que las longitudes disponibles son pequeñas, se requieren **ganchos estándar** a 90°.")
        print(f"Para la barra de {D_cm:.2f} cm, las dimensiones mínimas a cumplir son:")
        print(f"* Longitud de Desarrollo Requerida (Ldh_req): {Ldh_req:.2f} cm")
        print(f"* Longitud mínima del tramo recto (L_recto): {L_recto_min:.2f} cm")
        print(f"* Longitud mínima de la extensión del gancho (L_gancho): {L_gancho_min:.2f} cm")
        
    else:
        print("\n=========================================================")
        print("                 🚫 ANÁLISIS DETENIDO 🚫")
        print("=========================================================")
        print("La zapata falló la verificación por cortante o punzonamiento.")
        print("Se debe aumentar el peralte efectivo ($d$) antes de continuar con el cálculo del acero.")

