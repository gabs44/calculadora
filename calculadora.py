from tkinter import *

root = Tk()
root.title('Calculadora')
root.configure(bg = 'white')

lb1 = Label(root, text='Calculadora', bg='white', font=('arial', 12, 'bold'), pady = 10)
lb1.pack()

visor = Entry(root, bg= 'white')
visor.pack()

# funções:

def click_button(numero):
    atual = visor.get()
    visor.delete(0, END)
    visor.insert(END, str(atual + str(numero)))

def click_ponto():
    visor.insert(END, '.')

def deletar():
    visor.delete(0, END)

def is_numeric(valor):
    try:
        float(valor)
        return True
    except:
        return False


def click_igual():
    segundo_numero = visor.get()
    visor.delete(0, END)
    if matematica == 'soma': 
        if is_numeric(p_numero) and is_numeric(segundo_numero):
            visor.insert(0, float(p_numero) + float(segundo_numero))
        else:
            visor.insert(0, 'use apenas números')
    if matematica == 'subtracao':
        if is_numeric(p_numero) and is_numeric(segundo_numero):
            visor.insert(0, float(p_numero) - float(segundo_numero))
        else:
            visor.insert(0, 'use apenas números')
    if matematica == 'multiplicacao':
        if is_numeric(p_numero) and is_numeric(segundo_numero):
            visor.insert(0, float(p_numero) * float(segundo_numero))
        else:
            visor.insert(0, 'use apenas números')
    if matematica == 'divisao':
        if is_numeric(p_numero) and is_numeric(segundo_numero):
            if segundo_numero == '0':
                visor.insert(0, 'operação impossível')
            else:
                visor.insert(0, float(p_numero) / float(segundo_numero))
        else:
            visor.insert(0, 'use apenas números')
    if matematica == 'potenciacao':
        if is_numeric(p_numero) and is_numeric(segundo_numero):
            visor.insert(0, float(p_numero) ** float(segundo_numero))
        else:
            visor.insert(0, 'use apenas números')

def click_soma():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = 'soma'
    p_numero = primeiro_numero
    visor.delete(0, END)

def click_subtracao():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = 'subtracao'
    p_numero = primeiro_numero
    visor.delete(0, END)

def click_multiplicacao():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = 'multiplicacao'
    p_numero = primeiro_numero
    visor.delete(0, END)

def click_divisao():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = 'divisao'
    p_numero = primeiro_numero
    visor.delete(0, END)

def click_potenciacao():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = 'potenciacao'
    p_numero = primeiro_numero
    visor.delete(0, END)

#fileira 1:

bt1 = Button(root, text='1', bg = 'white', pady = 25, padx= 25 , bd=2, command = lambda: click_button(1))
bt1.place(x=10, y=100)

bt2 = Button(root, text = '2' , bg = 'white', pady = 25, padx = 25, bd =2, command = lambda: click_button(2))
bt2.place(x=10, y=170)

bt3 = Button(root, text='3', bg = 'white', pady = 25, padx = 25, bd = 2, command =  lambda: click_button(3))
bt3.place(x=10, y=240)

bt0 = Button(root, text= '0', bg = 'white', pady = 25, padx = 25, bd=2, command = lambda: click_button(0))
bt0.place(x=10, y= 310)

# fileira 2:

bt4 = Button(root, text= '4', bg='white', pady = 25, padx= 25, bd=2, command =  lambda: click_button(4) )
bt4.place(x=73, y=100)

bt5= Button(root, text = '5', bg ='white', pady = 25, padx =25, bd=2, command = lambda: click_button(5))
bt5.place(x=73, y= 170)

bt6 = Button(root, text='6', bg='white', pady=25, padx=25, bd=2,command =  lambda: click_button(6))
bt6.place(x=73, y=240)

btPonto = Button(root, text='.', bg='white', pady=25, padx =25, bd=2, command = lambda: click_ponto())
btPonto.place(x=73, y=310)

# fileira 3:

bt7 = Button(root, text='7', bg= 'white', pady=25, padx=25, bd=2, command =  lambda: click_button(7) )
bt7.place(x=133, y=100)

bt8 = Button(root, text='8', bg= 'white', pady=25, padx=25, bd=2,command =  lambda: click_button(8) )
bt8.place(x=133, y=170)

bt9 = Button(root, text='9', bg= 'white', pady=25, padx=25, bd=2, command = lambda: click_button(9) )
bt9.place(x=133, y=240)

btPotenciacao = Button(root, text='**', bg='white', pady=25, padx=25, bd=2, command= click_potenciacao)
btPotenciacao.place(x=133, y=310)

# fileira 4:

btSoma = Button(root, text='+', bg='white', pady=25, padx=25, bd=2, command = click_soma)
btSoma.place(x=193, y= 100)

btSubtracao = Button(root, text='-', bg='white', pady=25, padx=25, bd=2, command = click_subtracao)
btSubtracao.place(x=193, y=170)

btMultiplicacao = Button(root, text='*', bg='white', pady=25, padx=25, bd=2, command = click_multiplicacao)
btMultiplicacao.place(x=193, y=240)

btDivisao = Button(root, text='/', bg='white', pady=25, padx=25, bd=2, command = click_divisao)
btDivisao.place(x=193, y=310)



# botão de = :

btIgual = Button(root, text='=', bg= 'lightpink1', pady=13, padx=142, bd=2, command = click_igual )
btIgual.place(x=10, y=383)

# botão CE:

btICe = Button(root, text='CE', bg= 'white', pady=130, padx=16, bd=2, command = deletar )
btICe.place(x=255, y=99)



root.geometry('320x500')
root.resizable(False, False)
root.mainloop()
