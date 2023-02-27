from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

# #Create arrays for the feautures and the target variable 
# y = churn_df["church"].values
# X = churn_df["account_length", "customer_service_calls"].values

# # Create a KNN classifier with 6 neighbors 
# knn = KNeighborsClassifier(n_neighbers= 6)

# #Fit the classifier to the data 

# knn.fit(X,y)

# #Need new data to make predictions

# X_new = np.array([[30.0, 17.5],
#                   [107.0, 24.1],
#                   [213.0, 10.9]])

# y_predic = knn.predict(X_new)

# print("Predictions: {}".format(y_predic))


############################################
# Measuring Performance of our model # 


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state= 21, stratify=y)
#set test size = 0.3 says that 30% of the data is test data

# random_state= sets the seed for the random number generator to split the data randomly

#  stratify says the amount of the 
# we want the split to represent the exact proportion of the times our y variable is equal to 1. we are setting the percentage of the times the labels are equal to y. do this by setting stratify equal to the dependent variable
knn = KNeighborsClassifier(n_neighbors = 6)
knn.fit(X_train, y_train)
print(knn.score(X_test, y_test)) # score is a method that judges the accuracy of the model 
#in the example with the churn_df, the score was .88 which is considered low since the labels have a 9 to 1 ratio. 


############################################
# Model complexity curve #
# we plot the results of incremently greater values of k to measure over/underfitting the model
train_accuracies = {}
test_accuracies = {}
neighbors = np.arrange(1, 26) # sets the range of possible number of neighbors 

# use a for loop to create n models with n+1 neighbors 

for neighbor in neighbors: 
    knn = KNeighborsClassifier(n_neighbors=neighbor)
    knn.fit(X_train, y_train)
    train_accuracies[neighbor] = knn.score(X_train, y_train) #calculate accuracy and store results in dictionaies
    test_accuracies[neighbor] = knn.score(X_test, y_test)


#plot the results 


plt.figure(figsize=(8,6))
plt.title("KNN: Varying Number of Neighbors")
plt.plot(neighbors, train_accuracies.values(), label= "Training Accuracy")
plt.plot(neighbors, test_accuracies.values(), label="Testing Accuracy")
plt.legend()
plt.xlabel("Number of Neighbors")
plt.ylabel("Accuracy")
plt.show()



