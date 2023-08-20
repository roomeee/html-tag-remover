import re
import tkinter as tk
from tkinter import scrolledtext


def remove_html_tags(input_string):
    clean_string = re.sub(r'<.*?>', '', input_string)
    return clean_string


def process_text():
    input_text = input_text_widget.get("1.0", "end-1c")
    cleaned_text = remove_html_tags(input_text)
    output_text_widget.delete("1.0", "end")
    output_text_widget.insert("1.0", cleaned_text)


# Create the main application window
app = tk.Tk()
app.title("HTML Tag Remover")

app.configure(bg='lightgray')

font_style = ("Helvetica", 12)

input_label = tk.Label(app, text="Enter HTML Text:", font=font_style)
input_label.pack()

input_text_widget = scrolledtext.ScrolledText(app, width=40, height=10, font=font_style)
input_text_widget.pack()

process_button = tk.Button(app, text="Process", command=process_text, font=font_style)
process_button.pack()

output_label = tk.Label(app, text="Cleaned Text:", font=font_style)
output_label.pack()

output_text_widget = scrolledtext.ScrolledText(app, width=40, height=10, font=font_style)
output_text_widget.pack()

app.mainloop()
