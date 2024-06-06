import PySimpleGUI as psg
psg.theme("DarkAmber")
layout=[[psg.Text("Simple Board",font=("Comic Sans MS", 15), justification="center")],]
button_array=[]
gap = 2
cols, rows = 5, 5
for y in range(0, 3):
    line = []
    for x in range(0, 3):
        x_pad = (gap, gap) if x==cols-1 else (gap, 0)
        y_pad = (gap, gap) if y==rows-1 else (gap, 0)
        pad = (x_pad, y_pad)
        line.append(
            psg.Button("", size=(10, 5), pad=pad, button_color="white", key=str((y, x)))
         )
    button_array.append(line)
layout=[[psg.Text("Simple Board",font=("Comic Sans MS", 15), justification="center")],[psg.Column(button_array)]]
win=psg.Window(title="Board", layout=layout, margins=(5, 5), size=(300,350), finalize=True)

while True:
    event,values=win.read()
    print(values)
    if event==psg.WIN_CLOSED:
        break
win.close()