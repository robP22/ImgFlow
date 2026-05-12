import math
import os
import sys

from formatter import format_process_output, summary
from PIL import Image
from progress_bar import progress_b
from threading import Thread
from time import sleep

CURRENT_DIRECTORY: str = os.path.normpath(os.getcwd()).replace(os.sep, '/')  # Current working directory.
images_path: str = f"{CURRENT_DIRECTORY}/images/"  # Images to be processed
output_path: str = f"{CURRENT_DIRECTORY}/processed/"  # Images that have been processed
failures: list = []

def get_decision() -> str:
    """ Allow the user to exit the program or correct a directory path error. """
    print("Example path structure: './images/' or 'C://Users/user/Documents/ImgFlow/images/'\n")
    user_input: str = input("Enter the images path or type 'q' to quit: ")
    if user_input == 'q':
        sys.exit(0)
    return user_input if os.path.isdir(user_input) else get_decision()

def get_files(path: str) -> list[str]:
    """ Iterate through the directory and return a list of files. """
    global images_path
    try:
        image_files = os.listdir(path)
        return image_files
    except FileNotFoundError:
        print(f"\n[Directory './{os.path.basename(os.path.normpath(path))}' not found.]")
        images_path = get_decision()
        corrected_files: list = get_files(images_path)
        print(images_path)
        return corrected_files

def processor(chunk) -> None:
    """ Passes each individual filename into the image processor function. """
    count: int = 1
    n: int = len(chunk)

    progress_b(0, n)
    for filename in chunk:
        progress_b(count, n)
        process_image(filename)
        count += 1

def process_image(filename: str):
    """ Pillow image resizing to 64 x 128 px. """
    global failures
    global images_path
    global output_path

    max_width: int = 64 #px
    max_height: int = 128 #px

    try:
        with Image.open(images_path + filename) as f:
            f.load() # Load the image for processing
            f.thumbnail((max_width, max_height))  # Resize the image
            f.save(output_path + '_' + filename)

    except FileNotFoundError:
        # Add failed files to a list and print after.
        sleep(0.01)
        failures.append(filename)

def process_threads(files: list) -> None:
    """
    Slices the array of filenames and assigns each chunk to the
    processor function in individual thread.
    All threads are started and joined before returning.
    """
    threads: list = []
    num_threads: int = 6 # Testing with 6 threads
    chunk_size: int = math.ceil(len(files) / num_threads)

    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size
        chunk = files[start:end]
        if not chunk:
            break
        t = Thread(target=processor, args=(chunk,))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

def process_and_print(files: list)-> None:
    """ Gathers list of files and processes them, displaying a formatted output. """
    # These are for future message customization by users
    _begin: str = " Begin Processing "
    _complete: str = " Processing Completed "
    _symbol: str = '一'
    print(f"\n|{format_process_output(_begin, _symbol)}|")
    process_threads(files)
    print(f"\n|{format_process_output(_complete, _symbol)}|")

def main():
    """ Main program entry point. """
    global failures
    global images_path
    global output_path

    files: list = get_files(images_path)
    process_and_print(files)
    summary(len(failures), len(files))

if __name__ == "__main__":
    main()
