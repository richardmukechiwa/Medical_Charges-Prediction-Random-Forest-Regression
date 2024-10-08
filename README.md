[medicalbillsprediction]()
# Medical Charges Prediction Project 

### Project Overview

**Project Name:** Medical Charges Prediction using Random Forest Regression

**Objective:** Predict medical charges based on patient demographic and lifestyle data such as age, BMI, number of children, smoking habits, and region.

**Deployed App:** https://medicalcharges-prediction-random-forest-regression-u9bhntftna2.streamlit.app/

 ### Problem Statement
 
- Medical expenses vary based on demographic and lifestyle factors. By building a predictive model, I aim to help medical insurance companies estimate patient costs and allocate resources more effectively.

### Data Description

**Source:** https://www.kaggle.com/datasets/simranjain17/insurance

#### The dataset includes variables like:

**age:** Age of the patient

**sex:** Gender of the patient (male/female)

**bmi:** Body Mass Index

**children:** Number of children/dependents

**smoker:** Smoking status (yes/no)

**region:** Geographical region (northeast, northwest, southeast, southwest)

**charges:** Medical charges

### Exploratory Data Analysis (EDA):

- Distribution of charges is right-skewed/ positive skewnessness
  
- Smokers tend to have higher charges on average.

- The northeast region has highest charges

- Those with more dependances has low charges where as those without children have the highest charges
  
### Data Preprocessing

**One-Hot Encoding:** Categorical features sex, smoker, and region were one-hot encoded to ensure they could be properly used by the model.

**Handling Missing Data:**  No missing data in the provided dataset.

### Model Selection

**Models Used:** Multi-LinearRegression, Ridge, Lasso and Random Forest Regression

**Why Random Forest?:** Given the non-linear relationships in the data, Random Forest performed well in capturing the complexity of the features.

**Model Tuning:** Hyperparameter tuning was performed using GridSearchCV to optimize the number of estimators and tree depth.

### Evaluation Metrics

#### **Performance Metrics:**

**R-squared:** 0.93 (model explains 93% of the variance in the data)

**Mean Squared Error (MSE):** 2436

- Cross-validation was used to avoid overfitting

**Feature Importance:** Based on the model, smoker, age, and bmi were the most important factors in predicting medical charges.

### Deployment Process

**Tools Used:**

Streamlit for web app creation and deployment
GitHub for code version control

**How to Use the App:**

- Users can input their age, BMI, number of children, smoking habits, and region.
- The app will predict the medical charges using the pre-trained model.
  
**Link to the Live App:** https://medicalcharges-prediction-random-forest-regression-u9bhntftna2.streamlit.app/

### Challenges Faced

- Handling one hot coded variables
- deploying the model

### Future Improvements

- there is need to integrate more features, such as lifestyle or diet-related variables, to improve prediction accuracy.
  
- Refine the user interface for better usability.

## Conclusion

The Random Forest model successfully predicts medical charges with good accuracy, and the Streamlit app provides a simple and intuitive interface for users. This project demonstrates my skills in data preprocessing, model development, and web app deployment, which are highly relevant to solving business problems.

### Thank you.
