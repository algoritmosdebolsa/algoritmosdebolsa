import numpy as np
import pandas as pd

def Crosses(small: pd.Series, big: pd.Series) -> pd.Series:
    small_1 = small.shift(1).to_numpy()
    big_1 = big.shift(1).to_numpy()

    small = small.to_numpy()    
    big = big.to_numpy()
    
    # 'small' crosses over 'big'
    crossed_up = np.argwhere((np.sign((small - big) * \
                                (small_1 - big_1)) == -1) & \
                                (small > big)).flatten()
    
    # 'big' crosses over 'small'
    crossed_down = np.argwhere((np.sign((big - small) * \
                                (big_1 - small_1)) == -1) & \
                                (big > small)).flatten()
    
    length = len(small)
    crosses = pd.Series(length*[0])
    crosses[crossed_up] = 1
    crosses[crossed_down] = -1
    return crosses