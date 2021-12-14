# Intro to Machine Learning Final Project

C. Cook & K. Thach

## Objective

Generate and train a model on a dataset. Validate the model on a TEST set. Report all findings. 

## Project Proposal 

We intend to create a machine learning algorithm to detect distribution structures, lines, and components (transformers, insulators, connectors) through the use of drone imagery from field inspections. To improve the plausibility of autonomous inspections using drones to reduce blackouts and wildfires. 

Details of the project (Name sources of selected datasets, detailed training and evaluation plan):
        	
* Select 6 total circuits
* Develop image processing algorithm to detect objects/ extracting features
* Implement dimensionality reduction (PCA, LDA)
* Split our dataset into  training and evaluation sets, 80%/20% respectively.
* Train our model using various classification methods/regression techniques.

**A projection of achievable outcomes:** Detect a structure within an image, at a minimum. Possibly determine if that component is a transformer or not. 

Sources for dataset: https://ieee-dataport.org/open-access/drone-based-distribution-inspection-imagery

Object Detection (Google Colab): https://colab.research.google.com/drive/1lbqVcJDhxicWGAWJYHdgEwx9_VLkSD27#scrollTo=wOk22-6-IVkR

## Resources 

* Object Labeling: https://github.com/microsoft/VoTT
* CNN: https://www.datacamp.com/community/tutorials/convolutional-neural-networks-python
* CNN 2: https://cs231n.github.io/convolutional-networks/
* R-CNN: https://www.datacamp.com/community/tutorials/object-detection-guide
* Example: https://www.pyimagesearch.com/2020/10/05/object-detection-bounding-box-regression-with-keras-tensorflow-and-deep-learning/
* Example 2: https://medium.com/nerd-for-tech/building-an-object-detector-in-tensorflow-using-bounding-box-regression-2bc13992973f
* TensorFlow Start: https://www.tensorflow.org/tutorials/images/cnn

