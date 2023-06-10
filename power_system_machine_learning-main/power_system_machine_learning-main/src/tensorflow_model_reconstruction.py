from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy
import pandas as pd
import keras
# #Red data from csv file for training and validation data
TrainingSet = numpy.genfromtxt("../data/dataTrain2.csv", delimiter=",", skip_header=True)
ValidationSet = numpy.genfromtxt("../data/dataTest2.csv", delimiter=",", skip_header=True)

X1 = TrainingSet[:,0:4]
Y1 = TrainingSet[:,4]

X2 = ValidationSet[:,0:4]
Y2 = ValidationSet[:,4]

...
# equivalent to: model.save("model.h5")
reconstructed_model = keras.models.load_model("model.h5")


# Calculate predictions
PredTestSet = reconstructed_model.predict(X1)
PredValSet = reconstructed_model.predict(X2)

# Save predictions
numpy.savetxt("trainresults.csv", PredTestSet, delimiter=",")
numpy.savetxt("valresults.csv", PredValSet, delimiter=",")


#Plot actual vs predition for training set
TestResults = numpy.genfromtxt("trainresults.csv", delimiter=",")
plt.plot(Y1,TestResults,'ro')
plt.title('Training Set')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.show()
#Compute R-Square value for training set
TestR2Value = r2_score(Y1,TestResults)
print("Training Set R-Square=", TestR2Value)


#Plot actual vs predition for validation set
ValResults = numpy.genfromtxt("valresults.csv", delimiter=",")
plt.plot(Y2,ValResults,'ro')
plt.title('Validation Set')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.show()
#Compute R-Square value for validation set
ValR2Value = r2_score(Y2,ValResults)
print("Validation Set R-Square=",ValR2Value)
reconstructed_model.save("../output_model/model.h5")
print("Saved model to disk")