from tkinter import *


class Imaginario:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return Imaginario(real, imag)

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return Imaginario(real, imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Imaginario(real, imag)

    def __truediv__(self, other):
        divisor = other.real**2 + other.imag**2
        real = (self.real * other.real + self.imag * other.imag) / divisor
        imag = (self.imag * other.real - self.real * other.imag) / divisor
        return Imaginario(real, imag)


class app:
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title("Calculadora de Números Imaginarios")

        # Crear las etiquetas y campos de entrada para los números imaginarios
        real1_label = Label(self.__ventana, text="Parte Real 1:")
        real1_label.grid(row=0, column=0)
        self.real1_entry = Entry(self.__ventana)
        self.real1_entry.grid(row=0, column=1)

        imag1_label = Label(self.__ventana, text="Parte Imaginaria 1:")
        imag1_label.grid(row=1, column=0)
        self.imag1_entry = Entry(self.__ventana)
        self.imag1_entry.grid(row=1, column=1)

        real2_label = Label(self.__ventana, text="Parte Real 2:")
        real2_label.grid(row=2, column=0)
        self.real2_entry = Entry(self.__ventana)
        self.real2_entry.grid(row=2, column=1)

        imag2_label = Label(self.__ventana, text="Parte Imaginaria 2:")
        imag2_label.grid(row=3, column=0)
        self.imag2_entry = Entry(self.__ventana)
        self.imag2_entry.grid(row=3, column=1)

        # Crear la etiqueta y la variable para la selección de operación
        operacion_label = Label(self.__ventana, text="Operación:")
        operacion_label.grid(row=4, column=0)
        self.operacion_var = StringVar()
        self.operacion_var.set("+")  # Valor inicial de la selección
        operacion_optionmenu = OptionMenu(self.__ventana, self.operacion_var, "+", "-", "*", "/")
        operacion_optionmenu.grid(row=4, column=1)

        # Crear el botón de calcular
        calcular_button = Button(self.__ventana, text="Calcular", command=self.calcular_resultado)
        calcular_button.grid(row=5, column=0, columnspan=2)

        # Crear la etiqueta para mostrar el resultado
        self.resultado_label = Label(self.__ventana, text="Resultado: ")
        self.resultado_label.grid(row=6, column=0, columnspan=2)

        self.__ventana.mainloop()

    def calcular_resultado(self):
        try:
            # Obtener los números ingresados en la interfaz
            real1 = float(self.real1_entry.get())
            imag1 = float(self.imag1_entry.get())
            real2 = float(self.real2_entry.get())
            imag2 = float(self.imag2_entry.get())

            # Crear objetos de la clase Imaginario con los números ingresados
            num1 = Imaginario(real1, imag1)
            num2 = Imaginario(real2, imag2)

            # Realizar la operación seleccionada
            operacion = self.operacion_var.get()
            if operacion == "+":
                resultado = num1 + num2
            elif operacion == "-":
                resultado = num1 - num2
            elif operacion == "*":
                resultado = num1 * num2
            elif operacion == "/":
                resultado = num1 / num2

            # Mostrar el resultado en la etiqueta de resultado
            self.resultado_label.config(text=f"Resultado: {resultado.real} + {resultado.imag}i")
        except ValueError:
            self.resultado_label.config(text="Error: Ingrese números válidos")


def test():
    mi_app = app()


if __name__ == '__main__':
    test()


