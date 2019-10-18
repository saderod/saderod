import tkinter as tk
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox
import time

WIDTH = 1525
HEIGHT = 900

#generates the window canvas
root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#4d067d')
canvas.pack()

#stacked under the canvas window
# relx and rely are used to center the frame, it changes the origin location which is usually on the top left corner,
# rel height and relweidth change how wide the rectangle becomes (or narrow or shorter)*+
frame = tk.Frame(root, bg='#8d20d6')
frame.place(relx=0.01, rely=0.06, relwidth=0.98, relheight=0.82)


label = tk.Label(frame, text="What is the best Mega Genger for Team C", fg='red', bg='black', font=('Courier ', 13))
label.place(relx=0.38, rely=0, relwidth=0.25, relheight=0.07)

labeltwo = tk.Label(frame, text="Team C is comprised of Mega Gengar, Raichu, Blaziken and Venasaur. You are going to pick moves for Mega Gengar. Their technical data is shown next to them. Pick one move per list that best fit Mega \n Gengar in a VGC dooubles format battle.Gengar already has the move Protect. Type the corresponding letter (lower case only) of the chosen move from each move list in the entry box next to the \n corresponding color. Then type any advice for building the team in the entry box below where labeled. Once done, hit submit button", fg='white', bg='black', font=('Courier ', 10))
labeltwo.place(relx=0.025, rely=0.075, relwidth=.95, relheight=0.1)

labelthree = tk.Label(frame, fg='white', bg='black', font=('Courier ', 10), text="role: Sp Sweeper \n\n\n weakness: Ground \n\n\n resist: Fly, Steel, Elec \n\n\n item: Focus Sash \n\n\n ability: Lightning Rod \n\n\n moves: Thunder Bolt \n\n Thunder Wave, \n\n Calm Mind, \n\n Protect ")
labelthree.place(relx=0.45, rely=0.2, relwidth=0.118, relheight=0.46)

labeleight = tk.Label(frame, fg='white', bg='black', font=('Courier ', 10), text="role: Ph Sweeper \n\n\n weakness: Fly, Wat, Psy \n\n\n resist: Bug, Steel, Fire \n\n\n item: Choice Band \n\n\n ability: Blaze \n\n\n moves: High Jump Kick, \n\n Blaze Kick, \n\n Night Slash, \n\n Rock Slide")
labeleight.place(relx=0.67, rely=0.2, relwidth=0.118, relheight=0.46)

labeleight = tk.Label(frame, fg='white', bg='black', font=('Courier ', 10), text="role: Support Tank \n\n\n weakness: Fl, Fir, Ice \n\n\n resist: Fi, Wat, Fai \n\n\n item: Sitrus Berry \n\n\n ability: Overgrow \n\n\n moves: Sleep Powder, \n\n Leech Seed, \n\n Mega Drain, \n\n Sludge Bomb")
labeleight.place(relx=0.89, rely=0.2, relwidth=0.118, relheight=0.46)

labeleleven = tk.Label(frame, fg='white', bg='black', font=('Courier ', 10), text="Hp 60 \n\n Atk 65 \n\n Def 80 \n\n Sp Atk 170 \n\nSp Def 95 \n\n Speed 130")
labeleleven.place(relx=0.55, rely=0.68, relwidth=0.065, relheight=0.3)

bg_image = ImageTk.PhotoImage(Image.open("Raichu.gif"))
labelfour = tk.Label(frame, fg='white', bg='black', font=('Courier ', 10), image=bg_image)
labelfour.place(relx=0.35, rely=0.26, relwidth=0.1, relheight=0.4)

bg_image_two = ImageTk.PhotoImage(Image.open("blaziken.jpg"))
labelseven = tk.Label(frame, fg='white', bg='black', font=('Courier ', 10), image=bg_image_two)
labelseven.place(relx=0.57, rely=0.26, relwidth=0.1, relheight=0.4)

