import math
import os
import sys

from PIL import Image
from time import sleep
from progress_bar import progress_b
from threading import Thread

CURRENT_DIRECTORY: str = os.path.normpath(os.getcwd()).replace(os.sep, '/')  # Current working directory.
images_path: str = f"{CURRENT_DIRECTORY}/images/"  # Images to be processed
output_path: str = f"{CURRENT_DIRECTORY}/processed/"  # Images that have been processed
failures: list = []

def get_decision() -> str:
    user_input: str = input("Paste the path to the images directory or type 'q' to quit: ")
    return user_input

def get_files() -> list:
    """ Iterate through the directory and return a list of files. """
    global images_path
    image_files: list = []

    try:
        image_files = os.listdir(path=images_path)
    except FileNotFoundError:
        print(f"<{images_path}> not found.")
        decision: str = get_decision()
        if decision == "q":
            sys.exit()
        else:
            images_path = decision
            process_and_print()

    return image_files

def processor(chunk_files) -> None:
    """ Process images from a list of filenames. """
    count: int = 1
    n: int = len(chunk_files)

    progress_b(0, n)
    for filename in chunk_files:
        progress_b(count, n)
        process_image(filename)
        count += 1

def process_image(filename: str) -> None:
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
            f.save(output_path + ('_' + filename))
    except FileNotFoundError:
        # Add failed files to a list and print after.
        sleep(0.01)
        failures.append(filename)

def process_threads(files_list) -> None:
    """
    Slices the array of filenames and assigns each chunk to the
    processor function in individual thread.
    All threads are started and joined before returning.
    """
    threads: list = []
    num_threads: int = 6 # Testing with 6 threads
    chunk_size: int = math.ceil(len(files_list) / num_threads)

    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size
        chunk = files_list[start:end]
        if not chunk:
            break
        t = Thread(target=processor, args=(chunk,))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

def format_process_output(target_string: str, symbol: str = chr(0x305)) -> str:
    """ Formats the string for a 78 character terminal width. """
    target: int = (78 - len(target_string) // 2) - 1
    left: str = symbol * (target//4)
    right: str = symbol * (target//4)

    return left + target_string + right

def process_and_print():
    """ Gathers list of files and processes them, displaying a formatted output. """
    # These are for future message customization by users
    _begin: str = " Begin Processing "
    _complete: str = " Processing Completed "
    _symbol: str = '一'

    print(f"\n|{format_process_output(_begin, _symbol)}|")
    process_threads(get_files())
    print(f"\n|{format_process_output(_complete, _symbol)}|")

def summary() -> None:
    """ Print a formatted summary of the image processing function."""
    global failures

    num_failed: int = len(failures)
    tot_length: int = len(get_files())
    fail_percent: float = (num_failed / tot_length) * 100

    _success: str = f"Success rate: \033[4m{100.0 - fail_percent:5.1f}%\033[0m"
    _failed: str = f"Failure rate: \033[4m{fail_percent:5.1f}%\033[0m"
    _items: str = f"Items Processed: \033[4m{tot_length - num_failed}\033[0m"
    _summary: str = f"[SUMMARY {_success} | {_failed} | {_items}]"

    print(f"{_summary}\n")
    failures.clear()

def main():
    """ Main program entry point. """
    process_and_print()
    summary()

if __name__ == "__main__":
    main()
