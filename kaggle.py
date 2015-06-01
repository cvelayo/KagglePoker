import pandas as pd
import numpy as np
import time

# For .read_csv, always use header=0 when you know row 0 is the header row
df = pd.read_csv('data/train.csv', header=0)
train_data=df.values

testdf = pd.read_csv('data/test.csv', header=0)
test_data = testdf.values

# Import the random forest package
from sklearn.ensemble import RandomForestClassifier 

# Create the random forest object which will include all the parameters
# for the fit
start = time.time()
forest = RandomForestClassifier(n_estimators = 1000)
end = time.time()
elapsed = end - start
print "Time taken for random forest: ", elapsed, "seconds."

# Fit the training data to the Survived labels and create the decision trees
forest = forest.fit(train_data[0::,0:10:],train_data[0::,10])

# Take the same decision trees and run it on the test data
output = forest.predict(test_data[0::,1::])
ids = test_data[0::,0]

predictions_file = open("myfirstforest2.csv", "wb")
open_file_object = csv.writer(predictions_file)
open_file_object.writerow(["id","hand"])
open_file_object.writerows(zip(ids, output))
predictions_file.close()
print 'Done.'