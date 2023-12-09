import os
from tkinter import *
from PIL import Image, ImageTk, ImageFilter

def launch():
    os.system("python app.py")
    root.destroy()

root = Tk()

root.title('App Launcher')

# Set window size and position
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

background_image = Image.open("junky (1).jpeg")
background_image = background_image.resize((window_width, window_height), Image.LANCZOS)
background_image = background_image.filter(ImageFilter.GaussianBlur(radius=5))
background_render = ImageTk.PhotoImage(background_image)
background_label = Label(root, image=background_render, highlightthickness=0)
background_label.place(relwidth=1, relheight=1)


launcher_button = Button(root, text='Launch',
                         height=2, width=15,
                         command=launch,
                         bg='#2ecc71', fg='white', bd=4,
                         font=('Arial', 12, 'bold'))

# Pack the Launch button into the window with some padding
launcher_button.pack(pady=20)

# Create a label for additional information with updated styling
info_label = Label(root, text="Hi,I'm Junky-β",
                   font=('Arial', 14, 'italic', 'bold'), highlightthickness=0, fg='#e74c3c', padx=10, pady=5, bd=2, relief='ridge')

# Pack the info label with some padding
info_label.pack(pady=10)

# Create a footer label with updated styling
footer_label = Label(root, text='© 2023 asr pvt ltd',
                     font=('Arial', 10, 'italic'), highlightthickness=0, fg='#95a5a6', padx=10, pady=5, bd=2, relief='ridge')

# Pack the footer label with some padding
footer_label.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()






