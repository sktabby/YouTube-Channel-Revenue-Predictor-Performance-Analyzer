
# 🎥 YouTube Channel Revenue Predictor & Performance Analyzer

## 🚀 Project Overview

This project provides a comprehensive analysis of YouTube channel performance data to uncover key revenue-driving factors. It uses **machine learning** techniques to predict the estimated revenue of YouTube videos based on various video metrics like views, likes, comments, and engagement rates. The project includes:

✅ Data preprocessing, feature engineering, and exploratory data analysis (EDA)  
✅ Random Forest Regressor model for revenue prediction  
✅ Visualizations for insights and understanding feature importance  
✅ Flask-based web application for interactive revenue prediction  

---

## 📂 Dataset

The dataset (`youtube_channel_real_performance_analytics.csv`) contains various metrics for YouTube videos, such as:

- 📺 Video Duration  
- 📅 Publish Time  
- 👀 Views  
- 👍 Likes, 🔗 Shares, 💬 Comments  
- 💰 Estimated Revenue (USD)  
- 📈 Subscribers  
- 📊 Engagement Metrics (e.g., Engagement Rate, Revenue per View)  

Place the CSV file in the `data/` directory.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/youtube-revenue-prediction.git
cd youtube-revenue-prediction
````

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv

# For Windows:
venv\Scripts\activate

# For macOS/Linux:
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Data Processing & Model Training

This will clean the data, perform EDA, train the model, and generate visualizations.

```bash
python main.py
```
![revenue_vs_views](https://github.com/user-attachments/assets/fb7e45ff-9ea7-44d8-af83-c2799dbb0c97)
![revenue_distribution](https://github.com/user-attachments/assets/b227dc4a-de11-4391-95c8-f6261f9e8505)
![feature_importance](https://github.com/user-attachments/assets/50262fa2-41d1-4147-bd72-454d4f60efe4)
![correlation_heatmap](https://github.com/user-attachments/assets/a8fb46ed-7265-4ab6-abf7-b27fa85d05e8)

### 5️⃣ Start the Flask Web Application

```bash
python app.py
```
![Screenshot 2025-06-02 213950](https://github.com/user-attachments/assets/353aa887-ce6b-41db-9e67-4e659a93c0bf)

### 6️⃣ Access the Web App

Open your browser and navigate to:

```
http://127.0.0.1:5000/
```

---

## 🌐 Web App Usage

* Fill in the form with video metrics: Views, Subscribers, Likes, Shares, Comments, Engagement Rate, etc.
* Click **Predict** to estimate the revenue for the video.
* Visualizations like revenue distribution and feature importance are available in the `outputs/plots/` directory.

---

## 🗂️ Project Structure

```
youtube-revenue-prediction/
│
├── data/
│   └── youtube_channel_real_performance_analytics.csv
│
├── models/
│   └── youtube_revenue_predictor.pkl
│
├── outputs/
│   └── plots/
│       ├── revenue_distribution.png
│       ├── revenue_vs_views.png
│       └── feature_importance.png
│
├── static/
│   └── css/
│       └── styles.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py            # Flask web app
├── main.py           # Data processing, EDA, and model training
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

---

## 🛠️ Technologies Used

* **Python 3.x**
* **Pandas, NumPy** – Data handling
* **Scikit-learn** – Machine learning
* **Matplotlib, Seaborn** – Visualizations
* **Flask** – Web interface
* **Joblib** – Model persistence

---

## 🌟 Future Enhancements

* 🔍 Advanced feature engineering & hyperparameter tuning
* 📡 Real-time data fetching from YouTube API
* ☁️ Cloud deployment (Heroku, AWS, etc.)
* 🔒 User authentication for personalized analytics
* 📊 Interactive dashboards and detailed visualizations

---

## 📝 License

This project is licensed under the **MIT License**.

---

## 🙌 Author

**Aqsa Shah**
GitHub: [yourusername](https://github.com/yourusername)
LinkedIn: [yourprofile](https://linkedin.com/in/yourprofile) *(optional)*

---

## 💬 Contributions

Feel free to **open issues** or submit **pull requests** for improvements!
Thank you for checking out the project! 🎉

```

---

✅ Let me know if you'd like to update your repo link or need **help with the Flask app code, HTML templates, or CSS**!
```
