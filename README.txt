README
Indian Medicinal Leaves Classification Application
This application classifies Indian medicinal leaves based on uploaded images. It uses a pre-trained TensorFlow model and a Streamlit-based front-end interface.

Prerequisites
1. Python Environment
Ensure Python (>=3.8) is installed on your system.
2. Install Required Libraries
Install the necessary Python packages. Run the following command in your terminal:
                     pip install tensorflow numpy streamlit matplotlib pillow
3. Dataset and Model Files
o Place the trained model file medicinal_leaf_model.h5 in the project directory.
o Ensure the dataset folder Indian Medicinal Leaves Image Datasets/Medicinal Leaf dataset is present for retrieving class names.

Running the Application
Step 1: Navigate to the Project Directory
Open a terminal and navigate to the folder where the app.py script is located.
Step 2: Run the Streamlit Application
Execute the following command:
streamlit run app.py
Step 3: Open the Web Interface
Once the server starts, a URL will appear in the terminal (e.g., http://localhost:8501).
Copy and paste it into a web browser to access the application.

Using the Application
1. Upload an Image
o Click the "Upload an image" button.
o Select an image file in .jpg, .png, or .jpeg format.
2. View Predictions
o The application will display the uploaded image.
o The predicted class name for the medicinal leaf will be shown below the image.

