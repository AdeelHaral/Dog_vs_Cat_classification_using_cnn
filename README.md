# Dog vs. Cat Image Classifier

## Overview

This project is a Deep Learning-based image classifier that can distinguish between images of dogs and cats. It includes an IPython notebook for model training and a Streamlit app for testing.

## Project Structure

- **`notebooks/`**: Contains the Jupyter notebook (`dog_vs_cat_classifier.ipynb`) for model training.
- **`src/`**: Contains the Streamlit app (`app.py`) for testing the trained model.
- **`model/`**: Location to save the trained model (`model.h5`).
- **`data/`**: Placeholder for dataset. Add your images to this directory.

## Instructions

### Model Training

1. Open the Jupyter notebook `dog_vs_cat_classifier.ipynb` in the `notebooks/` directory.
2. Replace the dataset in the `data/` directory with your own images.
3. Run the notebook to train the model and save it in the `model/` directory as `model.h5`.

### Streamlit App

1. Ensure you have the required dependencies installed:

    ```bash
    pip install -r requirements.txt
    ```

2. Open `app.py` in the `src/` directory.
3. Replace the model path with your trained model's path:

    ```python
    # Update this line with the path to your trained model
    model_path = '/path/to/your/model.h5'
    ```

4. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

5. Access the app in your browser and upload images for predictions.

## Acknowledgments

- Thanks to Knowledge Stream Bootcamp for the guidance and support during this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
