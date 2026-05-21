import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# 1. Load Dataset
data = pd.read_csv("data3.csv")

# 2. Convert text data into numbers
df_encoded = data.apply(lambda col: col.astype('category').cat.codes)

# Features (X) and Target (y)
X = df_encoded.iloc[:, :-1]
y = data.iloc[:, -1]

# 3. Train Decision Tree using ID3 (entropy)
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)

# 4. Test Sample
test_sample = pd.DataFrame([[1, 0, 1, 0]], columns=X.columns)

prediction = model.predict(test_sample)

print("Final Prediction:", prediction[0])
