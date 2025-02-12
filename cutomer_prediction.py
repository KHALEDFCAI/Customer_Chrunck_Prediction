import streamlit as st
import pandas as pd
import pickle
import os

def load_model(model_path):
    if os.path.exists(model_path):
        with open(model_path, "rb") as f:
            return pickle.load(f)
    else:
        st.error(f"❌ لم يتم العثور على ملف النموذج: {model_path}")
        return None

def preprocess_data(df, scaler_path=None):
    if scaler_path and os.path.exists(scaler_path):
        with open(scaler_path, "rb") as f:
            scaler = pickle.load(f)
        df = scaler.transform(df) 
    return df  

def main():
    st.title("📊 تطبيق التنبؤ CSV")
    st.write("قم بتحميل ملف CSV يحتوي على البيانات، ثم اضغط على **Submit** للحصول على التوقعات.")

    # المسارات
    model_path = r"D:\Prctise\customer_prediction\model2.pkl"
    scaler_path = r"D:\Prctise\customer_prediction\scaler2.pkl"  

    uploaded_file = st.file_uploader("📂 تحميل ملف CSV", type=["csv"], accept_multiple_files=False)
   

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.write("### 👀 معاينة البيانات المرفوعة:")
        st.dataframe(df.head())
        submit_button = st.button("🚀 تنفيذ التوقعات")
        if submit_button:
            model = load_model(model_path)
            if model is None:
                return

            processed_data = preprocess_data(df, scaler_path=None) 

            try:
                predictions = model.predict(processed_data)
                
                if hasattr(model, "predict_proba"):
                    probabilities = model.predict_proba(processed_data)[:, 1]
                    df["Probability"] = probabilities

                df["Prediction"] = predictions

                st.write("### 🔍 نتائج التنبؤ:")
                st.dataframe(df.head(15))

                csv = df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="⬇️ تحميل نتائج التنبؤ",
                    data=csv,
                    file_name="predictions.csv",
                    mime="text/csv",
                )
            except Exception as e:
                st.error(f"❌ حدث خطأ أثناء التنبؤ: {e}")

if __name__ == "__main__":
    main()
