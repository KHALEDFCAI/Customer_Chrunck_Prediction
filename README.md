# Customer Churn Prediction

## 📌 Project Overview
This project is a **Customer Churn Prediction** application built with **Streamlit**. It allows users to upload a CSV file containing customer data and obtain predictions on whether a customer is likely to churn. The model is pre-trained and loaded from a `.pkl` file.

## 🚀 Features
- **CSV Upload**: Users can upload a CSV file with customer data.
- **Data Preview**: The first few rows of the uploaded dataset are displayed.
- **Churn Prediction**: A trained model makes predictions based on the provided data.
- **Probability Scores**: If applicable, the model also provides probability scores for each prediction.
- **Downloadable Results**: Users can download the predictions as a CSV file.

## 📂 Project Structure
```
📁 Customer Churn Prediction
│── cutomer_prediction.py  # Main Streamlit app script
│── model2.pkl             # Pre-trained ML model (loaded in the script)
│── scaler2.pkl (optional) # Pre-trained scaler (if used for preprocessing)
│── bank-customer-churn-prediction-v1.ipynb  # Jupyter notebook for model training (not included in app)
```

## 🛠️ Installation
To run this project locally, follow these steps:

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
```

### 2️⃣ Install Dependencies
Ensure you have Python installed, then install the required libraries:
```sh
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, install the main dependencies manually:
```sh
pip install streamlit pandas pickle5
```

### 3️⃣ Run the Streamlit App
```sh
streamlit run cutomer_prediction.py
```

## 📝 Usage
1. **Upload a CSV File** with customer data.
2. Click on **Submit** to process the file and generate predictions.
3. View the **predicted churn status** and probability scores.
4. **Download** the predictions as a CSV file.

## 🔧 Configuration
- The model file (`model2.pkl`) should be available in the project directory.
- Modify `model_path` and `scaler_path` in `cutomer_prediction.py` if needed.

## 🏗️ Future Enhancements
- Improve model accuracy with more feature engineering.
- Add real-time visualization of predictions.
- Deploy on a cloud platform (e.g., AWS, Heroku).

## 📜 License
This project is licensed under the **MIT License**.

## 🤝 Contributing
Feel free to submit issues and pull requests for improvements.

---
🔗 **Developed by:** KHALED_MOUSA

