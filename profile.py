import PySimpleGUI as sg 
window = sg.Window(title="Profile",
                   layout=[[sg.Text("NPM    : 2210010366")],
                           [sg.Text("NAMA   : Angri Santoso")],
                           [sg.Text("KELAS  : 5E Reguler Banjarmasin")],
                           [sg.Text("MATKUL : PEMROGRAMAN VISUAL 2")]],
                           size=(400,200))
window()
window.close()