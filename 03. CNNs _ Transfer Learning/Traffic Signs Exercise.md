# Belgian Traffic Signs Classifier

## Part 1
### Objective:

Design and implement a CNN for classifying Belgian traffic signs into their respective categories.

### Assignment Description:

You will develop a deep learning model to classify Belgian traffic signs into their designated classes using a dataset of your choice, either a customized 34-class dataset or the original 62-class dataset. The goal is to create a robust classifier capable of accurately identifying traffic signs.

### Assignment Tasks:

#### 1. Dataset Selection:

* Option 1: https://data.mendeley.com/datasets/kfngc5jxds/2
  This is a customized version of the Belgian Traffic Signs dataset with 34 classes.
* Option 2: The original Belgian Traffic Signs dataset with 62 classes: https://btsd.ethz.ch/shareddata/
  	You only need the two files listed after the text "BelgiumTS for Classification (cropped images)":
	 * BelgiumTSC_Training (171.3MBytes)
	 * BelgiumTSC_Testing (76.5MBytes)
* The labels: [labels](labels.py)

#### 2. Data Preprocessing:

Load and preprocess the dataset, including resizing, normalization, and data augmentation if necessary.

#### 3. Model Architecture:

Design and build a CNN model for traffic sign classification. Specify the model architecture, including the number of layers, filter sizes, activation functions, and output layer.

#### 4. Training:

Train the model on the training dataset.
Plot a graph showing the model's accuracy and loss for each epoch during training.

#### 5. Evaluation:

Assess the model's performance on the test dataset.
Calculate and report the accuracy achieved on the test set.

#### 6. Confusion Matrix:

Create a confusion matrix to visualize the model's performance in classifying different traffic signs.

#### 7. Misclassification Analysis:

Display some images from the test set that were misclassified by the model, along with their predicted and true labels.

#### 8. Custom Image Testing:

Test the trained classifier with a random image (i.e. from google images) of a Belgian traffic sign and display the model's predictions.


## Part 2
### Objective:

Retrain a YOLO model for classifying traffic signs. 

### Assignment Description:

YOLO comes in several flavours. You can use a basic classifier, or a detector/classifier. 

**__Note__**:  If you use the detector, you'll need an annotated dataset with bounding boxes. You can search on the internet for a dataset that has this kind of format, or you can create it yourself using RoboFlow (https://roboflow.com).