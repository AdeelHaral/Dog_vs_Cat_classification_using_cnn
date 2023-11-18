import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input

# Load the trained model
model_path = '/content/drive/MyDrive/model.h5'  # Replace with the actual path to your model file
model = load_model(model_path)

# Function to preprocess the uploaded image
def preprocess_image(img_path):
    test_image = image.load_img(img_path, target_size = (64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)

    return test_image

# Streamlit app
st.image('/content/drive/MyDrive/ks.jpeg')
st.title('Image Classification App')

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

    # Preprocess the image
    img_array = preprocess_image(uploaded_file)

    # Make predictions
    prediction = model.predict(img_array)
    class_label = 'Dog' if prediction[0][0] > 0.5 else 'Cat'  # Modify based on your binary classification labels

    # Display the prediction
    st.subheader('Prediction:')
    st.subheader(f'The image is classified as a {class_label}')
