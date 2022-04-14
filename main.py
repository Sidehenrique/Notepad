import tkinter


def abrir():
    file = open('arquivo.txt', 'r')
    container = file.read()
    text_area.insert(1.0, container)


def novo():
    text_area.delete(1.0, 'end')


def salvar():
    container = text_area.get(1.0, 'and')
    fire = open('Arquivo.txt', 'w')
    fire.write(container)
    fire.close()


def UpdadeFont():
    size = spin_size.get()
    font = spin_font.get()
    text_area.config(font='{} {}'.format(font, size))


window = tkinter.Tk()
window.title('Meu Notepad')
window.geometry('430x550')
window.minsize(width=430, height=550)


frame = tkinter.Frame(window, height=25)
frame.pack(fill='x')

font_text = tkinter.Label(frame, text='Font: ')
font_text.pack(side='left')

spin_font = tkinter.Spinbox(frame, values=('Arial', 'Verdana', 'Elephant', 'Impact'))
spin_font.pack(side='left')

font_size = tkinter.Label(frame, text=' Fonte Size: ')
font_size.pack(side='left')

spin_size = tkinter.Spinbox(frame, to=60)
spin_size.pack(side='left')

botton_update = tkinter.Button(frame, text='Atualizar', command=UpdadeFont)
botton_update.pack(side='left')

text_area = tkinter.Text(window, font='Arial 20', width=1280, height=720)
text_area.pack()

main_menu = tkinter.Menu(window)

arquivo_menu = tkinter.Menu(main_menu, tearoff=0)
arquivo_menu.add_command(label='abrir', command=abrir)
arquivo_menu.add_command(label='Novo', command=novo)
arquivo_menu.add_command(label='Salvar', command=salvar)
arquivo_menu.add_command(label='Salvar Como', command=None)
arquivo_menu.add_command(label='Sair', command=window.quit)


editar_menu = tkinter.Menu(main_menu, tearoff=0)
editar_menu.add_command(label='Recortar')
editar_menu.add_command(label='Copiar')
editar_menu.add_command(label='Colar')
editar_menu.add_command(label='Deletar')
editar_menu.add_command(label='Selecionar Tudo')

formatar_menu = tkinter.Menu(main_menu, tearoff=0)
formatar_menu.add_command(label='Quebrar texto')

exibir_menu = tkinter.Menu(main_menu, tearoff=0)
exibir_menu.add_command(label='Barra de Status')

main_menu.add_cascade(label='Arquivo', menu=arquivo_menu)
main_menu.add_cascade(label='Editar', menu=editar_menu)
main_menu.add_cascade(label='Formatar', menu=formatar_menu)
main_menu.add_cascade(label='Exibir', menu=exibir_menu)

window.config(menu=main_menu)

window.mainloop()
