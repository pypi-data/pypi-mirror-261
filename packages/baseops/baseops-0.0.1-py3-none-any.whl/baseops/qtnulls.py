#!/bin/bash

import pandas as pd
from tqdm import tqdm

#from keyring.backends.Windows import WinVaultKeyring

#keyring.set_keyring(WinVaultKeyring())

def count_nulls(x):
    
    # Crie uma barra de progresso para acompanhar o processamento
    
    with tqdm(total=len(x.columns), desc="Quantify nulls") as pbar:
        
        countnulls = round(x.isnull().sum(), 2)
        countnulls = pd.DataFrame(countnulls).reset_index().\
            rename(columns={'index': 'features_names', 0: 'qt_nulls'}
                   ).sort_values(by=['qt_nulls'], ascending=False)
        
        pbar.update(1)  # Atualize a barra de progresso

    return countnulls