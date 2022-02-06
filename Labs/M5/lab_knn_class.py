# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv(
    "https://raw.githubusercontent.com/grbruns/cst383/master/College.csv", index_col=0
)

# 3
df.info()
df.describe()

# 4
X = df[["Outstate", "F.Undergrad"]].values
y = (df["Private"] == "Yes").values.astype(int)  # Private == 1
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 5
X_train[:10]

# 6
knn = KNeighborsClassifier() # uses n_neighbors=5 as default
knn.fit(X_train, y_train) # train using fit

# 7 
predictions = knn.predict(X_test)

# 8
predictions[:10]
y_test[:10]

# 9
accuracy = (predictions == y_test).mean()

# 10
accuracy.round(3)

# 11
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train) # train using fit
predictions = knn.predict(X_test)
accuracy = (predictions == y_test).mean()
accuracy.round(3)
