from tkinter import * #importe tout de Tkinter


def window_storie():
    window = Tk() #La fenêtre afficher est Tkinter
    window.iconbitmap("soul_logo.ico") #Configure le logo de la fenêtre (.ico)
    window.geometry("1366x768") #Configure la taille de la fenêtre
    window.resizable(height=False,width=False) #Empêche de pouvoir modifier la taille de la fenêtre
    window.title("Light Your Soul") #Configure le nom de la fenêtre
    window.config(background='black') #Séléctionne la couleur du fond de la fenêtre de jeu

    background = PhotoImage(file = "maison_pote_joueur.png") #Variable pour dire que l'image est là
    show_background = Canvas(window, width=1366, height=580, bd=7.5, background = 'black', relief=RIDGE, highlightthickness= 0) #Caractéristiques de l'image
    id_background=show_background.create_image(683,200,image=background) #place l'image dans la fenêtre
    show_background.image = background
    show_background.pack() #Pour dire à Tkinter d'utiliser l'image


    nombre_clic  = IntVar(window,value=0) #Nombre de clic par rapport un endroit choisit de la fenêtre
    def add_passage (window,texte_scenario,id_background,show_background):
        temp= nombre_clic.get()
        if temp == 0 :
            lieu_texte_scenario.config(text="Vous") #Défini le texte à l'edroit où sont placer les variables
            texte_scenario.config(text="*Vous vous relevez*") #idem
            texte_scenario_2.config(text="") #idem
            nombre_clic.set( nombre_clic.get() + 1 ) #Incrémente de 1 le nombre de clic
        elif temp == 1 :
            image= PhotoImage(file="maison_pote_joueur_2.png") 
            show_background.itemconfigure(id_background,image = image) #Change l'image actuelle par une autre
            show_background.image = image
            lieu_texte_scenario.config(text="...")
            texte_scenario.config(text="-Ahhh un mort vivant !!")
            texte_scenario_2.config(text="")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 2 :
            lieu_texte_scenario.config(text="Vous")
            texte_scenario.config(text="*Vous vous dépoussièrez*")
            texte_scenario_2.config(text="")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 3 :
            lieu_texte_scenario.config(text="...")
            texte_scenario.config(text="-Oh, mais c’est toi, comment vas-tu ? Pas trop mal je suppose, tu as une meilleure tête que d’habitude.")
            texte_scenario_2.config(text="Quel… Hhmmm… plaisir de te retrouver.")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 4 :
            lieu_texte_scenario.config(text="Vous")
            texte_scenario.config(text="Qui es-tu ?")
            texte_scenario_2.config(text="")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 5 :
            lieu_texte_scenario.config(text="...")
            texte_scenario.config(text="Quoi ? Comment ça ?")
            texte_scenario_2.config(text="Tu ne vas pas me dire que tu as oublié ton meilleur pote ? Jacque Asseur")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 6 :
            lieu_texte_scenario.config(text="Vous")
            texte_scenario.config(text="J’ai mal partout, on est où ?")
            texte_scenario_2.config(text="")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 7 :
            lieu_texte_scenario.config(text="Jacque Asseur")
            texte_scenario.config(text="Je voie, je suppose que tu as une perte de mémoire à cause de l’accident.")
            texte_scenario_2.config(text="Vue qu’on est meilleur amis… Même si t’en souviens pas sale ingrat… Je vais t’aider…")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 8 :
            lieu_texte_scenario.config(text="Jacque Asseur")
            texte_scenario.config(text="Alors…")
            texte_scenario_2.config(text="Hhmmm…")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 9 :
            lieu_texte_scenario.config(text="Jacque Asseur")
            texte_scenario.config(text="Tu t’appelles comment déjà ?")
            texte_scenario_2.config(text="")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 10 :
            lieu_texte_scenario.config(text="Vous")
            texte_scenario.config(text="...")
            texte_scenario_2.config(text="*Vous dites votre Prénom")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 11 :
            lieu_texte_scenario.config(text="Jacque Asseur")
            texte_scenario.config(text="Haha… comme ma grand-mère.")
            texte_scenario_2.config(text="Espérons que ça revienne à la mode.")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 12 :
            lieu_texte_scenario.config(text="Système")
            texte_scenario.config(text="-@ Vous avez débloquez la capacité : Le seum @-")
            texte_scenario_2.config(text="-@ Vous avez débloquez la capacité : Cassage de Gueule @-")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 13 :
            lieu_texte_scenario.config(text="Jacque Asseur")
            texte_scenario.config(text="Allez salut")
            texte_scenario_2.config(text="...")
            nombre_clic.set( nombre_clic.get() + 1 )
        else :
            window.destroy() #Ferme la fenêtre

    lieu_texte_scenario = LabelFrame(window, text="..." ,font=("ALGERIAN",30), bg= 'black',fg='white',relief=RIDGE, bd=7.5,) #Choisi les caractéristiques de la poolice et l'emplacement
    lieu_texte_scenario.pack(side=BOTTOM)
    texte_scenario=Label(lieu_texte_scenario, text="Heeeeeyyyyy !",width=90, font=("Bahnschrift Condensed",25) , bg= 'black',fg='white') #Choisi les caractéristiques de la poolice et l'emplacement
    texte_scenario.grid(row=0,column=0)
    texte_scenario_2=Label(lieu_texte_scenario, text="Vous êtes en vie ? Vous m’entendez ?",width=90, font=("Bahnschrift Condensed",25) , bg= 'black',fg='white') #Choisi les caractéristiques de la poolice et l'emplacement
    texte_scenario_2.grid(row=1,column=0)
    bouton_image =PhotoImage(file="doigt_montre.png").zoom(10) .subsample(50) #Change caractéristique de l'image taille et emplacement
    bouton_scenario=Button(lieu_texte_scenario,image=bouton_image,bg='black',bd =0 ,width=165,height=110, highlightthickness= 0, command= lambda :add_passage(window,texte_scenario,id_background,show_background)) #Choisi les caractéristiques de l'image et ce qui se passe quand on clique dessus
    bouton_scenario.grid(row=0,column=1,rowspan=2) #Emplacement de l'image/bouton
    window.mainloop() #Permet d'avoir la fenêtre ouverte (toujours à la fin)