# Customer Churn Prediction App

A machine learning web application that predicts whether a customer is likely to churn based subscription details.

## Live Demo

**Streamlit App:** https://customer-churn--predication-eda.streamlit.app/

---

## Project Overview

Customer churn is one of the most important business problems for subscription-based companies such as telecom.

This project uses machine learning to predict whether a customer will leave the service based on features such as:

* Age
* Gender
* Tenure
* Monthly Charges

The model is deployed as an interactive web application using Streamlit.

---

## Business Problem

Acquiring a new customer is often more expensive than retaining an existing one.

By identifying customers who are likely to churn, businesses can:

* Offer targeted discounts
* Improve customer support
* Increase retention
* Reduce revenue loss

---

## Features Used

| Feature        | Description                       |
| -------------- | --------------------------------- |
| Age            | Customer age                      |
| Gender         | Male/Female                       |
| Tenure         | Number of months with the company |
| MonthlyCharges | Monthly subscription cost         |

---

## Target Variable

| Value | Meaning                 |
| ----- | ----------------------- |
| 1     | Customer will churn     |
| 0     | Customer will not churn |

---

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit
* Git & GitHub
* Streamlit Community Cloud

---

## Machine Learning Workflow

1. Data cleaning and preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature selection
4. Train-test split
5. Feature scaling using `StandardScaler`
6. Model training
7. Model serialization with `joblib`
8. Streamlit app development
9. Cloud deployment

---

## Project Structure

```text
Customer-Churn-Prediction/
│── app.py
│── model.pkl
│── scaler.pkl
│── customer_churn_dataset.csv
│── requirements.txt
│── README.md
```

---


## Model Input Order

The model expects features in the following order:

```python
[Age, Gender, Tenure, MonthlyCharges]
```

Where:

* Gender: Female = 1, Male = 0

---

## Sample Prediction

Input:

* Age: 45
* Gender: Female
* Tenure: 6
* Monthly Charges: 85.5

Output:

```text
The customer is likely to Churn
```

---

## Key Insights from EDA

* Customers with higher monthly charges are more likely to churn.
* Customers with shorter tenure have a higher churn probability.
* Tenure is one of the strongest predictors of churn.

---

## Screenshots

<img width="935" height="723" alt="image" src="https://github.com/user-attachments/assets/02cb0028-ffe1-4e46-9629-2049d1ad235e" />


---


## Resume Project Description

Developed a customer churn prediction web application using Python, scikit-learn, and Streamlit. Performed data preprocessing and exploratory data analysis, trained a machine learning model, and deployed the solution on Streamlit Community Cloud.

---

## Author

**Ishita Jain**

* GitHub: (https://github.com/IshitaJain-code)
* LinkedIn:https://www.linkedin.com/in/ishita-jain-5a178a3b0

---

## License

This project is for educational and portfolio purposes.

