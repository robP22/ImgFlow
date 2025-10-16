# Img_Rsz

`img_rsz` is a lightweight Python tool that automates the resizing of `.png` images.  
Designed for quick batch processing and can easily fit into other image-processing workflows.

---

## Installation

```bash
git clone https://github.com/robP22/img_rsz.git
cd img_rsz
source venv/bin/activate
pip install -r requirements.txt
```

---

## Usage

Run the main script from the command line:

```bash
python img_rsz.py
'- or -'
python3 img_rsz.py
```

By default, it processes all `.png` images in the current directory and saves the resized versions to an output folder.

You can change the input/output directory or image dimensions directly in the script. [TEMPORARY]

---

## Example

```bash
(venv) PS C:\Users\username\Documents\Projects\py_projects\img_rsz> Python3 img_rsz.py
```

- **Input:** All `.png` files in the "working directory + /images"
- **Output:** Resized images written to `/processed` (or configured path)

---

## Features

- Automatically resizes all `.png` files in a directory.
- Saves output images to a specified folder.
- Displays a simple progress bar during processing.
- Built with **Pillow** and minimal dependencies.

---

## Implementation Notes

- Uses Pillow’s `Image.thumbnail()` with BICUBIC anti-aliasing by default.
- Displays the progress of the file processing task in terminal.

---

## Future Improvements

Planned enhancements focus on scalability and performance:

- **User Input:** 
- **temp**
---

## License

This project is released under the **MIT License**. See the LICENSE file for details.
