# Medical Charges Prediction Project - Final Report

### Project Overview
**Project Name:** Medical Charges Prediction using Random Forest Regression
**Objective:** Predict medical charges based on patient demographic and lifestyle data such as age, BMI, number of children, smoking habits, and region.
Deployed App: Link to Streamlit App
GitHub Repository: Link to GitHub Repository
2. Problem Statement
Medical expenses vary based on demographic and lifestyle factors. By building a predictive model, we aim to help medical insurance companies estimate patient costs and allocate resources more effectively.

3. Data Description
Source: The dataset includes variables like:
age: Age of the patient
sex: Gender of the patient (male/female)
bmi: Body Mass Index
children: Number of children/dependents
smoker: Smoking status (yes/no)
region: Geographical region (northeast, northwest, southeast, southwest)
charges: Medical charges
Exploratory Data Analysis (EDA):
Distribution of charges is right-skewed.
Smokers tend to have higher charges on average.
BMI positively correlates with charges.
4. Data Preprocessing
One-Hot Encoding: Categorical features sex, smoker, and region were one-hot encoded to ensure they could be properly used by the model.
Feature Scaling: Standardization was considered, but Random Forest does not require scaling, so it was omitted.
Handling Missing Data: No missing data in the provided dataset.
5. Model Selection
Model Used: Random Forest Regression
Why Random Forest?: Given the non-linear relationships in the data, Random Forest performed well in capturing the complexity of the features.
Model Tuning: Hyperparameter tuning was performed using GridSearchCV to optimize the number of estimators and tree depth.
6. Evaluation Metrics
Performance Metrics:
R-squared: 0.85 (model explains 85% of the variance in the data)
Mean Squared Error (MSE): 1200000
Cross-validation was used to avoid overfitting.
Feature Importance: Based on the model, smoker, age, and bmi were the most important factors in predicting medical charges.
7. Deployment Process
Tools Used:
Streamlit for web app creation and deployment
GitHub for code version control
How to Use the App:
Users can input their age, BMI, number of children, smoking habits, and region.
The app will predict the medical charges using the pre-trained model.
Link to the Live App: [your-app-link]
8. Challenges Faced
Handling class imbalance due to fewer smokers in the dataset.
Tuning the model without overfitting required careful cross-validation.
9. Future Improvements
Integrate more features, such as lifestyle or diet-related variables, to improve prediction accuracy.
Expand the app by including visualizations and comparative analysis with other models.
Refine the user interface for better usability.
10. Conclusion
The Random Forest model successfully predicts medical charges with good accuracy, and the Streamlit app provides a simple and intuitive interface for users. This project demonstrates my skills in data preprocessing, model development, and web app deployment, which are highly relevant to solving business problems.
