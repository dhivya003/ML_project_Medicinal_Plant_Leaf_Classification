%%writefile app.py
import tensorflow as tf
import numpy as np
import streamlit as st
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import matplotlib.pyplot as plt
import os

IMAGE_RES = 224
BATCH_SIZE = 32


@st.cache_resource
def load_model():

    model = tf.keras.models.load_model('medicinal_leaf_model.h5')
    return model


@st.cache_resource
def get_class_names(dataset_path):
    class_names = sorted(os.listdir(dataset_path))
    return class_names


dataset_path = 'Indian Medicinal Leaves Image Datasets/Medicinal Leaf dataset'


model = load_model()
class_names = get_class_names(dataset_path)


st.title("Indian Medicinal Leaves Classification")
st.write("Upload an image to predict the medicinal leaf class.")


uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:

    input_image = load_img(uploaded_file, target_size=(IMAGE_RES, IMAGE_RES))
    input_image_array = img_to_array(input_image)
    input_image_array = input_image_array / 255.0
    input_image_array = input_image_array[tf.newaxis, ...]


    predictions = model.predict(input_image_array)
    predicted_class_index = tf.argmax(predictions, axis=1).numpy()[0]
    predicted_class_name = class_names[predicted_class_index]


    st.image(input_image, caption="Uploaded Image", use_column_width=True)
    st.write(f"Predicted Class: {predicted_class_name}")