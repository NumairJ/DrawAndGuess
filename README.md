# DrawAndGuess
Personal Project to implement a CNN that is trained on MNIST dataset and to then predict the numbers based on user generated images

# Imports Needed
Tensorflow
Pillow
Ghostscript (Add to path aswell)
Matplotlib
seaborn
scikit-learn

# Get Started
It is reccommended to set up a python virtual environment with python 3.9+ with the mentioned imports above
Please make sure that python programs is able to create files and read files and not restricted from antiviruses

# Once setup
1. Run character-recognization.ipynb in an IDE
2. Run Main.py
3. Draw and see if the CNN predicts correctly

# Review
After playing around with the program and drawing my own images for the CNN to predict, I realize that it would frequently predict the wrong number.
This is a stark contrast to the 97.8% test accuracy from the MNIST dataset.
I believe this can be the caused by multiple factors which are but limited to:
-Errorness preprocessing that includes resizing, converting from .eps to .png to numpy.array
-CNN is trained on flattened 28x28 drawn images but not on resized flattened 28x28 images
-CNN wasn't trained on corrupted MNIST dataset that exists out there

# TO DO
Possibly increase accuracy with user generated images by adding more images to dataset or by adjusting the model to handle complex digits
