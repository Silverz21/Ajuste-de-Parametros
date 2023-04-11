# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 18:39:20 2023

@author: Lenovo
"""

import pandas as pd
import datetime

paste = pd.read_csv('Puebla_pos.csv')

Casos = pd.DataFrame(paste)

Casos.FECHA_SINTOMAS = pd.to_datetime(Casos.FECHA_SINTOMAS)

Casos = Casos.set_index("FECHA_SINTOMAS")

Casos["positivo"].resample("W").sum().plot()
