import pandas as pd 

df = pd.DataFrame(
    {
        'TID' : ['T1','T2','T3','T4','T5','T6','T7','T8','T9'],
        'items' : ['I1, I2, I3','I2, I4','I2,I3','I1,I2,I4','I1,I3','I2,I3','I1,I3','I1,I2,I3,I5','I1,I2,I3']
    }
)

def get_dataset():
    return df
