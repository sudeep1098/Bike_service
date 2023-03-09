from tkinter import *
window = Tk()
window.title("Bike Service")
window.geometry("800x600+300+100")

photo = PhotoImage(file="./bike.png")
myimg = Label(image=photo).place(x=300, y=50)


def start():
    start_button.destroy()

    def buy():
        user_label.destroy()
        dict = {"suzuki": [16, 50000], "pulser": [18, 60000],
                "ktm": [10, 70000], "duke": [7, 80000], }
        bike_label = Label(window, text="Which bike do you want to buy:\n Suzuki ,Pulser ,KTM ,Duke",
                           font=("arial", 20, "bold"), bg="yellow", fg="red")
        bike_label.place(x=200, y=300)

        bike_var = StringVar()

        bikeEntry = Entry(window, textvariable=bike_var,
                          width=20, font=20, bd=2)
        bikeEntry.place(x=320, y=400)

        def bought():

            if (bikeEntry.get() == "suzuki") or (bikeEntry.get() == "pulser") or (bikeEntry.get() == "ktm") or (bikeEntry.get() == "duke"):
                x = Label(text=f"{bike_var.get()} price is {dict[bike_var.get()][1]}\nOur stock is {dict[bike_var.get()][0]}", font=(
                    "arial", 20, "bold"), fg="black")
                x.place(x=290, y=410)
                bike_label.destroy()
                bikeEntry.destroy()
                a = Label(text="Do you wish to buy?", font=(
                    "arial", 20, "bold"), bg="yellow", fg="red")
                a.place(x=280, y=300)

                def submitting():
                    a.destroy()
                    x.destroy()
                    back.destroy()

                    Label(text=f"{bike_var.get()} is Successfully Purchased\nThank You", font=(
                        "arial", 20, "bold"), fg="black").place(x=200, y=300)
                    submit.destroy()

                submit = Button(text="Submit", font=("arial", 15, "bold"), width=7,
                                height=1, fg="red", bg="yellow", command=submitting)
                submit.place(x=430, y=360)
                buy_submit.destroy()

                def goback():
                    buy()
                    a.destroy()
                    x.destroy()
                    back.destroy()
                    submit.destroy()

                back = Button(text="Back", font=("arial", 15, "bold"), width=7,
                              height=1, fg="red", bg="yellow", command=goback)
                back.place(x=280, y=360)

            else:
                c = Label(text=f"{bikeEntry.get()} is not in the lists", font=(
                    "arial", 20, "bold"), fg="black")
                c.place(x=250, y=510)

        buy_submit = Button(text="Submit", font=("arial", 20, "bold"), width=10,
                            height=1, fg="red", bg="yellow", command=bought)
        buy_submit.place(x=325, y=450)

        buy_button.destroy()
        rent_button.destroy()

    buy_button = Button(window, text="Buy", font=(
        "arial", 20, "bold"), bg="yellow", fg="red", command=buy)
    buy_button.place(x=300, y=350)

    def rent():
        user_label.destroy()
        dict = {"suzuki": [1, 2000], "pulser": [1, 3000],
                "ktm": [1, 4000], "duke": [1, 5000], }
        bike_label = Label(window, text="Which bike do you want to rent:\n Suzuki ,Pulser ,KTM ,Duke",
                           font=("arial", 20, "bold"), bg="yellow", fg="red")
        bike_label.place(x=200, y=300)

        bike_var = StringVar()

        bikeEntry = Entry(window, textvariable=bike_var,
                          width=20, font=20, bd=3)
        bikeEntry.place(x=320, y=400)

        def rented():

            if (bikeEntry.get() == "suzuki") or (bikeEntry.get() == "pulser") or (bikeEntry.get() == "ktm") or (bikeEntry.get() == "duke"):
                y = Label(text=f"{bike_var.get()} 1 day rent is {dict[bike_var.get()][1]}", font=(
                    "arial", 20, "bold"), fg="black")
                y.place(x=270, y=430)
                bike_label.destroy()
                bikeEntry.destroy()
                b = Label(text="Do you wish to buy?", font=(
                    "arial", 20, "bold"), bg="yellow", fg="red")
                b.place(x=280, y=300)

                def submitting():
                    b.destroy()
                    y.destroy()
                    Label(text=f"{bike_var.get()} is Successfully Rented\nThank You", font=(
                        "arial", 20, "bold"), fg="black").place(x=240, y=310)
                    submit.destroy()

                submit = Button(text="Submit", font=("arial", 20, "bold"), width=10,
                                height=1, fg="red", bg="yellow", command=submitting)
                submit.place(x=325, y=350)
                rent_submit.destroy()
            else:
                Label(text=f"{bikeEntry.get()} is not in the lists", font=(
                    "arial", 20, "bold"), fg="black").grid(row=2, column=0).place(x=250, y=510)

        rent_submit = Button(text="Submit", font=("arial", 20, "bold"), width=10,
                             height=1, fg="red", bg="yellow", command=rented)
        rent_submit.place(x=325, y=450)

        buy_button.destroy()
        rent_button.destroy()

    rent_button = Button(window, text="Rent", font=(
        "arial", 20, "bold"), bg="yellow", fg="red", command=rent)
    rent_button.place(x=450, y=350)


user_label = Label(window, text="Welcome to bike services",
                   font=("arial", 20, "bold"), bg="yellow", fg="red")
user_label.place(x=240, y=300)

start_button = Button(window, text="Start", font=(
    "arial", 20, "bold"), bg="yellow", fg="red", command=start)
start_button.place(x=370, y=350)


window.mainloop()
