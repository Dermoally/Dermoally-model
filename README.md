# Dermoally-model

## 1. Load Datasets 



## 2. Pre-processing Datasets
The preprocessing pipeline includes:
  - Data Loading and Labeling:
    - 'data_appender' function collects image paths and labels from specified folders.
    - Converts collected data into a DataFrame dataset with image paths and labels.
  - Data Visualization:
    - Displays a grid of sample images and a pie chart of label distribution.
  - Dataset Splitting:
    - dataset_splitter function splits data into training, validation, and test sets.
    - Splits the dataset into 80% training data and 20% test data.
  - Data Augmentation and Generators:
    - Defines datagen with augmentation techniques for training like rotation, shift, shear, zoom, flips, and rescaling to create a robust model.
    - Creates data generators for training (with augmentation), validation, and test sets (without augmentation).
      
## 3. Training

## 4. Saved the Model
