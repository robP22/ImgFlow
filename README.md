# img_rsz

`img_rsz` is a lightweight Python tool that automates the resizing of `.png` images.  
Designed for quick batch processing and can easily fit into other image-processing workflows.

---

## Features

- Automatically resizes all `.png` files in a directory  
- Saves output images to a specified folder  
- Displays a simple progress bar during processing  
- Built with **Pillow** and minimal dependencies  

---

## Installation

```bash
git clone https://github.com/robP22/img_rsz.git
cd img_rsz
pip install -r requirements.txt
```

---

## Usage

Run the main script from the command line:

```bash
python img_rsz.py
```

By default, it processes all `.png` images in the current directory and saves the resized versions to an output folder.

You can modify the target output directory or image dimensions directly in the script.

---

## Example

```bash
python img_rsz.py
```

- **Input:** All `.png` files in the working directory  
- **Output:** Resized images written to `output/` (or configured path)

---

## Implementation Notes

- Uses Pillow’s `Image.resize()` with anti-aliasing for smooth results.  
- Displays progress with a simple, text-based progress bar.  
- Handles basic file errors gracefully and logs any failures.

---

## Future Improvements

Planned enhancements focus on scalability and performance:

- **Multithreading** image operations for faster batch processing  
- **Mutex control** to manage concurrent access to shared resources  

---

## License

This project is released under the **MIT License**. See the LICENSE file for details.
