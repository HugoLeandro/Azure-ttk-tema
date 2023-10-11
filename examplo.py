
# "Exemplo de script para testar o tema Azure ttk
# Autor: rdbende
# Licença: Licença MIT
# Fonte: https://github.com/rdbende/ttk-widget-factory"


import tkinter as tk
from tkinter import ttk


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Tornar o aplicativo responsivo.
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Criar listas de valores.
        self.option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]
        self.combo_list = ["Combobox", "Editable item 1", "Editable item 2"]
        self.readonly_combo_list = ["Readonly combobox", "Item 1", "Item 2"]

        # Criar variáveis de controle.
        self.var_0 = tk.BooleanVar()
        self.var_1 = tk.BooleanVar(value=True)
        self.var_2 = tk.BooleanVar()
        self.var_3 = tk.IntVar(value=2)
        self.var_4 = tk.StringVar(value=self.option_menu_list[1])
        self.var_5 = tk.DoubleVar(value=75.0)

        # Criar widgets :)
        self.setup_widgets()

    def setup_widgets(self):
        # Crie um Quadro para os botões de seleção (Checkbuttons)
        self.check_frame = ttk.LabelFrame(self, text="Checkbuttons", padding=(20, 10))
        self.check_frame.grid(
            row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )

        # Checkbuttons
        self.check_1 = ttk.Checkbutton(
            self.check_frame, text="Unchecked", variable=self.var_0
        )
        self.check_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

        self.check_2 = ttk.Checkbutton(
            self.check_frame, text="Checked", variable=self.var_1
        )
        self.check_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

        self.check_3 = ttk.Checkbutton(
            self.check_frame, text="Third state", variable=self.var_2
        )
        self.check_3.state(["alternate"])
        self.check_3.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

        self.check_4 = ttk.Checkbutton(
            self.check_frame, text="Disabled", state="disabled"
        )
        self.check_4.state(["disabled !alternate"])
        self.check_4.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

        # Separador
        self.separator = ttk.Separator(self)
        self.separator.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="ew")

        # Crie um Quadro para os Radiobotoes
        self.radio_frame = ttk.LabelFrame(self, text="Radiobuttons", padding=(20, 10))
        self.radio_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")

        # Radiobuttons
        self.radio_1 = ttk.Radiobutton(
            self.radio_frame, text="Unselected", variable=self.var_3, value=1
        )
        self.radio_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
        self.radio_2 = ttk.Radiobutton(
            self.radio_frame, text="Selected", variable=self.var_3, value=2
        )
        self.radio_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
        self.radio_4 = ttk.Radiobutton(
            self.radio_frame, text="Disabled", state="disabled"
        )
        self.radio_4.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

        # Crie um quadro para widgets de entrada
        self.widgets_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.widgets_frame.grid(
            row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3
        )
        self.widgets_frame.columnconfigure(index=0, weight=1)

        # Entrada
        self.entry = ttk.Entry(self.widgets_frame)
        self.entry.insert(0, "Entrada")
        self.entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")

        # Caixa de rotação
        self.spinbox = ttk.Spinbox(self.widgets_frame, from_=0, to=100, increment=0.1)
        self.spinbox.insert(0, "Caixa de Rotação")
        self.spinbox.grid(row=1, column=0, padx=5, pady=10, sticky="ew")

        # Caixa de combinação
        self.combobox = ttk.Combobox(self.widgets_frame, values=self.combo_list)
        self.combobox.current(0)
        self.combobox.grid(row=2, column=0, padx=5, pady=10, sticky="ew")

        # Caixa de combinação somente leitura
        self.readonly_combo = ttk.Combobox(
            self.widgets_frame, state="readonly", values=self.readonly_combo_list
        )
        self.readonly_combo.current(0)
        self.readonly_combo.grid(row=3, column=0, padx=5, pady=10, sticky="ew")

        # Menu para o Botão de Menu
        self.menu = tk.Menu(self)
        self.menu.add_command(label="Menu item 1")
        self.menu.add_command(label="Menu item 2")
        self.menu.add_separator()
        self.menu.add_command(label="Menu item 3")
        self.menu.add_command(label="Menu item 4")

        # Botão de Menu
        self.menubutton = ttk.Menubutton(
            self.widgets_frame, text="Botão de Menu", menu=self.menu, direction="below"
        )
        self.menubutton.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")

        # Menu de Opções (OptionMenu)
        self.optionmenu = ttk.OptionMenu(
            self.widgets_frame, self.var_4, *self.option_menu_list
        )
        self.optionmenu.grid(row=5, column=0, padx=5, pady=10, sticky="nsew")

        # Botão
        self.button = ttk.Button(self.widgets_frame, text="Botão")
        self.button.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")

        # Botão de Acento
        self.accentbutton = ttk.Button(
            self.widgets_frame, text="Botão de Acento", style="Accent.TButton"
        )
        self.accentbutton.grid(row=7, column=0, padx=5, pady=10, sticky="nsew")

        # Botão de Alternância
        self.togglebutton = ttk.Checkbutton(
            self.widgets_frame, text="Botão de Alternância", style="Toggle.TButton"
        )
        self.togglebutton.grid(row=8, column=0, padx=5, pady=10, sticky="nsew")

        # Interruptor
        self.switch = ttk.Checkbutton(
            self.widgets_frame, text="Switch", style="Switch.TCheckbutton"
        )
        self.switch.grid(row=9, column=0, padx=5, pady=10, sticky="nsew")

        # Panedwindow
        self.paned = ttk.PanedWindow(self)
        self.paned.grid(row=0, column=2, pady=(25, 5), sticky="nsew", rowspan=3)

        # Pane #1
        self.pane_1 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_1, weight=1)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.pane_1)
        self.scrollbar.pack(side="right", fill="y")

        # Treeview
        self.treeview = ttk.Treeview(
            self.pane_1,
            selectmode="browse",
            yscrollcommand=self.scrollbar.set,
            columns=(1, 2),
            height=10,
        )
        self.treeview.pack(expand=True, fill="both")
        self.scrollbar.config(command=self.treeview.yview)

        # Colunas da Treeview
        self.treeview.column("#0", anchor="w", width=120)
        self.treeview.column(1, anchor="w", width=120)
        self.treeview.column(2, anchor="w", width=120)

        # Cabeçalhos da Treeview
        self.treeview.heading("#0", text="Coluna 1", anchor="center")
        self.treeview.heading(1, text="Coluna 2", anchor="center")
        self.treeview.heading(2, text="Coluna 3", anchor="center")

        # Definir dados da Treeview
        treeview_data = [
            ("", 1, "Pai", ("Item 1", "Valor 1")),
            (1, 2, "Filho", ("Subitem 1.1", "Valor 1.1")),
            (1, 3, "Filho", ("Subitem 1.2", "Valor 1.2")),
            (1, 4, "Filho", ("Subitem 1.3", "Valor 1.3")),
            (1, 5, "Filho", ("Subitem 1.4", "Valor 1.4")),
            ("", 6, "Pai", ("Item 2", "Valor 2")),
            (6, 7, "Filho", ("Subitem 2.1", "Valor 2.1")),
            (6, 8, "Subpai", ("Subitem 2.2", "Valor 2.2")),
            (8, 9, "Filho", ("Subitem 2.2.1", "Valor 2.2.1")),
            (8, 10, "Filho", ("Subitem 2.2.2", "Valor 2.2.2")),
            (8, 11, "Filho", ("Subitem 2.2.3", "Valor 2.2.3")),
            (6, 12, "Filho", ("Subitem 2.3", "Valor 2.3")),
            (6, 13, "Filho", ("Subitem 2.4", "Valor 2.4")),
            ("", 14, "Pai", ("Item 3", "Valor 3")),
            (14, 15, "Filho", ("Subitem 3.1", "Valor 3.1")),
            (14, 16, "Filho", ("Subitem 3.2", "Valor 3.2")),
            (14, 17, "Filho", ("Subitem 3.3", "Valor 3.3")),
            (14, 18, "Filho", ("Subitem 3.4", "Valor 3.4")),
            ("", 19, "Pai", ("Item 4", "Valor 4")),
            (19, 20, "Filho", ("Subitem 4.1", "Valor 4.1")),
            (19, 21, "Subpai", ("Subitem 4.2", "Valor 4.2")),
            (21, 22, "Filho", ("Subitem 4.2.1", "Valor 4.2.1")),
            (21, 23, "Filho", ("Subitem 4.2.2", "Valor 4.2.2")),
            (21, 24, "Filho", ("Subitem 4.2.3", "Valor 4.2.3")),
            (19, 25, "Filho", ("Subitem 4.3", "Valor 4.3")),]

        # Inserir dados na Treeview
        for item in treeview_data:
            self.treeview.insert(
                parent=item[0], index="end", iid=item[1], text=item[2], values=item[3]
            )
            if item[0] == "" or item[1] in {8, 21}:
                self.treeview.item(item[1], open=True)  # Open parents

        # Selecionar e rolar
        self.treeview.selection_set(10)
        self.treeview.see(7)

        # Caderno, painel #2.
        self.pane_2 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_2, weight=3)

        # Notebook, painel #2.
        self.notebook = ttk.Notebook(self.pane_2)
        self.notebook.pack(fill="both", expand=True)

        # Aba #1.
        self.tab_1 = ttk.Frame(self.notebook)
        for index in [0, 1]:
            self.tab_1.columnconfigure(index=index, weight=1)
            self.tab_1.rowconfigure(index=index, weight=1)
        self.notebook.add(self.tab_1, text="Aba #1.")

        # Escala.
        self.scale = ttk.Scale(
            self.tab_1,
            from_=100,
            to=0,
            variable=self.var_5,
            command=lambda event: self.var_5.set(self.scale.get()),
        )
        self.scale.grid(row=0, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")

        # Barra de progresso.
        self.progress = ttk.Progressbar(
            self.tab_1, value=0, variable=self.var_5, mode="determinate"
        )
        self.progress.grid(row=0, column=1, padx=(10, 20), pady=(20, 0), sticky="ew")

        # Label
        self.label = ttk.Label(
            self.tab_1,
            text="Tema Azure para ttk",
            justify="center",
            font=("-size", 15, "-weight", "bold"),
        )
        self.label.grid(row=1, column=0, pady=10, columnspan=2)

        # Aba #2
        self.tab_2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_2, text="Guia 2")

        # Aba #3
        self.tab_3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_3, text="Guia 3")

        # Punho de dimensionamento (ou tamanho)
        self.sizegrip = ttk.Sizegrip(self)
        self.sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("")


    # Simplesmente defina o tema
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")

    app = App(root)
    app.pack(fill="both", expand=True)

    # Defina um tamanho mínimo para a janela e coloque-a no centro
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

    root.mainloop()
