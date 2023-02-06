import streamlit as st
import pandas as pd
import numpy as np

from PIL import Image
from torchvision import models
from src import helpers

model = # download the pretrained model, e.g. resnet50
model.eval()


# set the title of the application using streamlit functions

# use the st.camera_input("") feature of the streamlit to get the input picture of the user

# load the vectors of the dataset pictures and use the helper function to compare them to the input

# print a result for the user! what dog breed is the selfie most similar to? :)



### additional ideas:
    # - enrich the page layout, add texts, input fields, result metrics - be creative
    # - ask the user if he/she/it is a cat or dog person and based on the answer choose dataset - for cats use images from https://www.kaggle.com/datasets/ma7555/cat-breeds-dataset
    # - add your project to github repository and deploy your app to streamlit cloud!