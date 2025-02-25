import customtkinter

# GUI Setup

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


root = customtkinter.CTk()
root.geometry("700x700")
root.title("Dr. Akash - Emotinal Support Bot")

label = customtkinter.CTkLabel(master=root, text="What can I do for you today?", font=("Arial", 24), pady=50)
label.pack(pady=5, padx=10)

prompt_entry = customtkinter.CTkEntry(master=root, placeholder_text="Enter any of your concerns here")
prompt_entry.pack(pady=20, padx=10, ipadx=35)

text_box = customtkinter.CTkTextbox(master=root)
text_box.pack()

root.mainloop()
