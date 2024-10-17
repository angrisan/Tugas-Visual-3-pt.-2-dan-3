import PySimpleGUI as sg 
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Contoh Button",
                   layout=[[sg.Button("Contoh Button")],
                           [sg.Button("Botton Simpan")],
                           [sg.Button("Botton Keluar")]
                           ],
                           size=(400,200),
                           font=("Times",18),
                           icon=("favicon.ico"))
kejadian,nilai = window.read()
print(kejadian,"=>",nilai)
window.close()