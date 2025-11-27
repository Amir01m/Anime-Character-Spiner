from tkinter import *
import random
#characters and colors
character_colors = {
    # COMMON
    "Sakura (Naruto)": "dimgray",
    "Usopp (One Piece)": "dimgray",
    "Yajirobe (Dragon Ball)": "dimgray",
    "Iruka (Naruto)": "dimgray",
    "Kon (Bleach)": "dimgray",

    # UNCOMMON
    "Rock Lee (Naruto)": "green",
    "Krillin (Dragon Ball)": "green",
    "Chopper (One Piece)": "green",
    "Kuwabara (Yu Yu Hakusho)": "green",
    "Shino (Naruto)": "green",

    # RARE
    "Zoro (One Piece)": "blue",
    "Vegeta (Dragon Ball)": "blue",
    "Kakashi (Naruto)": "blue",
    "Ichigo (Bleach)": "blue",
    "Killer Bee (Naruto)": "blue",

    # EPIC
    "Gojo Satoru (JJK)": "purple",
    "Madara Uchiha (Naruto)": "purple",
    "Yamamoto (Bleach)": "purple",
    "Aizen (Bleach)": "purple",
    "Sukuna (JJK)": "purple",

    # LEGENDARY
    "Naruto Uzumaki": "darkorange",
    "Goku": "darkorange",
    "Monkey D. Luffy": "darkorange",
    "Saitama": "darkorange",
    "Isaac Netero (HXH)": "darkorange"
}
#Character Class
class Characters:
    def __init__(self):
        pass
    def common(self):
        spin_list = [
            "Sakura (Naruto)",
            "Usopp (One Piece)",
            "Yajirobe (Dragon Ball)",
            "Iruka (Naruto)",
            "Kon (Bleach)"
        ]
        weights = [40, 25, 15, 10, 10]
        choice = random.choices(spin_list, weights=weights)
        return choice[0]

    def uncommon(self):
        spin_list = [
            "Rock Lee (Naruto)",
            "Krillin (Dragon Ball)",
            "Chopper (One Piece)",
            "Kuwabara (Yu Yu Hakusho)",
            "Shino (Naruto)"
        ]
        weights = [30, 25, 20, 15, 10]
        choice = random.choices(spin_list, weights=weights)
        return choice[0]

    def rare(self):
        spin_list = [
            "Zoro (One Piece)",
            "Vegeta (Dragon Ball)",
            "Kakashi (Naruto)",
            "Ichigo (Bleach)",
            "Killer Bee (Naruto)"
        ]
        weights = [25, 25, 20, 15, 15]
        choice = random.choices(spin_list, weights=weights)
        return choice[0]

    def epic(self):
        spin_list = [
            "Gojo Satoru (JJK)",
            "Madara Uchiha (Naruto)",
            "Yamamoto (Bleach)",
            "Aizen (Bleach)",
            "Sukuna (JJK)"
        ]
        weights = [30, 25, 15, 15, 15]
        choice = random.choices(spin_list, weights=weights)
        return choice[0]

    def legendry(self):
        spin_list = [
            "Naruto Uzumaki",
            "Goku",
            "Monkey D. Luffy",
            "Saitama",
            "Isaac Netero (HXH)"
        ]
        weights = [25, 25, 20, 20, 10]
        choice = random.choices(spin_list, weights=weights)
        return choice[0]

    def mythic(self):
        spin_list = [
            "Zeno (DB Super)",
            "The Presence (DC)",
            "One Above All (Marvel)",
            "Kami Tenchi",
            "Featherine (Umineko)"
        ]
        weights = [20, 20, 20, 20, 20]    
        choice = random.choices(spin_list, weights=weights)
        return choice[0]
def c_common():
    fg = "white"
    return fg

#defs
def show_real():
    global ch, fg
    label.config(text=ch, fg=fg)
    btn.config(state="normal")

def animtaion(frame=0):
    global sec, shuffled_names
    fake_names = shuffled_names[frame % len(shuffled_names)]
    label.config(text=fake_names, fg=character_colors[fake_names])
    
    if frame <=20 and frame > 10:
        sec += 60
        root.after(sec+20, animtaion, frame+1)
    elif frame <= 20:    
        root.after(60, animtaion, frame+1)
    else:
        show_real()

def spin_delay():
    global shuffled_names
    btn.config(state="disabled")
    shuffled_names = list(character_colors.keys())
    random.shuffle(shuffled_names)
    global sec
    sec = 30
    animtaion()
    btn.after(80)
    btn.config(state="active")

#def spin
c=20
edame = True
def spin():
    global c 
    global edame
    global ch,fg
    c-=1
    if c <= -1:
        edame = False
    if edame == True:
        ch = ""
        char = Characters()
        spin_list = ['common',"uncommon","rare","epic","legendry","mythic"]
        choice = random.choices(spin_list,weights=[6.2,2.0,1.0,0.5,0.25,0.05])
        if choice[0] == spin_list[0]:
            ch = char.common()
            fg = "dimgray"
        elif choice[0] == spin_list[1]:
            ch = char.uncommon()
            fg = "green"
        elif choice[0] == spin_list[2]:
            ch = char.rare() 
            fg = "blue"
        elif choice[0] == spin_list[3]:
            ch = char.epic()
            fg = "purple"
        elif choice[0] == spin_list[4]:
            ch = char.legendry()
            fg = "darkorange"
        elif choice[0] == spin_list[5]:
            ch = char.mythic() 
            fg = "red"
        
        spin_delay()
        btn.config(state="disabled")
        label.config(text=ch,fg=fg)
        label1.config(text=c)
        
        

#Main
root = Tk()
root.geometry("400x400")
root.title("Anime Character Spiner")
root.resizable(0,0)

#Buttons
btn = Button(root,text="Spin",command=spin,width=10,height=3,fg="red")
btn.place(x=157,y=200)

btne = Button(root,text="Exit",command=exit)
btne.place(x=20,y=20)

#Labels
label = Label(root,text="None",bg="lightgray",width=22,height=2,border=1,relief="solid")
label.place(x=120,y=120)
label1 = Label(root,text="20")
label1.place(x=187,y=90)
#Menus



root.mainloop()
