# Mach-Learn-Mat-Sci
**Predict materials band gap with machine learning algorithm**

New materials band gaps are usually calculated using Density Functional Theory (DFT). However, DFT often underestimate the values of band gaps. To overcome this problem, assuming a number of materials with the right band gaps are known, machine learning can be used to predict the band gaps of new materials, and expedite the discovery of new materials with useful applications.</br>

This code bandgap.py written in Python shows that ternary materials' band gap can be predicted using just atomic mass as the only feature.</br>
Training data = 10,000 materials band gaps</br>
Cross-validation (CV) = 3,000 materials band gaps</br>
Feature = atomic mass in each compounds</br>
Algorithm = random forest regression</br>

**Results:**</br>
Training score = 0.926188737522</br>
Prediction score (CV) = 0.728193397287</br>
Mean avarage error = 0.43978489978958324 eV </br>
Mean square error = 0.800555474512 eV</br>

**Plot:**</br>
![](https://github.com/wfgoh/mach-learn-mat-sci/blob/master/bandgap_predict.jpg)
