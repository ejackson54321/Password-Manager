from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
EMAIL = " " #Enter your email address here in quotes.
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave a field blank")
    else:
        try:
            with open("data.json", "r") as file:
                #Reading old data
                data = json.load(file)
        except ValueError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                #Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
# ---------------------------- SEARCH BUTTON ------------------------------- #

def search():
    website = website_input.get()
    if len(website) > 0:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\n"
                                                           f"Password: {data[website]['password']}")
        except KeyError:
            messagebox.showinfo(title="Error", message="No details for the website exists.")
        except ValueError:
            messagebox.showinfo(title="Error", message="No Data File Found.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=1)

website_label = Label(text="Website:")
website_label.grid(column=0, row=2)

website_input = Entry(width=21)
website_input.grid(column=1, row=2)

search_button = Button(text="Search", width=14, command=search)
search_button.grid(column=2, row=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=3)

email_input = Entry(width=35)
email_input.grid(column=1, row=3, columnspan=2)
email_input.insert(0, EMAIL)

password_label = Label(text="Password:")
password_label.grid(column=0, row=4)

password_input = Entry(width=21)
password_input.grid(column=1, row=4)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=4)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()