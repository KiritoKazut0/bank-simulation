import tkinter as tk
from concurrencia import Banco

class InterfazBanco:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulación de Sistema Bancario")
        
        self.banco = Banco()
        self.cliente_count = 0
        self.clientes_activos = {}  


        main_frame = tk.Frame(root, padx=10, pady=10)
        main_frame.pack(expand=True, fill='both')


        tk.Label(main_frame, text="Sistema Bancario", font=("Arial", 16, "bold")).pack(pady=5)
        
 
        self.saldo_label = tk.Label(main_frame, text=f"Saldo: ${self.banco.saldo}", font=("Arial", 14))
        self.saldo_label.pack(pady=10)


        control_frame = tk.Frame(main_frame)
        control_frame.pack(pady=10)

 
        self.monto_var = tk.StringVar(value="100")
        tk.Label(control_frame, text="Monto:").grid(row=0, column=0, padx=5)
        tk.Entry(control_frame, textvariable=self.monto_var, width=10).grid(row=0, column=1, padx=5)

    
        tk.Button(control_frame, text="Nuevo Depósito", 
                 command=lambda: self.crear_nuevo_cliente("deposito")).grid(row=0, column=2, padx=5)
        tk.Button(control_frame, text="Nuevo Retiro", 
                 command=lambda: self.crear_nuevo_cliente("retiro")).grid(row=0, column=3, padx=5)

   
        ventanillas_frame = tk.LabelFrame(main_frame, text="Estado de Ventanillas", pady=5)
        ventanillas_frame.pack(fill='x', pady=10)

        self.ventanilla_labels = []
        for i in range(3):
            label = tk.Label(ventanillas_frame, text=f"Ventanilla {i+1}: Disponible", 
                           bg="green", width=30)
            label.pack(pady=2)
            self.ventanilla_labels.append(label)

        self.actualizar_interfaz()

    def crear_nuevo_cliente(self, tipo):
     
        try:
            self.cliente_count += 1
            monto = int(self.monto_var.get())
            
           
            cliente_thread = self.banco.crear_cliente(self.cliente_count, tipo, monto)
            self.clientes_activos[self.cliente_count] = cliente_thread
            
        except ValueError as e:
            tk.messagebox.showerror("Error", f"Monto inválido: {str(e)}")

    def actualizar_interfaz(self):

        self.saldo_label.config(text=f"Saldo: ${self.banco.saldo}")

  
        for i, label in enumerate(self.ventanilla_labels):
            cliente_id = self.banco.ventanillas[i]
            if cliente_id is None:
                label.config(text=f"Ventanilla {i+1}: Disponible", bg="green")
            else:
                label.config(text=f"Ventanilla {i+1}: Cliente {cliente_id}", bg="red")

        for cliente_id, thread in list(self.clientes_activos.items()):
            if not thread.is_alive():
                del self.clientes_activos[cliente_id]

        self.root.after(1000, self.actualizar_interfaz)