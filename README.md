# Dermoally-model

## 1. Load Datasets 



## 2. Pre-processing Datasets
The preprocessing pipeline includes:
  - Data Loading and Labeling:
    - _data_appender_ function collects image paths and labels from specified folders.
    - Converts collected data into a DataFrame dataset with image paths and labels.
  - Data Visualization:
    - Displays a grid of sample images and a pie chart of label distribution.
  - Dataset Splitting:
    - _dataset_splitter_ function splits data into training, validation, and test sets.
    - Splits the dataset into 80% training data and 20% test data.
  - Data Augmentation and Generators:
    - Defines datagen with augmentation techniques for training like rotation, shift, shear, zoom, flips, and rescaling to create a robust model.
    - The training data generator uses datagen to load images from the training DataFrame, resizing them to 224x224 pixels, and encoding labels as categorical data.
    - Separate data generators for validation and test sets use rescaling without augmentation to load images from their respective DataFrames for evaluation.
      
## 3. Training

## 4. Saved the Model
