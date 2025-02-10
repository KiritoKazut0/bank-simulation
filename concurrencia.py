import threading
import time
import logging
from queue import Queue

class Banco:
    def __init__(self):
        self.saldo = 5000
        self.lock = threading.Lock()  # Protege el saldo del banco
        self.semaforo = threading.Semaphore(3)  # Limita a 3 ventanillas
        self.ventanilla_disponible = threading.Event()  # Notifica disponibilidad
        self.ventanillas = [None] * 3  # Estado de las ventanillas
        

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger('Banco')
        
        # Inicialmente todas las ventanillas están disponibles
        self.ventanilla_disponible.set()

    def realizar_transaccion(self, cliente_id, tipo, monto):
        """
        Función que ejecutará cada hilo (cliente)
        Implementa el flujo completo de la transacción
        """
        try:
            # 1. Solicitar y adquirir ventanilla
            self.logger.info(f"Cliente {cliente_id} esperando ventanilla")
            self.semaforo.acquire()
            
            # 2. Buscamos si hay una ventanilla disponible
            ventanilla_asignada = None
            with self.lock:
                for i in range(len(self.ventanillas)):
                    if self.ventanillas[i] is None:
                        self.ventanillas[i] = cliente_id
                        ventanilla_asignada = i
                        break
                        
            self.logger.info(f"Cliente {cliente_id} asignado a ventanilla {ventanilla_asignada}")
            
            try:
                # 3. Solicitar acceso al saldo
                with self.lock:
                    # 4. Realizar la operación
                    if tipo == "retiro":
                        if self.saldo >= monto:
                            self.saldo -= monto
                            estado = "Retiro exitoso"
                        else:
                            raise ValueError("Saldo insuficiente")
                    else:  # depósito
                        self.saldo += monto
                        estado = "Depósito exitoso"
                    
                    self.logger.info(f"Cliente {cliente_id}: {estado} - Monto: {monto}")
                    
                # Simular tiempo de procesamiento
                time.sleep(3)
                
            finally:
                # 5. Liberar ventanilla
                with self.lock:
                    self.ventanillas[ventanilla_asignada] = None
                self.semaforo.release()
                
                # 6. Notificar disponibilidad
                self.ventanilla_disponible.set()
                self.logger.info(f"Cliente {cliente_id} liberó ventanilla {ventanilla_asignada}")
                
            return estado
            
        except ValueError as e:
            self.logger.error(f"Error de validación para cliente {cliente_id}: {e}")
            return f"Error: {str(e)}"
        except Exception as e:
            self.logger.error(f"Error inesperado para cliente {cliente_id}: {e}")
            return "Error en la transacción"

    def crear_cliente(self, cliente_id, tipo, monto):
        """
        Crea y inicia un nuevo hilo para un cliente
        """
        if monto <= 0:
            raise ValueError("El monto debe ser positivo")
            
        # Crear un nuevo hilo para el cliente
        cliente_thread = threading.Thread(
            target=self.realizar_transaccion,
            args=(cliente_id, tipo, monto),
            name=f"Cliente_{cliente_id}"
        )
        
        # Iniciar el hilo
        cliente_thread.start()
        return cliente_thread