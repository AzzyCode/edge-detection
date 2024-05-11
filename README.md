# Edge Detection GUI

This application provides a simple graphical user interface (GUI) for performing edge detection on images using the Canny algorithm. It is built with Python, using Tkinter for the GUI and OpenCV for image processing.

## Features

- Load images from the filesystem.
- Interactive sliders to adjust edge detection parameters:
  - Low Threshold
  - High Threshold
  - Blur Kernel Size
- Display the original and processed images side by side.
- Simple and intuitive user interface.

## Dependencies

To run this application, you will need Python and several packages. Here are the steps to set up your environment:

1. **Python**: Make sure Python 3.6 or later is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **OpenCV**: Used for image processing functions.
```bash
pip install opencv-python
```

3. **Pillow** (PIL Fork): Used for image handling in the Tkinter GUI.
```bash
pip install Pillow
```

4. **Tkinter**: Typically comes pre-installed with Python. If not, you can install it using your package manager. For example, on Ubuntu:
```bash
sudo apt-get install python3-tk
```

## How to Use
1. **Load an Image**: Click on the 'Load Image' button and select an image from your filesystem.
2. **Adjust Parameters**: Use the sliders to adjust the low threshold, high threshold and blur size.
3. **Process Image:** Click on the 'Process Image' button to apply edge detection.
4. **View Results:** The processed image will appear next to the original image.

## Licence
This project is open-source and available under the MIT License. See the LICENSE file for more details.