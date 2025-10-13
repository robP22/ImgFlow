import os
import sys

from PIL import Image
from time import sleep
from progress_bar import progress_b
from threading import Thread

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

def processor(chunk_files) -> None:
    """ Process images from a list of filenames. """
    count: int = 1
    n: int = len(chunk_files)

    progress_b(0, n)
    for filename in chunk_files:
        progress_b(count, n)
        process_image(filename)
        count += 1

def prcss_thrds(files_list) -> None:
    threads: list = []
    num_threads: int = 6 # Testing with 6 threads

    chunk_size: int = int(len(files_list)/num_threads)
    curr_chunk: int = 0

    chunk_arr: list = []

    for _ in range(num_threads):
        chunk: list = []
        for i in range(curr_chunk, curr_chunk + chunk_size):
            chunk.append(files_list[i])
        curr_chunk += chunk_size
        t = Thread(target=processor, args=(chunk,))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

def format_process_output(target_string: str, symbol: str =chr(0x305)) -> str:
    """ Formats the string for a 78 character terminal width. """
    target: int = (78 - len(target_string) // 2) - 1
    left: str = symbol * (target//2)
    right: str = symbol * (target//2)

    return left + target_string + right

def summary(num_failed: int, tot_length: int) -> None:
    fail_percent: float = (num_failed / tot_length) * 100

    _success: str = f"Success rate: {100.0 - fail_percent:5.1f}%"
    _failed: str = f"Failure rate: {fail_percent:5.1f}%"
    _items: str = f"Items Processed: {tot_length - num_failed}"

    _summary: str = f"[SUMMARY] {_success} | {_failed} | {_items}"
    _5: str = "     "
    print(f"{_5}{_summary}\n")

def main():
    global failures
    global input_path
    global output_path

    output_path = os.path.join(input_path, 'processed/') # Images that have been processed
    input_path = os.path.join(input_path, 'images/') # Images to be processed

    files_list = get_files()
    n: int = len(files_list)
    if n == 0:
        sys.exit(1)

    _begin: str = " Begin Processing "
    _complete: str = " Processing Complete "
    symbol: str = '_'

    print(f"\n{format_process_output(_begin)}")
    prcss_thrds(files_list)
    print(f"\n{format_process_output(_complete, symbol)}")

    num_failed: int = len(failures)
    tot_length: int = len(files_list)

    summary(num_failed, tot_length)
    failures.clear()

if __name__ == "__main__":
    main()
