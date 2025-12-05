

def open_file(): # This func works together with chk_format() func; they check if file is valid and return file ext. (even if file does not have ext.) and file path.
The reason for it is to avoid relying on ext during file selection/opening; in case the file has no ext, the program will not raise an error but complete the job

def create_temp_dir(): # This func is used only if the file is pdf; it creates temp dir on the local drive as ...\pix_calc_app\temp.
The reason for this is pdf documents can have multiple pages and, once converted, those paged need to be accessed by the cout_pixels func
There is also a function that removes ...\pix_calc_app\temp in order to save space/memory.
Func to remove the ...\pix_calc_app\temp directory is only ran from the main() func, and can be disabled there

def pdf_to_img(file_path): # This function calls create_temp_dir() func which I mentioned above, then converts *.pdf pages to *.png pages and stores them in ...\pix_calc_app\temp until count_pixels() is called.

def main(): # None of the funcs apart from main() use print(), all other functions return value, so in main() we can shape how the values are shown