import numpy as np
import pandas as pd
from pathlib import Path

vix_path = Path("../Data/vix_daily.csv")
data = pd.read_csv(vix_path)


