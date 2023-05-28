from statsmodels.tsa.ar_model import AutoReg, ar_select_order
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

data = [0.9, 1.3, 2.2, 3.3, 5.0, 7.8, 13.3, 20.7]
# sm.graphics.tsa.plot_pacf(data, lags=3)
# plt.show()

model = AutoReg(data, lags=3).fit()
para = model.params
print(para[0] + para[1]* 7.8 + para[2]* 13.3 + para[3]*20.7)
