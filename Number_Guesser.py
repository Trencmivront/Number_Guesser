import customtkinter
import time

customtkinter.set_appearance_mode("white")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()

root.geometry("450x300")
root.resizable(False, False)

frame = customtkinter.CTkFrame(master = root, width = 450, height = 300)
frame.pack(pady = 20, padx = 60, fill = "both")




def final_screen(number):
    final_frame = customtkinter.CTkFrame(master = root, width = 450, height = 300)
    final_frame.pack(pady = 20, padx = 60, fill = "both")

    def no_screen():
        final_frame.destroy()

        no_frame = customtkinter.CTkFrame(master = root, width = 450, height = 300)
        no_frame.pack(pady = 20, padx = 60, fill = "both")
    
        byby = customtkinter.CTkLabel(master = no_frame, text = "YOU ARE GAY", bg_color = "white", text_color = "black", font = ("Roboto", 30))
        byby.pack(pady = 40, padx = 60, side = "top")

        e_xt = customtkinter.CTkButton(master = no_frame, text = "Exit", command = exit)
        e_xt.pack(pady = 20, padx = 60, side = "bottom")
    

    def yes_screen():
        final_frame.destroy()

        yes_frame = customtkinter.CTkFrame(master = root, width = 450, height = 300)
        yes_frame.pack(pady = 20, padx = 60, fill = "both")
    
        byby = customtkinter.CTkLabel(master = yes_frame, text = "Allright! Have a nice day!", text_color = "white", font = ("Roboto", 19))
        byby.pack(pady = 40, padx = 60, side = "top")

        e_xt = customtkinter.CTkButton(master = yes_frame, text = "Exit", command = exit)
        e_xt.pack(pady = 20, padx = 60, side = "bottom")


    answer = customtkinter.CTkLabel(master = final_frame, text = f"Your number is {number}\n\nIs that correct?", text_color = "skyblue" , font = ("Roboto", 25))
    answer.pack(pady = 20, padx = 60, side = "top")

    yes = customtkinter.CTkButton(master = final_frame, width = 30, height = 20, text = "Yes", command = yes_screen)
    yes.pack(pady = 20, padx = 60, side = "left")

    no = customtkinter.CTkButton(master = final_frame, width = 30, height = 20, text = "No", command = no_screen)
    no.pack(pady = 20, padx = 60, side = "right")


def loading_screen():
    number = entry.get()

    frame.destroy()

    frame_2 = customtkinter.CTkFrame(master = root, width = 450, height = 300)
    frame_2.pack(pady = 20, padx = 60, fill = "both")

    headline = customtkinter.CTkLabel(master = frame_2, text = "Guessing...", font = ("Roboto", 20))
    headline.pack(pady = 20, padx = 60)

    bar = customtkinter.CTkProgressBar(master = frame_2)
    bar.pack(pady = 20, side =  "top")

    def bar_load(value = 0):
        for i in range(101):
            bar.set(i/100)
            root.update()
            time.sleep(0.03)
        frame_2.destroy()
        final_screen(number)
    bar_load()




label = customtkinter.CTkLabel(master = frame, text = "Number Guesser", text_color = "white", font = ("Roboto", 24))
label.pack(pady = 20, padx = 60)

entry = customtkinter.CTkEntry(master = frame, placeholder_text = "Enter the number on your mind", width = 200, height = 40)
entry.pack(pady = 20, padx = 60)

button = customtkinter.CTkButton(master = frame, text = "guess my number", width = 150, height = 50, command = loading_screen)
button.pack(pady = 40, padx = 30)

root.mainloop()
