import pandas as pd
from sklearn.utils import shuffle
from pymatgen import Composition
from sklearn.ensemble import RandomForestRegressor
from numpy import mean, var, sqrt
from matplotlib import pyplot as plt

train = pd.read_csv('bandgaps.csv')
train = shuffle(train)

composition = []
mass_sum = []
mass1 = []
mass2 = []
mass3 = []

for mat in train['material']:
    composition.append(Composition(mat))
    element_mass = []
    element_group = []
    element_eneg = []
    for element in Composition(mat):
        element_mass.append(element.atomic_mass)
    mass_sum.append(element_mass[0]+element_mass[1]+element_mass[2])
    mass1.append(element_mass[0])
    mass2.append(element_mass[1])
    mass3.append(element_mass[2])
    
train['composition'] = composition
train['mass_sum'] = mass_sum
train['mass1'] = mass1
train['mass2'] = mass2
train['mass3'] = mass3

train1 = train.iloc[:10000, :]
train2 = train.iloc[10000:, :]

x_train = train1.drop(['material','composition','bandgap','mass_sum'],axis=1)
y_train = train1['bandgap']
x_test = train2.drop(['material','composition','bandgap','mass_sum'],axis=1)
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
