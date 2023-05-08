# Wine quality prediction

## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Algorithms](#algorithms)
- [Results](#results)

## Introduction

This project utilizes Scikit-Learn machine learning algorithms to predict the wine quality from 12 features of two datasets that were combined from <https://archive.ics.uci.edu/ml/datasets/Wine+Quality>.

## Technologies Used

- Scikit-learn
- Numpy
- Seaborn
- Matplotlib
- Xgboost

## Algorithms

- Logistic Regression Multi-class
- KNN
- Linear SVM
- SVM (RBF)
- Naive Bayes
- Decision Tree
- Random Forest
- XGBoost

## Results

The purpose of this project was to gain experience in utilizing scikit-learn machine learning algorithms and deploy model using Flask, Docker and Heroku. AWS and Azure are being explored for deployment in the future.  The results were good with most models above 80 for accuracy.  In this specific exmaple Decision Tree had the best results and that model was saved and containerized for deployment.
