#!/usr/local/bin/python3

from data.read_data import read_data,get_plot_data,get_train_data
data = read_data()
plot_data = get_plot_data()
train_data = get_train_data()

x = list(map(lambda z: [z[0]], data))
y = list(map(lambda z: [z[1]], data))

from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit(x,y)

from data.plot_function import plot,show
predict_result = reg.predict(x)
plot_x = list(map(lambda z: [z],plot_data))
plot_predict_function = reg.predict(plot_x)

plot(x,y,'ro')
#plot(x,predict_result,'bo')
plot(plot_x,plot_predict_function,'b')
show()

