from tkinter import *
window = Tk()
window.title('CT/2017/051 T.S.Robertson')
window.geometry('750x500')

option1 = [
    "Black Colour",
    "Blue Colour",
    "Green Colour",
    "Yellow Colour"]

option2 = [
    "0.5 Liter",
    "1 Liter",
    "1.5 Liter"]

option3 = [
    "Kids Drinking Bottle",
    "Sport Drinking Bottel",
    "Healthy Drinking Bottle"]

option4 = [
    "Standard Screw Cap",
    "Push-Pull Cap",
    "Kid-Friendly Cap",
    "Flip-Flop Cap"]

option5 = [
    "Fun Graphic",
    "Filter"]

clicked1 = StringVar()
clicked1.set(option1[0])

clicked2 = StringVar()
clicked2.set(option2[0])

clicked3 = StringVar()
clicked3.set(option3[0])

clicked4 = StringVar()
clicked4.set(option4[0])

clicked5 = StringVar()
clicked5.set(option5[0])

#------------------------create a frame-------------------------------
frame = LabelFrame(window, text='Topic of Manufacturing', padx='10', pady='10') #frame content padding
frame.pack(padx='5', pady='5') #frame padding

#-------------------------Heading one----------------
heading1 = Label(frame, text='Process of Bottle Manufacturing').grid(row='0', column='1', padx=5, pady=5)
#-------------------------Heading two----------------
heading2 = Label(frame, text='Design Your Own Bottle.').grid(row='1', column='1', padx=5, pady=5)

#------------------------------Label name & drop down-----------------------------------------
firstSelection = Label(frame, text='Select your Preferred Color :').grid(row='2', column='0', sticky='w', padx=5, pady=5)
firstDrop = OptionMenu(frame, clicked1, *option1)
firstDrop.grid(row='2',column='1', sticky='w', padx=5, pady=5)
firstDrop.config(width=20)

secondSelection = Label(frame, text='Select your Preferred Size :').grid(row='3', column='0', sticky='w', padx=5, pady=5)
secondDrop = OptionMenu(frame, clicked2, *option2)
secondDrop.grid(row='3',column='1', sticky='w', padx=5, pady=5)
secondDrop.config(width=20)

thirdSelection = Label(frame, text='Select your Preferred Bottle Type :').grid(row='4', column='0', sticky='w', padx=5, pady=5)
thirdDrop = OptionMenu(frame, clicked3, *option3)
thirdDrop.grid(row='4',column='1', sticky='w', padx=5, pady=5)
thirdDrop.config(width=20)

fourthSelection = Label(frame, text='Select your Preferred type of Bottle Cap :').grid(row='5', column='0', sticky='w', padx=5, pady=5)
fourthDrop = OptionMenu(frame, clicked4, *option4)
fourthDrop.grid(row='5',column='1', sticky='w', padx=5, pady=5)
fourthDrop.config(width=20)

fifthSelection = Label(frame, text='Select your Preferred other option :').grid(row='6', column='0', sticky='w', padx=5, pady=5)
fifthDrop = OptionMenu(frame, clicked5, *option5)
fifthDrop.grid(row='6',column='1', sticky='w', padx=5, pady=5)
fifthDrop.config(width=20)

#-------------------WHat happen when click the submitBut--------------
def condtion():
    global pop
    pop = Toplevel(window)
    pop.title('My pop')
    pop.geometry('600x50')

    bottle_type_input = clicked3.get()
    bottle_cap_input = clicked4.get()
    other_option_input = clicked5.get()

#---------------------------System design condition checked------------------------------------------
    if ((bottle_type_input == 'Kids Drinking Bottle') and (bottle_cap_input == 'Kid-Friendly Cap') or
        (bottle_type_input == 'Healthy Drinking Bottle') and (bottle_cap_input == 'Filter')):
        pop_label = Label(pop, text='input').pack()
    else:
        pop_label = Label(pop, text='Your design is not agreed with system conditions. Please re-checked it and try.').pack()

#-------------------Submit Button-----------------------------
submitBut = Button(frame, text='submit your design', command=condtion, pady=4, padx=4).grid(row='7', column='2', sticky='w', padx=5, pady=5)

window.mainloop()