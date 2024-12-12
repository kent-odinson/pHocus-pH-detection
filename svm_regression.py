# ==================================================
# SECTION 1: LIBRARIES IMPORT
# ==================================================
from sklearn.svm import SVR
import numpy as np
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# ==================================================
# SECTION 2: DATA LOADING
# ==================================================
df = pd.read_csv("C:/Users/ASUS/Documents/(())/Semester 7/Despro 2/pH Detection Using Smartphone/Final/dataset/dataset.csv") #Dataset Directory

# ==================================================
# SECTION 3: DATA PREPROCESSING
# ==================================================
# Separating Features from Target Variables
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Splitting Training and Testing Set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Construct SVR Model
svr = SVR(kernel='poly', degree=5)

# Model Training
svr.fit(X_train, y_train)

# ==================================================
# SECTION 4: PREDICTION AND EVALUATION
# ==================================================
# Prediction Making on Testing Set
y_pred = svr.predict(X_test)

# Calculation of Evaluation Indicators
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print Calculation Result
print('Mean Squared Error: ', mse)
print('Mean Absolute Error: ', mae)
print('Coefficient of Determination Score: ', r2)

# Comparison Graph Plotting
fig, ax = plt.subplots()
ax.scatter(y_pred, y_test, s=10)
ax.plot([0,10.0], [0,10.0], '--', color='gray', label='Perfect Calibration')
ax.set_xlabel('Predicted Value')
ax.set_ylabel('Observed Value')
ax.legend(loc='lower right')
plt.title('test')
plt.rcParams['savefig.dpi'] = 300 #Saved Image Quality
plt.rcParams['figure.dpi'] = 300 #Displayed Image Resolution
plt.show()
plt.savefig('plot1.png', dpi=300)

# ==================================================
# SECTION 5: LOAD USING PICKLE
# ==================================================
import pickle
with open('model.pkl','wb') as f:
    pickle.dump(svr,f)