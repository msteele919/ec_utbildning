from sklearn.neighbors import KNeighborsClassifier
import numpy as np

#Create arrays for the feautures and the target variable 
y= churn_df["church"].values
X = churn_df["account_length", "customer_service_calls"].values

# Create a KNN classifier with 6 neighbors 
knn = KNeighborsClassifier(n_neighbers= 6)

#Fit the classifier to the data 

knn.fit(X,y)

#Need new data to make predictions

X_new = np.array([[30.0, 17.5],
                  [107.0, 24.1],
                  [213.0, 10.9]])

y_predic = knn.predict(X_new)

print("Predictions: {}".format(y_predic))
