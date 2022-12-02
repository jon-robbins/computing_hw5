import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

class myfunctions():
    def sample_diabetes_mellitus_predict(path='',filename='sample_diabetes_mellitus_data.csv'):
        # a Load the data.
        df =  pd.read_csv(path + filename, sep = ',')
        df_copy = df.copy()

        # c Remove those rows that contain NaN values in the columns: age, gender, ethnicity.
        df_copy = df_copy.dropna(axis=0,subset=['age','gender','ethnicity'])

        # d Fill NaN with the mean value of the column in the columns: height, weight.
        df_copy.loc[df_copy["height"].isna(),"height"] = df["height"].mean()
        df_copy.loc[df_copy["weight"].isna(),"weight"] = df["weight"].mean()

        # e Generate dummies for ethnicity column (One hot encoding).
        df_copy = pd.get_dummies(df_copy, columns = ["ethnicity"])

        # f Create a binary variable for gender M/F.
        df_copy['gender'] = [0 if x == 'M' else 1 for x in df_copy['gender']]

        # b Split the data between train and test. (you can use train_test_split from sklearn or any other way)
        SEED = 0
        features = ['age','height','weight','aids','cirrhosis','hepatic_failure','immunosuppression','leukemia','lymphoma','solid_tumor_with_metastasis']
        X = df_copy.loc[:, features]
        y = df_copy.loc[:, 'diabetes_mellitus']
        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = SEED, train_size = .90)

        # g Train a model (for instance LogisticRegression or RandomForestClassifier from sklearn) in the train data.
        # Use as features the columns: ‘age’, ‘height’, ‘weight’, ‘aids’, ‘cirrhosis’, ‘hepatic_failure’,
        # ‘immunosuppression’, ‘leukemia’, ‘lymphoma’, ‘solid_tumor_with_metastasis’.
        # Use as target the column: ‘diabetes_mellitus’
        model = LogisticRegression()
        model.fit(X_train, y_train)

        # h Predict the targets for both the train and test sets and add the prediction as a new column
        # (use predict_proba from the model to get the predicted probabilities) name the new column something like predictions.
        y_train_pred = np.squeeze(model.predict_proba(X_train)[:, 1])
        y_test_pred = np.squeeze(model.predict_proba(X_test)[:, 1])
        X_train['predictions'] = y_train_pred
        X_test['predictions'] = y_test_pred

        # i. Compute the train and test roc_auc metric using roc_auc_score from sklearn.
        roc_auc_score(y_train, y_train_pred)
        roc_auc_score(y_test, y_test_pred)