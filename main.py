import numpy as np 
import pandas as pd
import tensorflow as tf
from tensorflow.keras.datasets import imdb 
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
import streamlit as st
import os

df = pd.read_excel("customer_churn_large_dataset.xlsx")
df.head()

model = load_model(model_path) = "customer_churn_model.h5"
