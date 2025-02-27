# 🏦 Sistema de Simulación Bancaria Concurrente

<p align="center">
  <img src="https://raw.githubusercontent.com/KiritoKazut0/bank-simulation/main/assets/logo.png" width="100%" alt="Bank Simulation Logo" />
</p>

---

## 🖍 Descripción
Sistema que simula las operaciones de un banco con tres ventanillas, implementando programación concurrente en Python. Cada cliente es un hilo independiente que puede realizar depósitos o retiros, manteniendo la integridad del saldo bancario mediante mecanismos de sincronización.

---

## ✨ Características Principales

- 🔄 Simulación concurrente de operaciones bancarias
- 👥 Múltiples clientes operando simultáneamente
- 🏧 Tres ventanillas de servicio
- 💰 Control de saldo en tiempo real
- 🔒 Sincronización mediante primitivas de threading

---

## 🔧 Tecnologías Utilizadas

- **Python 3.x**: Lenguaje de programación principal
- **Tkinter**: Interfaz gráfica de usuario
- **Threading**: Módulo para programación concurrente:
  - Lock
  - Semaphore
  - Event

---

## 🏛️ Arquitectura del Sistema

<p align="center">
  <img src="https://raw.githubusercontent.com/KiritoKazut0/bank-simulation/main/assets/arquitectura.png" width="80%" alt="Arquitectura del Sistema" />
</p>

### 🧬 Componentes Principales

#### 🧵 Hilos (Threads)
- **Cliente (Thread Principal)**:
  - Representa cada cliente como un hilo independiente.
  - Gestiona operaciones de depósito y retiro.
  - Interactúa con las ventanillas disponibles.

#### 🔒 Primitivas de Sincronización
1. **Lock**:
   - Protege el acceso al saldo bancario.
   - Previene condiciones de carrera.
   - Asegura la integridad de las transacciones.
2. **Semaphore(3)**:
   - Controla el acceso a ventanillas.
   - Limita a 3 clientes simultáneos.
   - Gestiona la disponibilidad de servicio.
3. **Event**:
   - Señaliza ventanillas disponibles.
   - Optimiza la cola de espera.
   - Mejora la eficiencia del sistema.

---

## 🗂️ Estructura del Proyecto

```bash
bank_simulation/
├── 🗍 main.py           # Punto de entrada
├── 🗍 concurrencia.py   # Lógica de concurrencia
├── 🗍 vista.py          # Interfaz gráfica
├── 📁 assets/           # Imágenes y diagramas
├── 🗍 README.md         # Documentación
```

---

## ⚙️ Requisitos Previos

```txt
- Python 3.x
- Tkinter (incluido en Python)
```

---

## 🚀 Instalación y Ejecución

### 1⃣ Clonar el repositorio
```bash
git clone https://github.com/KiritoKazut0/bank-simulation.git
cd bank-simulation
```

### 2⃣ Ejecutar la aplicación
```bash
python main.py
```

---

## 💻 Uso

1. Inicia la aplicación.
2. Usa los botones para crear nuevos clientes.
3. Ingresa el monto para la transacción.
4. Observa el estado de las ventanillas y el saldo en tiempo real.

---

## 🛡️ Manejo de Excepciones

- ✅ Validación de montos negativos.
- ✅ Control de saldo insuficiente.
- ✅ Gestión de errores en hilos.
- ✅ Sistema de logging completo.

---

## 📑 Recursos Adicionales

- Documentación completa del código en los comentarios.
- Diagramas ilustrativos disponibles en la carpeta `assets`.

---

## ✍️ Autor

**[Norberto Lopez](https://github.com/KiritoKazut0)**