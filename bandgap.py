import pandas as pd
from sklearn.utils import shuffle
from pymatgen import Composition
from sklearn.ensemble import RandomForestRegressor
from numpy import mean, var, sqrt
from matplotlib import pyplot as plt
import numpy as np

trainte = pd.read_csv('bandgapternary.csv')
trainte = shuffle(trainte)

composition = []
mass_sum = []
mass = []

def addfeature(train):
    for mat in train['material']:
        composition.append(Composition(mat))
        element_mass = []
        for num, element in enumerate(Composition(mat)):
            element_mass.append(element.atomic_mass)
        mass_sum.append(sum(element_mass))
        mass.append(element_mass)
        
    train['composition'] = composition
    train['mass_sum'] = mass_sum
    if num >= 0:
        train['mass1'] = np.array(mass)[:,0]
    if num >= 1:
        train['mass2'] = np.array(mass)[:,1]
    if num >= 2:
        train['mass3'] = np.array(mass)[:,2]
    return train

train = addfeature(trainte)
train1 = train.iloc[:10000, :]
train2 = train.iloc[10000:, :]

x_train = train1.drop(['material','composition','bandgap'],axis=1)
y_train = train1['bandgap']
x_test = train2.drop(['material','composition','bandgap'],axis=1)
y_test = train2['bandgap']

random_forest = RandomForestRegressor(n_estimators=100)
random_forest.fit(x_train, y_train)
print('Training score =',random_forest.score(x_train, y_train))
predict = random_forest.predict(x_test)
print('Prediction score =',random_forest.score(x_test,y_test))
mae = mean(abs(predict - y_test))
mse = sqrt(var(predict - y_test))
print('MAE =',mae,'eV','MSE =',mse,'eV')
plt.plot(y_test, predict, 'bo', [0,9],[0,9],'c--')
plt.ylabel('Predicted band gap (eV)')
plt.xlabel('Actual band gap (eV)')
plt.savefig('bandgap_predict.jpg',bbox_inches='tight')
plt.show()