bg_image_three = ImageTk.PhotoImage(Image.open("venusaur.jpg"))
labelnine = tk.Label(frame, fg='white', bg='black', font=('Courier ', 10), image=bg_image_three)
labelnine.place(relx=0.79, rely=0.26, relwidth=0.1, relheight=0.4)

bg_image_four = ImageTk.PhotoImage(Image.open('venusaur.jpg'))
labelten = tk.Label(frame, image=bg_image_four)
labelten.place(relx=0.35, rely=0.68, relwidth=0.2, relheight=0.3)

labelfive = tk.Label(frame, bg="red", text="Move List 1")
labelfive.place(relx=0.01, rely=0.18, relwidth=0.334, relheight=0.05)

labelsix = tk.Label(frame, bg="blue", text="Move List 2")
labelsix.place(relx=0.01, rely=0.42, relwidth=0.334, relheight=0.05)

labelseven = tk.Label(frame, bg="green", text="Move List 3")
labelseven.place(relx=0.01, rely=0.66, relwidth=0.334, relheight=0.05)

scrollbar = tk.Scrollbar(frame)
scrollbar.place(relx=0.334, rely=0.23, relwidth=0.01, relheight=0.12)

scrollbartwo = tk.Scrollbar(frame)
scrollbartwo.place(relx=0.334, rely=0.47, relwidth=0.01, relheight=0.12)

scrollbarthree = tk.Scrollbar(frame)
scrollbarthree.place(relx=0.334, rely=0.71, relwidth=0.01, relheight=0.12)

listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, font=("Verdana", 16))
listbox.place(relx=0.01, rely=0.23, relwidth=0.325, relheight=0.12)
listbox.insert(0, "(a) Shadowball / Ghost / 80 Pwr / 100 Acc")
listbox.insert(1, "(b) Dark Pulse / Dark / 80 Pwr / 100 Acc")
listbox.insert(2, "(c) Dream Eater / Psy / 100 Pwr / 100 Acc")
listbox.insert(3, "(d) Sludge Bomb / Pois / 90 Pwr / 100 Acc")
listbox.insert(4, "(e) Hyper Beam / Norm / 150 Pwr / 100 Acc")
listbox.insert(5, "(f) Mega Drain / Gra / 75 Pwr / 100 Acc")
listbox.insert(6, "(g) Dazzling Gleam / Fair / 80 Pwr / 100 Acc")

listboxtwo = tk.Listbox(frame, yscrollcommand=scrollbartwo.set, font=("Verdana", 16))
listboxtwo.place(relx=0.01, rely=0.47, relwidth=0.325, relheight=0.12)
listboxtwo.insert(0, "(h) Thunderbolt / Elec / 90 Pwr / 100 Acc")
listboxtwo.insert(1, "(i) Psychic / Pys / 90 Pwr / 100 Acc")
listboxtwo.insert(2, "(j) Focus Blast / Fighting / 120 Pwr / 70 Acc")
listboxtwo.insert(3, "(k) Energy Ball / Gra / 90 Pwr / 100 Acc")
listboxtwo.insert(4, "(l) Venoshock / Pois / 65 Pwr / 100 Acc")
listboxtwo.insert(5, "(m) Thunder / Elec / 110 Pwr / 100 Acc")
listboxtwo.insert(6, "(n) Hex / Gho / 65 Pwr / 100 Acc")

listboxthree = tk.Listbox(frame, yscrollcommand=scrollbarthree.set, font=("Verdana", 16))
listboxthree.place(relx=0.01, rely=0.71, relwidth=0.325, relheight=0.12)
listboxthree.insert(0, "(o) Haze / Removes all stat buffs / 110 Acc")
listboxthree.insert(1, "(p) Hypnosis / Sleep inducer / 60 Acc")
listboxthree.insert(2, "(q) Confuse Ray / Confusion inducer / 100 Acc")
listboxthree.insert(3, "(r) Toxic / Poisons target / 90 Acc")
listboxthree.insert(4, "(s) Will-O-Wisp / Fire / Burns / 85 Acc")
listboxthree.insert(5, "(t) Taunt / Only allows damage moves / 100 Acc")
listboxthree.insert(6, "(u) Rest / User sleeps / 110 Acc")

