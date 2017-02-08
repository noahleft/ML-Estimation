#!/usr/local/bin/python3
from data.read_data import read_data,get_plot_data,get_train_data
data = read_data()
plot_data = get_plot_data()
train_data = get_train_data()

x = list(map(lambda z: [z[0]], data))
y = list(map(lambda z: [z[1]], data))

from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=5)
poly_X = poly.fit_transform(x)
reg = linear_model.Ridge(alpha = 0.001)
reg.fit(poly_X,y)

from data.plot_function import plot,show,setTitle
predict_result = reg.predict(poly_X)
plot_x = list(map(lambda z: [z],plot_data))
poly_plot_X = poly.fit_transform(plot_x)
plot_predict_function = reg.predict(poly_plot_X)
setTitle('5st order polynomial model')

plot(x,y,'ro','raw data')
#plot(x,predict_result,'bo')
plot(plot_x,plot_predict_function,'black','polynomial model prediction (5 orders)')
#show()


from data.config import x_min,x_max
from data.config import func
import numpy as np
t = np.arange(x_min,x_max,0.01)
s = list(map(func,t))
actual = plot(t,s,'b' ,'actual')


show()
