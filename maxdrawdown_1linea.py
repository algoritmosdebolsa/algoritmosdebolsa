import youtube_gdx
import numpy as np
data = youtube_gdx.data
equity = data['cumstrat']

### Max drawdown con numpy ###
maxdrawdown_np = max(1 - equity/np.maximum.accumulate(equity))

### Max drawdown con pandas ###
maxdrawdown_pd = max(1 - equity/equity.rolling(window=len(equity),min_periods=0).max())