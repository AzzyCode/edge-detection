import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

def load_image():
    """
    Load an image from the filesystem and update the GUI to show it.
    """
    global img, img_path
    
    file_path = filedialog.askopenfilename()

    if not file_path:
        return
    
    img_path = file_path
    img = cv2.imread(file_path)
    
    if img is None:
        print("Error loading image")
        return
    
    img_to_show = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    imgtk = ImageTk.PhotoImage(image=img_to_show)
    lbl_original_img.config(image=imgtk)
    lbl_original_img.image = imgtk
    

def process_image():
    """
    Process the image using the current GUI settings and display the result
    """
    if img is None:
        return
    
    # Get slider values
    low_threshold = slider_low_threshold.get()
    high_threshold = slider_high_threshold.get()
    blur_size = slider_blur.get()
    
    # Ensure the blur size is odd
    blur_size = blur_size if blur_size % 2 != 0 else blur_size + 1
    
    # Perform edge detection
    edged = edge_detection(img, low_threshold, high_threshold, blur_size)
    
    # Convert the processed image to a format that can be displayed in Tkinter
    img_to_show = Image.fromarray(edged)
    imgtk = ImageTk.PhotoImage(image=img_to_show)
    lbl_processed_img.config(image=imgtk)
    lbl_processed_img.image = imgtk
    
    
def edge_detection(image, low_threshold, high_threshold, blur_size):
    """
    Perform edge detection using Canny algorithm on the provided image.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (blur_size, blur_size), 0)
    edged = cv2.Canny(blurred, low_threshold, high_threshold)
    
    return edged


# Initialize the main window
root = tk.Tk()
root.title("Edge Detection")

# Frames for layout
frame_controls = tk.Frame(root)
frame_controls.pack(side=tk.TOP, fill=tk.X)

frame_images = tk.Frame(root)
frame_images.pack(fill=tk.BOTH, expand=True)

# Button to load images
btn_load_image = tk.Button(frame_controls, text="Load Image", command=load_image)
btn_load_image.pack(side=tk.LEFT, padx=10, pady=10)

# Sliders for parameters
slider_low_threshold = tk.Scale(frame_controls, from_=0, to=100, label="Low Threshold")
slider_low_threshold.set(50)
slider_low_threshold.pack(side=tk.LEFT, padx=10)

slider_high_threshold = tk.Scale(frame_controls, from_=50, to=200, label="High Threshold")
slider_high_threshold.set(150)
slider_high_threshold.pack(side=tk.LEFT, padx=10)

slider_blur = tk.Scale(frame_controls, from_=1, to=10, resolution=2, label="Blur Kernel size")
slider_blur.set(3)
slider_blur.pack(side=tk.LEFT, padx=10)

# Button to process the image
btn_process_image = tk.Button(frame_controls, text="Process Image", command=process_image)
btn_process_image.pack(side=tk.LEFT, padx=10, pady=10)

# Labels for displaying images
lbl_original_img = tk.Label(frame_images)
lbl_original_img.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10, pady=10)

lbl_processed_img = tk.Label(frame_images)
lbl_processed_img.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()