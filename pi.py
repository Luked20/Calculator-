from tkinter import *
from tkinter import ttk
import math
from math import sqrt, sin 
from colorama import Fore, Back, Style


 
#inicialição da calculadora 
init = Tk()
init.title("Calculadora")
init.geometry('357x420+0+0')
text_parameter = ttk.Entry(init, width=20, font=("Arial", 24))  
text_parameter.grid(columnspan=5) 
calcular = ""

    
#adição dos numeros na width
def add_to_calc(symbol):
    global calcular
    calcular += str(symbol)
    text_parameter.delete(0, "end")
    text_parameter.insert(0 , calcular)

#confirmação de contaa 
def evaluate_calc():
    global calcular
    try: 
        calcular = str(eval(calcular))
        text_parameter.delete(0, "end")
        text_parameter.insert(0 , calcular)
    except: 
        clear_calc()
        text_parameter.insert(0, "Error")
        pass
#exclusão da conta(clear)   
def clear_calc():
    global calcular  
    calcular = ""  
    text_parameter.delete(0, "end")
    if(text_parameter == 0):
            return btn_0 
    
#botoes 
btn_1 = Button(init, text="1",command=lambda: add_to_calc(1), width=5, font=("Arial", 14) )
btn_1.grid(row=1, column=1)
btn_2 = Button(init, text="2",command=lambda: add_to_calc(2), width=5, font=("Arial", 14) )
btn_2.grid(row=1, column=2)
btn_3 = Button(init, text="3",command=lambda: add_to_calc(3), width=5, font=("Arial", 14) )
btn_3.grid(row=1, column=3)
btn_4 = Button(init, text="4",command=lambda: add_to_calc(4), width=5, font=("Arial", 14) )
btn_4.grid(row=2, column=1)
btn_5 = Button(init, text="5",command=lambda: add_to_calc(5), width=5, font=("Arial", 14) )
btn_5.grid(row=2, column=2)
btn_6 = Button(init, text="6",command=lambda: add_to_calc(6), width=5, font=("Arial", 14) )
btn_6.grid(row=2, column=3)
btn_7 = Button(init, text="7",command=lambda: add_to_calc(7), width=5, font=("Arial", 14) )
btn_7.grid(row=3, column=1)
btn_8 = Button(init, text="8",command=lambda: add_to_calc(8), width=5, font=("Arial", 14) )
btn_8.grid(row=3, column=2)
btn_9 = Button(init, text="9",command=lambda: add_to_calc(9), width=5, font=("Arial", 14) )
btn_9.grid(row=3, column=3)
btn_0 = Button(init, text="0",command=lambda: add_to_calc(0), width=5, font=("Arial", 14) )
btn_0.grid(row=4, column=2)
btn_plus = Button(init, text="+",command=lambda: add_to_calc("+"), width=5, font=("Arial", 14) )
btn_plus.grid(row=1, column=4)
btn_minus = Button(init, text="-",command=lambda: add_to_calc("-"), width=5, font=("Arial", 14) )
btn_minus.grid(row=2, column=4)
btn_multi = Button(init, text="*",command=lambda: add_to_calc("*"), width=5, font=("Arial", 14) )
btn_multi.grid(row=3, column=4)
btn_div = Button(init, text="/",command=lambda: add_to_calc("/"), width=5, font=("Arial", 14) )
btn_div.grid(row=4, column=4)
btn_bracketsopn = Button(init, text="(",command=lambda: add_to_calc("("), width=5, font=("Arial", 14) )
btn_bracketsopn.grid(row=4, column=1)
btn_bracketsclose = Button(init, text=")",command=lambda: add_to_calc(")"), width=5, font=("Arial", 14) )
btn_bracketsclose.grid(row=4, column=3)
btn_equal = Button(init, text="=",command= evaluate_calc, width=15, font=("Arial", 14) )
btn_equal.grid(row=5, column=1, columnspan=2)
btn_clear = Button(init, text="C",command= clear_calc, width=5, font=("Arial", 14) )
btn_clear.grid(row=5, column=3)

#segunda janela(calculador cientifica)
def open_second_window():
    second_window = Toplevel(init)
    btn_second =Button(init, text="Calculador cientifica", command= open_second_window)
    btn_second.grid(row=5, column=4)
    second_window.title("Calculadora Cientifica")
    second_window.geometry('357x420+0+0')
    text_parameter1 =Entry(second_window, width=20, font=("Arial", 24))  
    text_parameter1.grid(columnspan=5) 
