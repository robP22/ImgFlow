# ImgFlow

`ImgFlow` is a lightweight Python tool that automates the batch resizing of `.png` images.  
It is designed for quick local processing and can be integrated into other image-processing workflows.

---

## Installation

```bash
git clone https://github.com/robP22/ImgFlow.git
cd ImgFlow
source venv/bin/activate
pip install -r requirements.txt
````

---

## Usage

Run the main script from the command line:

```bash
python ImgFlow.py
# or
python3 ImgFlow.py
```

By default, it processes all `.png` images in the `/images` directory and saves the resized versions to `/processed`.

The tool supports user-defined input directories. If an invalid or missing directory is provided, it falls back to the default `/images` directory.

---

## Example

```bash
(venv) PS C:\Users\username\Documents\Projects\py_projects\ImgFlow> python ImgFlow.py
```

* **Input:** All `.png` files in `/images`
* **Output:** Resized images written to `/processed` (or configured path)

---

## Features

* Batch processes all `.png` files in a directory
* Saves output images to a specified folder
* Displays a simple progress indicator during processing
* Built with **Pillow** and minimal dependencies

---

## Implementation Notes

* Uses Pillow’s `Image.thumbnail()` with BICUBIC anti-aliasing
* Processes images in batch mode for efficiency
* Includes terminal-based progress tracking

---

## Future Improvements

Planned enhancements focus on scalability and robustness:

* **User Input:** Improve CLI handling for custom input/output paths with validation
* **Security:** Add input validation and path sanitization to prevent invalid or unsafe directory access

---

## License

This project is released under the **MIT License**. See the LICENSE file for details.

