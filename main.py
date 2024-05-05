from tkinter import Canvas, Tk, Button, Label
from PIL import Image, ImageTk, ImageOps
from keras import models
import numpy as np
global model

# Capture the drawing from the canvas
def capture_drawing(canvas):

    # Save canvas content as a PostScript file
    canvas.postscript(file="drawing.eps", colormode="mono")

    # Convert the PostScript file to an image format (PNG)
    img = Image.open("drawing.eps")
    img = ImageOps.invert(img)
    img.save("drawing.png", "png")

    # Return the image
    return img

# loading and returning model from model.json and weights from model.weights.h5
def load_model():

    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = models.model_from_json(loaded_model_json)

    # load weights into new model
    loaded_model.load_weights("model.weights.h5")
    print("Loaded model from disk")
    loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    #print(loaded_model.summary())
    return loaded_model

# Preprocess the image and uploading to model, returning the prediction
def process_image(img):

    # Grayscaling image and resizing
    img = img.convert('L')  
    img = img.resize((28, 28))

    # Creating numpy array of image and normalizing
    img_array = np.array(img) / 255.0
    img_array = img_array.reshape(1, -1) 

    # Predicting based on image array 
    prediction = model.predict(img_array)
    return prediction

# Function to process the drawing, sending it to the CNN and updating label
def submit_image():

    img = capture_drawing(canvas)
    print("Image Saved")

    prediction = process_image(img)
    #print("CNN Prediction:", np.argmax(prediction, axis=1))
    prediction_label.config(text=f"CNN Prediction: {np.argmax(prediction, axis=1)}")


# Function to clear the canvas and label
def clear_canvas():
    canvas.delete("all")
    prediction_label.config(text="")


if __name__ == "__main__":
    # Create the main window and canvas
    root = Tk()
    root.title("Draw and Guess")
    canvas = Canvas(root, width=500, height=500, bg="white")
    canvas.pack()
    root.resizable(width=False, height=False)

    # Bind the left mouse button drag event to capture drawing
    canvas.bind("<B1-Motion>",
                lambda event: canvas.create_rectangle(event.x - 3, event.y - 3, event.x + 3, event.y + 3, fill="black"))
    
    # Loads Keras model into global variable
    model = load_model()

    # Create Submit and Clear buttons
    submit_button = Button(root, text="Submit", command=submit_image)
    submit_button.pack(side="left")
    clear_button = Button(root, text="Clear", command=clear_canvas)
    clear_button.pack(side="right")

    # Create a label widget to display the prediction
    prediction_label = Label(root, text="")
    prediction_label.pack()

    # Start the Tkinter event loop
    root.mainloop()