scrollbar.config(command=listbox.yview)
scrollbartwo.config(command=listboxtwo.yview)
scrollbarthree.config(command=listboxthree.yview)


moveselectionlabelone = tk.Label(frame, bg="red", text="Type Move 1 Letter Here --> ")
moveselectionlabelone.place(relx=0.62, rely=0.703, relwidth=0.11, relheight=0.077)

moveselectionlabeltwo = tk.Label(frame, bg="blue", text="Type Move 2 Letter Here -->")
moveselectionlabeltwo.place(relx=0.62, rely=0.782, relwidth=0.11, relheight=0.077)

moveselectionlabelthree = tk.Label(frame, bg="green", text="Type Move 3 Letter Here -->")
moveselectionlabelthree.place(relx=0.62, rely=0.86, relwidth=0.11, relheight=0.078)

moveselected = StringVar()
moveselected.set("Move Selected Goes Here")

vallist = ["a", "b", "c", "d", "e", "f", "g"]
vallisttwo = ["h", "i", "j", "k", "l", "m", "n"]
vallistthree = ["o", "p", "q", "r", "s", "t", "u"]

def SaveToDb():
    database = mysql.connector.connect(host="localhost", user="root", password="Rodsader1*", database="Gengar")
    cursor = database.cursor()
    val = selectedentryone.get()
    valtwo = selectedentrytwo.get()
    valthree = selectedentrythree.get()
    valfour = feedback.get()
    cursor.execute("insert into GengarApp(MoveSelection1, MoveSelection2, MoveSelection3, Feedback) values(%s, %s, %s, %s)", (str(val), str(valtwo), str(valthree), str(valfour),))
    database.commit()
    if val not in vallist:
        messagebox.showerror("Error", "Remember to use lower case letters and check that the letter written in the entry box corresponds to the correct move list")
    elif valtwo not in vallisttwo:
        messagebox.showerror("Error", "Remember to use lower case letters and check that the letter written in the entry box corresponds to the correct move list")
    elif valthree not in vallistthree:
        messagebox.showerror("Error", "Remember to use lower case letters and check that the letter written in the entry box corresponds to the correct move list")
    else:
        messagebox.showinfo("Submitted", "Thank you for you input, press ok to close the window")
    cursor.close()
    database.close()
    time.sleep(2)
    root.quit()


selectedentryone = tk.Entry(frame)
selectedentryone.place(relx=0.73, rely=0.7, relwidth=0.05, relheight=0.08)

selectedentrytwo = tk.Entry(frame)
selectedentrytwo.place(relx=0.73, rely=0.78, relwidth=0.05, relheight=0.08)

selectedentrythree = tk.Entry(frame)
selectedentrythree.place(relx=0.73, rely=0.86, relwidth=0.05, relheight=0.08)


feedback = tk.Entry(frame)
feedback.place(relx=0.78, rely=0.76, relwidth=0.2, relheight=0.06)

feedbacklabel = tk.Label(frame, text="Type Any Feedback for Building Team C Below")
feedbacklabel.place(relx=0.78, rely=0.7, relwidth=0.2, relheight=0.06)

movesubmit = tk.Button(frame, text="Submit", command=SaveToDb, bg="black", fg="white")
movesubmit.place(relx=0.78, rely=0.82, relwidth=0.2, relheight=0.12)

labeltwelve = tk.Label(frame, bg="grey", text="Raichu")
labeltwelve.place(relx=0.35, rely=0.2, relwidth=0.1, relheight=0.06)

labelthirteen = tk.Label(frame, bg="grey", text="Blaziken")
labelthirteen.place(relx=0.57, rely=0.2, relwidth=0.1, relheight=0.06)

labelfourteen = tk.Label(frame, bg="grey", text="Venusaur")
labelfourteen.place(relx=0.79, rely=0.2, relwidth=0.1, relheight=0.06)

#call command
root.mainloop()


