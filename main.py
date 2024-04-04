import customtkinter
from random import choice


def generate_password():
    """
    Function takes in the contents of entry field and, if it's a valid entry, creates a randomised password
    at the indicated length.
    """
    try:
        # Take in the number of characters wanted from the input field.
        no_of_characters = int(character_count_entry.get())

        # Define available characters for the password generator.
        password_characters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890!?-')
        output_password = ""

        # For the amount of characters specified, pick a random character and append to an output variable
        for i in range(no_of_characters):
            output_character = choice(password_characters)
            output_password += output_character

        character_count_entry.delete(0, 'end')
        character_count_entry.insert(0, output_password)

    except ValueError:
        print("Error: Enter an integer.")


# Create a global font tuple for input fields.
button_font = ("Arial", 20, "bold")

# Setting the theme to dark mode with dark blue accent.
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Initial window setup, title, screensize etc.
root = customtkinter.CTk()
root.title("Random Pass")
root.geometry("400x200")
root.resizable(False, False)

# Label to put a title on the whole thing - could use logo in future.
application_title_label = customtkinter.CTkLabel(root, text="RandomPass", font=("Arial", 40, "bold"))
application_title_label.place(relx=0.5, rely=0.2, anchor="center")

# Number of character input entry field
character_count_entry = customtkinter.CTkEntry(root, placeholder_text="No. Characters")
character_count_entry.place(relx=0.5, rely=0.45, anchor="center")
character_count_entry.configure(width=350)

# This is the button that generates the random password, function needs to be attached.
generate_password_button = customtkinter.CTkButton(root, text="Generate", command=generate_password, font=button_font)
generate_password_button.configure(height=50, width=200)
generate_password_button.pack()
generate_password_button.place(relx=0.5, rely=0.75, anchor="center")

# Start the application.
root.mainloop()
