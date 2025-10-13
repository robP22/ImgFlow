import os
import sys

from PIL import Image
from time import sleep
from progress_bar import progress_b

failures: list = []
output_path: str = ''
input_path: str = os.getcwd() # Current working directory.

def get_files() -> list:
    """ Iterate through the directory and return a list of files. """
    global input_path
    image_files: list = os.listdir(path=input_path)
    return image_files

def process_image(filename) -> None:
    """ Pillow image resizing to 64 x 128 px. """
    global failures
    global output_path

    max_width: int = 64 #px
    max_height: int = 128 #px

    try:
        with Image.open(os.path.join(input_path, filename)) as f:
            f.load() # Load the image for processing
            f.thumbnail((max_width, max_height))  # Resize the image
            f.save(output_path + '_' + filename)
    except FileNotFoundError:
        # Add failed files to a list and print after.
        sleep(0.01)
        failures.append(filename)

def processor(files_list) -> None:
    """ Process images from a list of filenames. """
    count: int = 1
    n: int = len(files_list)

    print("\t\t<---------- Processing images ---------->")
    progress_b(0, n)
    for filename in files_list:
        progress_b(count, n)
        process_image(filename)
        count += 1
    print("\n\t\t<--------- Processing complete --------->")

def main():
    global failures
    global input_path
    global output_path

    output_path = os.path.join(input_path, 'processed/') # Images that have been processed
    input_path = os.path.join(input_path, 'images/') # Images to be processed

    files_list = get_files()
    if len(files_list) == 0:
        sys.exit(1)
    processor(files_list)

    num_failed: int = len(failures)
    fail_percent: float = (num_failed / len(files_list)) * 100
    print(f"\t\tSuccess rate: {100.00 - fail_percent:.2f} | Failure rate: {fail_percent:.2f}%")
    failures.clear()

if __name__ == "__main__":
    main()
