#@title Nonlinear Regression with Keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy
import pandas as pd
# %matplotlib inline

# #Red data from csv file for training and validation data
TrainingSet = numpy.genfromtxt("./data/filtered_data.csv", delimiter=",", skip_header=True)
ValidationSet = numpy.genfromtxt("./data/filtered_data.csv", delimiter=",", skip_header=True)

# TrainingSet = pd.read_csv("dataTrain.csv")
# ValidationSet = pd.read_csv("dataTest.csv")
# split into input (X) and output (Y) variables
X1 = TrainingSet[:,0:3]
Y1 = TrainingSet[:,3]

print(X1)
print(Y1)

X2 = ValidationSet[:,0:3]
Y2 = ValidationSet[:,3]

print(X2,Y2)

# create model
model = Sequential()
model.add(Dense(20, activation="tanh", input_dim=3, kernel_initializer="uniform"))
model.add(Dense(20, activation="relu", kernel_initializer="uniform"))
model.add(Dense(1, activation="linear", kernel_initializer="uniform"))

# Compile model
model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(X1, Y1, epochs=10000, batch_size=10,  verbose=2)

# Calculate predictions
PredTestSet = model.predict(X1)
PredValSet = model.predict(X2)

# Save predictions
numpy.savetxt("trainresults.csv", PredTestSet, delimiter=",")
numpy.savetxt("valresults.csv", PredValSet, delimiter=",")


#Plot actual vs predition for training set
TestResults = numpy.genfromtxt("data/trainresults.csv", delimiter=",")
plt.plot(Y1,TestResults,'ro')
plt.title('Training Set')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.show()
#Compute R-Square value for training set
TestR2Value = r2_score(Y1,TestResults)
print("Training Set R-Square=", TestR2Value)


#Plot actual vs predition for validation set
ValResults = numpy.genfromtxt("data/valresults.csv", delimiter=",")
plt.plot(Y2,ValResults,'ro')
plt.title('Validation Set')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.show()
#Compute R-Square value for validation set
ValR2Value = r2_score(Y2,ValResults)
print("Validation Set R-Square=",ValR2Value)
model.save("model/model.h5")
print("Saved model to disk")