# Workshop-Review-Sentiment-Analysis-Web-App

Greetings! 

The following repository contains the files for the deployment of the Sentiment Analysis model developed by me for the Inception 5.0 workshop as a simple Flask App. 

For the same, I have used the IMDB 50k review dataset and attempted to shift the intuition for detecting a positive or negative workshop review response using various NLP techniques such as POS Tagging on Tokenized sentences, Bag Of Words creation of adjectives, outlier removal and fine tuning, capped off with the use of a simple Naive Bayes model from the NLTK module. 

The construction and explanation of the same were done by me as Speaker during the course of the workshop held on 19-20th March 2021. For reference I have also included the Python Notebook used for the creation of the model. 

A newer model has been developed for the same, which uses Sequential Modelling to better the results achieved in the previous version. The Sequential model utilizes the Bidirectional LSTM cells to view the text as a sequence rather than a simple one hot encoding. 

