from tkinter import Canvas, Tk, Button
from PIL import Image, ImageTk

# Capture the drawing from the canvas
def capture_drawing(canvas):
    # Save canvas content as a PostScript file
    canvas.postscript(file="drawing.eps", colormode="color")

    # Convert the PostScript file to an image format (PNG)
    img = Image.open("drawing.eps")
    img.save("drawing.png", "png")

    # Perform preprocessing (resize, normalize, etc.) if necessary

    # Return the preprocessed image
    return img


# Preprocess the image and send it to your CNN
def process_image(img):
    # Preprocess the image (e.g., resize, normalize)

    # Send the preprocessed image to your CNN for prediction
    # Your CNN prediction code goes here
    pass


# Function to process the drawing and send to CNN
def submit_image():
    img = capture_drawing(canvas)
    print("Check Images")
    # prediction = process_image(img)
    # print("CNN Prediction:", prediction)


# Function to clear the canvas
def clear_canvas():
    canvas.delete("all")


if __name__ == "__main__":
    # Create the main window and canvas
    root = Tk()
    root.title("Draw and Guess")
    canvas = Canvas(root, width=200, height=200, bg="white")
    canvas.pack()
    root.resizable(width=False, height=False)

    # Bind the left mouse button drag event to capture drawing
    canvas.bind("<B1-Motion>",
                lambda event: canvas.create_oval(event.x - 5, event.y - 5, event.x + 5, event.y + 5, fill="black"))

    # Create Submit and Clear buttons
    submit_button = Button(root, text="Submit", command=submit_image)
    submit_button.pack(side="left")
    clear_button = Button(root, text="Clear", command=clear_canvas)
    clear_button.pack(side="right")

    # Start the Tkinter event loop
    root.mainloop()
