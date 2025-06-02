from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load your trained model
model = joblib.load('models/youtube_revenue_predictor.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    error = None
    
    if request.method == 'POST':
        try:
            # Extract input values from form
            views = float(request.form['views'])
            subscribers = float(request.form['subscribers'])
            likes = float(request.form['likes'])
            shares = float(request.form['shares'])
            new_comments = float(request.form['new_comments'])
            engagement_rate = float(request.form['engagement_rate'])
            
            # Prepare data for prediction (model expects 2D array)
            features = np.array([[views, subscribers, likes, shares, new_comments, engagement_rate]])
            
            # Predict revenue
            prediction = model.predict(features)[0]
            prediction = round(prediction, 2)
        except Exception as e:
            error = str(e)
    
    return render_template('index.html', prediction=prediction, error=error)

if __name__ == '__main__':
    app.run(debug=True)
