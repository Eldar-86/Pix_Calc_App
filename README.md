Pixel Calculator App
Video Demo: https://youtu.be/CI9hqN5-yUI
Description:
This app was developed as a request from my brother, who works as a print shop manager for a major company. He needed an app that could calculate the number of colored pixels on an image or PDF page, based on RGB settings (0-255). The current version is more of a proof of concept than a fully functional app that completes all the intended features. I plan to improve it in the future by -- among other changes -- simplifying the code and including support for the CMYK color model, which is more commonly used in printing.

When the program is run, tkinter is used to initiate the main app window (GUI) -- event handler -- which consists of three buttons on the left and three sliders on the right of the window. The three buttons are:

Open: to open a file
Calculate: to calculate coloured pixels in the file
Close: to close the app 'Close'
Three sliders are for red, green and blue colour thresholds. Filedialog in open_file function is used to open a file, after which, file format is checked for validity via chk_format function. If the file is not supported, program notifies the user that the chosen file is invalid. If the file is valid, the program confirms the validity by showing the path of the file selected, and instructing the user on how to proceed. At that point, If user selects 'Calculate', program runs count_pixels function, which goes through every pixel on each page and returns the percentage of coloured pixels in a message box, based on the RGB sliders' values. count_pixels function fetches the RGB values from the sliders before each click on the 'Calculate' button. If the 'Calculate' button is pressed before a file is selected, the program prompts the user to first select a file. The three sliders are:

R: slider for colour red
G: slider for colour green
B: slider for colour blue
The project is structured as follows:

Project Structure:
project/
├── project.py
├── test_project.py
├── Text_Document.txt
├── before1.jpg
├── pdf_doc.pdf
├── requirements.txt
└── README.md

File Descriptions:
project.py contains the main functionality (logic), including the app GUI. The reason I did not separate the logic from UI is, when I started building the app, GUI wasn't in any plans. At the beginning, the app was supposed to be initiated via command-line arguments, where sys.argv[1] would be a path to a PDF document or an image file. However, I eventually came to conclusion that RGB values would need to be dynamic, and including them as CL arguments might complicate UI. I then decided to use tkinter -- which is a part of the standard Python library -- and to create GUI for the app as well. I understand that separating the app UI from the logic would make the code more modular and, hence, futureproof in terms of maintainability and scalability, which I will explore in the next build.

test_project.py is a repository including a test suite for validating some functions used in the application.

Text_Document.txt is a file which is used by test_project.py repository to test error handling. The app is desgined to accept either PDF or image files, therefore any other file type should raise an error with messagebox popping up, informing the user that invalid file format was selected. Error handling does not solely rely on the files' extensions, since files can have wrong or no extension. Files can also be corrupt.

before1.jpg is also used for the testing purposes in test_project.py. Pillow library is used to access and try to open the selected file. If the file is a valid image file, PIL will be able to open and confirm its integrity, before the file is processed by count_pixels function.

pdf_doc.pdf is also a file which is used in test_project.py repository. As mentioned earlier, file extensions can be unreliable. That is why for PDF, chk_format function checks the files' magic number to confirm the files' integrity.

requirements.txt lists the required libraries for the application to run. The application requiures only two non-standard Python libraries:
Pillow (PIL) for image processing.
PyMuPDF (specifically fitz from PyMuPDF) for PDF handling.

Dependencies can be installed by running:

pip install -r requirements.txt
