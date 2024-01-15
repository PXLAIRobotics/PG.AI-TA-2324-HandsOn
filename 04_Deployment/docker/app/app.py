# IMPORT STATEMENTS
from flask import Flask

app = Flask(__name__)

from keras.datasets import mnist
from keras.models import load_model

import numpy as np
import warnings

import onnx
import onnxruntime as rt

warnings.filterwarnings('ignore')


### CREATE SOME INPUT DATA
# Load in the MNIST data
(_, _), (test_images, test_labels) = mnist.load_data()

# reshape it so the pixels are flattened into 1 row of 784 pixels
test_images_reshaped = test_images.reshape((10000, 28*28))

# normalize the pixel values to all of them are between 0 and 1
test_images_transformed = test_images_reshaped.astype('float32') / 255

# Get all the 7s
index_sevens = np.where(test_labels == 7)
sevens = test_images_transformed[index_sevens]

# Take a random seven
seven = sevens[0]


### ACTUAL API ROUTES
@app.route("/")
def hello():
    return "Go to <url>/keras or <url>/onnx to see the inference results"


# API route to Keras model inference
@app.route("/keras")
def keras_inference():
    output_path = "./sequential"

    img = seven.reshape(1, 28*28)

    # Load the Keras model
    model = load_model(output_path)

    # Do inference
    pred = np.argmax(model.predict(img), axis=1)

    return str(pred)


# API route to ONNX model inference
@app.route("/onnx")
def onnx_inference():
    output_path = "./sequential.onnx"

    # Load the ONNX model
    model = onnx.load(output_path)
    output = model.graph.output
    output_names = [n.name for n in output]

    providers = ['CPUExecutionProvider']
    m = rt.InferenceSession(output_path, providers=providers)

    # Do inference
    onnx_pred = np.argmax(m.run(output_names, {"input": [seven]}), axis=2)
    onnx_preds = onnx_pred[0]

    return str(onnx_preds)


# Start up the backend
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7777)
