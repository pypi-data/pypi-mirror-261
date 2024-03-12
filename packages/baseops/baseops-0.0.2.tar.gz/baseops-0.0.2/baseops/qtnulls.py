#!/bin/bash

import pandas as pd
from tqdm import tqdm


def count_nulls(x):

    with tqdm(total=len(x.columns), desc="Quantify nulls") as pbar:   
        countnulls = round(x.isnull().sum(), 2)
        countnulls = pd.DataFrame(countnulls).reset_index().\
            rename(columns={'index': 'features_names', 0: 'qt_nulls'}
                   ).sort_values(by=['qt_nulls'], ascending=False)
        
        pbar.update(1)  # Atualize a barra de progresso

    return countnulls