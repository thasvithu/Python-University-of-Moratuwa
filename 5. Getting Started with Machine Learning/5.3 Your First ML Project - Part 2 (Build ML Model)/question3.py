import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load training and test datasets
train_df = pd.read_csv('student_marks_train.csv')
test_df = pd.read_csv('student_marks_test.csv')

# EDA - Pairplot for visualization
sns.pairplot(train_df, hue='class-label', markers='+')
plt.show()

# Preprocessing
X_train = train_df.drop(['class-label'], axis=1)
y_train = train_df['class-label']

# Splitting the training data into train and validation sets
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=1)

# SVM model
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)

# Model evaluation
predictions = svm.predict(X_val)
print("Accuracy on validation set:", accuracy_score(y_val, predictions))

# Predicting the test dataset
test_predictions = svm.predict(test_df)

# Outputting predictions
print("------CLASSIFICATION RESULTS START------")
for prediction in test_predictions:
    print(prediction)
print("------CLASSIFICATION RESULTS END------")
