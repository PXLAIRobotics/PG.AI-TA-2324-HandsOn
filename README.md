# Postgraduate: AI Technical Architect 2023-2024

## Goals

### Les 1
- Begrijpen van het doel en de toepassingen van **NVIDIA CUDA**, inclusief de redenen voor zijn populariteit in computertechnologie.
- Inzicht in **Google Colab**, inclusief de belangrijkste voordelen en beperkingen.
- Analyseren van problemen gerelateerd aan imbalanced datasets in machine learning en mogelijke oplossingen.
- Kennis van verschillende soorten **activatiefuncties** in de outputlaag van neurale netwerken en hun toepassingen.
- Begrip van het doel en het belang van een **confusion matrix** in de evaluatie van classificatiemodellen.
- Het belang van het plotten van **nauwkeurigheid (accuracy)** en **verlies (loss)** tijdens het trainingsproces van een model.
- Begrijpen waarom en hoe **normalisatie** en **standaardisatie** worden toegepast in datavoorbereiding.
- De voordelen van het **finetunen** van een bestaand model in plaats van een model vanaf nul opbouwen.

### Les 2
- Definiëren van de rol en het belang van een **AI-backend** in een systeemarchitectuur.
- De voor- en nadelen van het gebruik van **pip** in Python voor package management en mogelijke verbeteringen.
- Het begrijpen van de voordelen van het gebruik van **containers** in softwareontwikkeling en deployment.
- Overwegen van redenen voor het ontwikkelen van AI-systemen in de **cloud**.
- Uitleggen van de essentiële kenmerken van een **AI-model** en de verschillende benaderingen in modelontwerp.
- Verschillende methoden voor het in productie brengen van AI-modellen en de overwegingen die daarbij komen kijken.
- Kan uitleggen welke **meta-informatie** belangrijk is om bij te houden voor een serialized object (model).
- Kan uitleggen hoe dit model aangesproken kan worden (bijvoorbeeld via een **web API**).
- Kan uitleggen welke **metrieken** bij het aanspreken van een getraind model belangrijk zijn (response time, retrain time, confidence of prediction, etc.).
- Kan uitleggen welke uitdagingen bestaan op het vlak van hard- en software in productie.
- Kan uitleggen welke oplossingen bestaan voor de uitdagingen op hard- en software vlak (API, messaging, **ONNX**).
- Kennis van **Retrieval-Augmented Generation (RAG)** en de toepassingen ervan in AI-modellen.
- Inzicht in het gebruik en de relevantie van **vector databases** in Large Language Models (LLMs) en waarom ze van belang zijn.


## Contents

1. **Frameworks & libraries**
   - Data Exploration & Model Training
     - *Classical Machine Learning*
     - *Deep Learning*
   - Visualizations
   - Prototyping & Robotics
2. **The tools we are going to use for the hands-on**
3. **Hands-on**
   - 01: First steps
     - First Neural Network with Keras
     - Credit Card Fraud
   - 02: Optimizations via MNIST
   - 03: CNNs & Transfer Learning
     - Object detection, identification and transfer learning with YOLO
     - CNN classifier
   - 04: Deployment & MNIST Solution
   - 05: NLP & LLMs
   - 06: Unstructured Data & Classical ML (not included in class, but added as reference)


## Example exam questions

### Wat is belangrijk bij het trainen van een neuraal netwerk?
- **a)** Het selecteren van een geschikte activatiefunctie voor de lagen.
- **b)** Het kiezen van een passend aantal neuronen en lagen.
- **c)** Het bepalen van een geschikte leersnelheid en optimalisatiemethode.
- **d)** Het verzekeren van een gebalanceerde en representatieve dataset.
- **e)** Alle bovenstaande opties.


### Wat beschrijft het beste het doel van een AI-backend?
- **a)** Het bieden van een gebruikersinterface voor AI-toepassingen.
- **b)** Het opslaan van grote hoeveelheden data.
- **c)** Het uitvoeren van de kernberekeningen en verwerking voor AI-toepassingen.
- **d)** Het verzorgen van netwerkverbindingen voor AI-systemen.

## [The questions with the answers](questionswithanswers.md)

## Development environments
* TensorFlow: https://github.com/PXLAIRobotics/PXL_ML_Docker_v2.0_TensorFlow
* PyTorch: https://github.com/PXLAIRobotics/PXL_ML_Docker_v2.0_PyTorch


## Exercises
**01. First steps**
* [01. First Neural Network with Keras](01.%20First%20Steps/01.%20First%20Neural%20Network%20with%20Keras.ipynb)  
* [02. Credit_card_fraud](01.%20First%20Steps/02.%20Credit_card_fraud.ipynb)

**02. Optimizations via MNIST**
* [01. simple_mnist_classifier_exercise](02.%20Optimization/01.%20simple_mnist_classifier_exercise.ipynb)

**03. CNNs & Transfer Learning**
* [Traffic Signs Exercise](03.%20CNNs%20_%20Transfer%20Learning/Traffic%20Signs%20Exercise.md)

**05. NLP**
* [IMDb Sentiment Classification](05_NLP/03.%20basic_imdb_classifier_exercise.ipynb)

## Demo notebooks
**03. CNNs & Transfer Learning**
* [01. YOLO](03.%20CNNs%20_%20Transfer%20Learning/01.%20YOLO.ipynb)
* [02. CNN Classifier](03.%20CNNs%20_%20Transfer%20Learning/02.%20demo_cnn_classifier.ipynb)
* [05. LLM Intro](05_NLP/01.%20Practical_example_with_LLMs.ipynb)
* [05. LangChain](05_NLP/02.%20LangChain_Example.ipynb)
* [06. Titanic - Structured Data](06_Structured_Data_Classical_ML/01.%20titanic_data_preprocessing.ipynb)
* [06. Titanic - Structured Data](06_Structured_Data_Classical_ML/02.%20titanic_model_training.ipynb)

## FAQ

### Google Drive
You can mount your Google Drive in Google Colab in the following way:

```
from google.colab import drive
drive.mount('/content/drive')
```

And then access your folders like this:

```
folder = "/content/drive/MyDrive/.../"
```

### Loss functions
#### Classification
**Binary classification**
* Number of neurons in the output layer: `1`
* Activation function in the output layer: `sigmoid`
* Loss function: `binary_crossentropy` (log loss)

**Multiclass classification**
* Number of neurons in the output layer: `<num_classes>`
* Activation function in the output layer: `softmax`
* Loss function: `categorical_crossentropy` (n log loss)

#### Regression
* Number of neurons in the output layer: `1`
* Activation function in the output layer: `linear`
* Loss function: `mse` or `mae`

#### Complex outputs (i.e. YOLO)
* Number of neurons in the output layer: `<to_define>`
* Activation function in the output layer: `<to_define>`
* Activation function in the output layer: `<to_define>`
