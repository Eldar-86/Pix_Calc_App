from project import chk_format, create_temp_dir, remove_temp_dir, pdf_to_img, count_pixels
import pytest


def test_chk_format():                                                                  # Function to test the chk_format function in project.py
    assert chk_format("/workspaces/38842169/project/before1.jpg") == "jpeg"             # This line will test returning value of a JPEG file; valid file
    assert chk_format("/workspaces/38842169/project/pdf_doc") == "pdf"                  # This line will test returning value of a PDF file; valid file
    assert chk_format("/workspaces/38842169/project/Text_Document.txt") is None         # This line will test returning value of a TXT file; invalid file


def test_pdf_to_img():                                                                  # Function to test the pdf_to_img function in project.py
    pdf_to_img_result = ['/workspaces/38842169/project/pix_calc_app/temp/page_1.png',
                        '/workspaces/38842169/project/pix_calc_app/temp/page_2.png']
    assert pdf_to_img("/workspaces/38842169/project/pdf_doc") == pdf_to_img_result      # This line will test returning value when 2 page long PDF file is selected


def test_count_pixels():                                                                # Function to test count_pixels() functions which uses PIL, goes through an image and returns float rounded to 2 decimals
    assert count_pixels("/workspaces/38842169/project/before1.jpg", 0, 0, 0) == 97.33   # This line will test returning value of a before1.jpg file; if all (RGB) values set to 0 should return 97.33


def test_create_temp_dir():                                                             # Function to test the create_temp_dir function in project.py
    assert create_temp_dir() == "/workspaces/38842169/project/pix_calc_app/temp"        # This line will test returning value of creating a temp directory for PDF files


def test_remove_temp_dir():                                                             # Function to test the remove_temp_dir function in project.py
    assert remove_temp_dir() is None                                                    # This line will test returning value of removing an existing temp directory
    with pytest.raises(FileNotFoundError):                                              # This line will test returning value of attempting to remove a non-existing temp directory
        remove_temp_dir()
