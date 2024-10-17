import PySimpleGUI as sg 
susunan=[[sg.Push(),
          sg.Text("UNISKA MAB",font=("Helvetica",24)),
          sg.Push()],
          [sg.Push(),
           sg.Text("BANJARMASIN" ,font=("Courier",18)),
           sg.Push()]
           ]
window = sg.Window(title="elemen Text",
                   layout=susunan,
                   size=(430,200))
window()
window.close()