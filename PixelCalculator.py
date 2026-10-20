import tkinter as tk
from tkinter import ttk, Tk, filedialog, messagebox
import fitz
from PIL import Image
from pathlib import Path
import shutil
import os


        # This is the main program function
def main():
    main_app_win()


        # This func works together with chk_format() func; they check if file is valid format and return file extension (even if file does not have ext.) and file path
def open_file():
    global file_path
    global file_format
    file_path = filedialog.askopenfilename(title="Select Image or PDF File")
    file_format = chk_format(file_path)
    if file_path:
        if file_format == None:
            messagebox.showwarning("Error", f"Invalid file format")
        else:
            messagebox.showinfo("File selected", f"File {file_path} has been selected. Please press Calculate")


        # Read open_file() func description
def chk_format(file):
    format_list = ["jpeg", "png", "gif", "bmp", "tiff", "ico", "webp", "ppm", "pgm", "pbm", "pcx", "tga", "avif"]
    try:
        slikica = Image.open(file)
        slikica_format = slikica.format
        if slikica_format.lower() in format_list:
            return slikica_format.lower()
    except:
        try:
            with open(file,'rb') as f:  # Every file has a, so called, magic number. It's a sequence of bytes that identifies the format of a file
                magic = f.read(5)
                if magic == b'%PDF-':
                    return 'pdf'
        except:
            return None


        # This func is used only if the file is pdf; it creates temp dir on the local drive as ...\pix_calc_app\temp
def create_temp_dir():
    drive = Path.cwd().anchor
    folder = Path(drive) / "workspaces" / "38842169" / "project" / "pix_calc_app" / "temp"
    Path(folder).mkdir(parents=True, exist_ok=True)
    return str(folder)

        # This func removes the ...\pix_calc_app\ dir created by the create_temp_dir() func once the files have gone through the count_pixels() func
def remove_temp_dir():
    drive = Path.cwd().anchor
    folder = Path(drive) / "workspaces" / "38842169" / "project" / "pix_calc_app"
    shutil.rmtree(folder)


        # This function calls create_temp_dir() func, then converts *.pdf pages to *.png pages and stores them in ...\pix_calc_app\temp until count_pixels() is called
def pdf_to_img(file_path):
    file = create_temp_dir()
    doc = fitz.open(file_path)
    image_paths = []
    for i, page in enumerate(doc):
        pix = page.get_pixmap(alpha=True)
        image_path = os.path.join(file, f"page_{i + 1}.png")
        pix.pil_save(image_path)
        image_paths.append(image_path)
    return image_paths


        # This func converts *.png files to RGBA, and goes through every pixel on page to check RGBA. RGBA because some img formats require A(lpha) / explore cmyk option for printers in next app ver.
def count_pixels(file_path, red_threshold, green_threshold, blue_threshold):
    img = Image.open(file_path)
    img = img.convert("RGBA")
    width, height = img.size
    total_pixels = width * height
    inked_pixels = 0
    for x in range(width):
        for y in range(height):
            r, g, b, a = img.getpixel((x, y))
            if r > red_threshold or g > green_threshold or b > blue_threshold:
                inked_pixels += 1
    ink_percentage = (inked_pixels / total_pixels) * 100
    return round(ink_percentage, 2)


        # This func is the callback/event_handler/command_handler. This func also retrieves RGB values from the sliders when the GUI's Calculate button is pressed
def calc_button(slider, slider1, slider2):
    try:
        red_threshold = slider.get()
        green_threshold = slider1.get()
        blue_threshold = slider2.get()

        if file_format == 'pdf':
            converted_img = pdf_to_img(file_path)
            result_list = []
            for i, j in enumerate(converted_img):
                result_list.append(
                    f"for >>page_{i + 1}<< percentage of inked pixels is {count_pixels(j, red_threshold, green_threshold, blue_threshold)}%")
            messagebox.showinfo("Result", f"As per RGB sliders {'; '.join(result_list)}")
            remove_temp_dir()
        else:
            messagebox.showinfo("Result", f"As per RGB sliders, percentage of inked pixels in >>{file_path}<< is {count_pixels(file_path, red_threshold, green_threshold, blue_threshold)}%")
    except:
        messagebox.showwarning("File missing", "Select a file first")


        # This is the GUI/main window function, including open, calculate and close buttons, as well as RGB sliders
def main_app_win():
    global file_path
    global file_format

    # Main app window
    app = Tk()
    app.geometry("600x250")
    app.title("PIXcalc")
    app.resizable(False, False)

    # Frame settings
    left_frame = tk.Frame(app)
    left_frame.pack(side="left", padx=20, pady=20)
    right_frame = tk.Frame(app)
    right_frame.pack(side="right", padx=5, pady=5)

    # Label settings
    app_label = ttk.Label(left_frame, text="PixelCalculatorV1.0", font=("Arial", 11, "bold"))
    app_label.pack(padx=20, pady=10)
    app_label = ttk.Label(right_frame, text="Set RGB")
    app_label.pack(padx=0, ipady=0)

    # Button settings
    app_button1 = ttk.Button(left_frame, text="Open", command=open_file)
    app_button1.pack(fill="x", pady=5)
    app_button2 = ttk.Button(left_frame, text="Calculate", command=lambda: calc_button(slider, slider1, slider2))
    app_button2.pack(fill="x", pady=5)
    app_button3 = ttk.Button(left_frame, text="Close", command=app.destroy)
    app_button3.pack(fill="x", pady=5)

    # Slider settings
    slider = tk.Scale(right_frame, from_=0, to=255, orient="horizontal", sliderlength=20, length=350, label="Red")
    slider1 = tk.Scale(right_frame, from_=0, to=255, orient="horizontal", sliderlength=20, length=350, label="Green")
    slider2 = tk.Scale(right_frame, from_=0, to=255, orient="horizontal", sliderlength=20, length=350, label="Blue")
    slider.pack(fill="x", pady=0)
    slider1.pack(fill="x", pady=0)
    slider2.pack(fill="x", pady=0)

    app.mainloop()


if __name__ == '__main__':
    main()