#Repetição da calculadora simples 
    def add_to_calc(symbol):
     global calcular
     calcular += str(symbol)
     text_parameter1.delete(0, "end")
     text_parameter1.insert(0 , calcular)
     


    def evaluate_calc():
     global calcular
     try: 
        calcular = str(eval(calcular))
        text_parameter1.delete(0, "end")
        text_parameter1.insert(0 , calcular)
     except: 
        clear_calc()
        text_parameter1.insert(0, "Error")
        pass
    
    def clear_calc():
     global calcular  
     calcular = ""  
     text_parameter1.delete(0, "end")
     if(text_parameter == 0):
            return btn_0
#função para calcular a potencia
    def pot(symbol):
     global calcular
     calcular += str(symbol)
     modulos = ['math.pow']
     for i in modulos:
        if i in calcular:
            calcular = calcular.replace("pow", "math.pow")
    
        resultado = eval(calcular)
        text_parameter1.delete(0, "end")
        text_parameter1.insert(0, str(resultado))
    
#função para calcular a raiz quadrada
    def root(symbol):
     global calcular
     calcular += str(symbol)
     modulos = ["√"]  
     for i in modulos:
        if i in calcular:
            
            calcular = calcular.replace("√", "")
            try:
                resultado = math.sqrt(eval(calcular))
                text_parameter1.delete(0, "end")
                text_parameter1.insert(0, str(resultado))
            except Exception as e:
                text_parameter1.delete(0, "end")
                text_parameter1.insert(0, "Erro: " + str(e))
    
#atualmente tentando descobrir como fazer a função do seno funcionar para que usar o eval não esta dando certo 
    def sin(symbol):
     global calcular
     calcular += str(symbol)
     modulos = ["sin"]
     for i in modulos:
        if i in calcular:
            calcular = calcular.replace("sin", "")
            try:
                resultado = math.sin(math.radians(eval(calcular)))  
                text_parameter1.delete(0, "end")
                text_parameter1.insert(0, str(resultado))
            except Exception as e:
                text_parameter1.delete(0, "end")
                text_parameter1.insert(0, "Erro: " + str(e))
         
            
   
    
        
       
     
        

#botoes para segunda janela 
    btn_1 = Button(second_window, text="1",command=lambda: add_to_calc(1), width=5, font=("Arial", 14) )
    btn_1.grid(row=1, column=1)
    btn_2 = Button(second_window, text="2",command=lambda: add_to_calc(2), width=5, font=("Arial", 14) )
    btn_2.grid(row=1, column=2)
    btn_3 = Button(second_window, text="3",command=lambda: add_to_calc(3), width=5, font=("Arial", 14) )
    btn_3.grid(row=1, column=3)
    btn_4 = Button(second_window, text="4",command=lambda: add_to_calc(4), width=5, font=("Arial", 14) )
    btn_4.grid(row=2, column=1)
    btn_5 = Button(second_window, text="5",command=lambda: add_to_calc(5), width=5, font=("Arial", 14) )
    btn_5.grid(row=2, column=2)
    btn_6 = Button(second_window, text="6",command=lambda: add_to_calc(6), width=5, font=("Arial", 14) )
    btn_6.grid(row=2, column=3)
    btn_7 = Button(second_window, text="7",command=lambda: add_to_calc(7), width=5, font=("Arial", 14) )
    btn_7.grid(row=3, column=1)
    btn_8 = Button(second_window, text="8",command=lambda: add_to_calc(8), width=5, font=("Arial", 14) )
    btn_8.grid(row=3, column=2)
    btn_9 = Button(second_window, text="9",command=lambda: add_to_calc(9), width=5, font=("Arial", 14) )
    btn_9.grid(row=3, column=3)
    btn_0 = Button(second_window, text="0",command=lambda: add_to_calc(0), width=5, font=("Arial", 14) )
    btn_0.grid(row=4, column=2)
    btn_pot = Button(second_window, text="^",command=lambda: pot("**"), width=5, font=("Arial", 14) )
    btn_pot.grid(row=1, column=4) 
    btn_root = Button(second_window, text="\u221a", command=lambda: root("√"), width=5, font=("Arial", 14))
    btn_root.grid(row=2, column=4)
    btn_sin = Button(second_window, text="sin", command=lambda: sin("sin"), width=5, font=("Arial", 14))
    btn_sin.grid(row=3, column=4)
    btn_equal = Button(second_window, text="=",command= evaluate_calc, width=15, font=("Arial", 14) )
    btn_equal.grid(row=5, column=1, columnspan=2) 
    btn_clear = Button(second_window, text="C",command= clear_calc, width=5, font=("Arial", 14) )
    btn_clear.grid(row=5, column=3)
  
open_second_window()


#execução do calculadora   
init.mainloop()
    
        
       
     
        

    

            

    


  
   

    








