# COVID-19 Detection with PyTorch

This repository contains a PyTorch machine learning model for detecting COVID-19 based on chest X-ray images. 

The model classifies images into three categories: Normal, Viral Pneumonia, and COVID-19.

To download dataset first you have to sign in Keggle. https://www.kaggle.com/

Then follow this documentation. https://github.com/Kaggle/kaggle-api

Go to settings and download API key. Copy it into `.keggle folder`.

Run `divide_save_data.py`

There are now 3 datasets, named Hospital_1, Hospital_2, Hospital_3

To run script you have to choose dataset. For example if you want hospital_1, run it with this command:

`python3 covid19.py Hospital_1`

And, because this is not model still, every time you run it, you have to delete test folder.

