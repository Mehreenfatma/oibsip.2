from flask import Flask, request, render_template
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
with open(r"C:\Users\HP\OneDrive\Desktop\sales prediction\sales.pickle", "rb") as file:
    model = pickle.load(file)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    try:
        tv = float(request.form['tv'])
        radio = float(request.form['radio'])
        newspaper = float(request.form['newspaper'])
        
        # Make prediction
        prediction = model.predict(np.array([[tv, radio, newspaper]]))
        
        # Return the result
        return render_template('index.html', prediction_text=f'Predicted Sales: ${prediction[0]:.2f}')
    
    except ValueError:
        return render_template('index.html', prediction_text="Please enter valid numbers.")

if __name__ == "__main__":
    app.run(debug=True)
