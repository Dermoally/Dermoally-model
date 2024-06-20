# Dermoally Model
## 1. Load Datasets 
Load Datasets from Modified dataset that we host to Google Drive, here is the link: https://drive.google.com/file/d/1Z0ffQw1uS85rdP25M81SFbHtNJMGMH_m/view?usp=sharing

## 2. Pre-processing Datasets
The preprocessing pipeline includes:
  - Data Loading and Labeling:
    - `data_appender` function collects image paths and labels from specified folders.
    - Converts collected data into a DataFrame dataset with image paths and labels.
  - Data Visualization:
    - Displays a grid of sample images and a pie chart of label distribution.
  - Dataset Splitting:
    - `dataset_splitter` function splits data into training, validation, and test sets.
    - Splits the dataset into 80% training data and 20% test data.
  - Data Augmentation and Generators:
    - Defines datagen with augmentation techniques for training like rotation, shift, shear, zoom, flips, and rescaling to create a robust model.
    - The training data generator uses datagen to load images from the training DataFrame, resizing them to 224x224 pixels, and encoding labels as categorical data.
    - Separate data generators for validation and test sets use rescaling without augmentation to load images from their respective DataFrames for evaluation.
      
## 3. Training
  - **Base Model**: InceptionV3 pre-trained on ImageNet, excluding the top layers and set with an input shape of (224, 224, 3).
    - All layers in the base model are frozen to preserve the pre-trained weights.
  - **Custom Layers**:
    - Input Layer: Accepts input images of size 224x224 with 3 color channels.
    - `Global Average Pooling`: Flattens the output from the base model.
    - `Dense Layer (512 units)`: Fully connected layer with ReLU activation.
    - `Dropout (0.3)`: Adds regularization to reduce overfitting.
    - `Dense Layer (256 units)`: Another fully connected layer with ReLU activation.
    - `Dropout (0.3)`: Additional regularization.
    - Output Layer: Dense layer with softmax activation for multi-class classification, corresponding to the number of unique labels in the training data.
  - **Compilation**:
    - Optimizer: Adam with a learning rate of 0.0001.
    - Loss Function: Categorical Crossentropy.
    - Epoch : 100
    - Metrics: Accuracy.
  - **Result**:
    - `Accuracy : 88%`
    - `Validation Accuracy : 84%`
    - `Loss : 34%`
    - `Validation Loss : 50%`
## 4. Saved the Model
After training the model, it is saved to a file for later use. This allows the trained model to be easily loaded and used for making predictions without needing to retrain it.
  - **Model Saving**:
    - The trained model is saved to a file named `dermoally-modelv7.h5` using the `model.save()` function from TensorFlow/Keras.
    - This step is crucial for deployment and further evaluation, ensuring that the trained model can be reused efficiently.
