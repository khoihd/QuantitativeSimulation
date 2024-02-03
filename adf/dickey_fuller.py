import numpy as np
from statsmodels.tsa.stattools import adfuller
from statsmodels.regression.linear_model import OLS
import pandas as pd

def dickey_fuller():
    normal_series = np.random.normal(size=1000)
    normal_series_df = pd.DataFrame(normal_series, columns=['data'])
    normal_series_df['prev'] = normal_series_df.data.shift()
    normal_series_df.dropna(inplace=True)
    normal_series_df['delta'] = normal_series_df.data - normal_series_df.prev

    # delta_y_t = phi * y_{t-1} + epsilon_t
    model = OLS(normal_series_df.delta, normal_series_df.prev)
    ols_result = model.fit()
    print('OLS SE', ols_result.bse)

    est_coeff = ols_result.params[0]
    sd_coeff = ols_result.bse[0]

    test_stat = est_coeff / sd_coeff
    print('test_stat t values', ols_result.tvalues[0])
    print('test_stat', test_stat)

    adf_result = adfuller(normal_series, maxlag=1)
    print('adf_result', adf_result)


if __name__ == "__main__":
    dickey_fuller()
