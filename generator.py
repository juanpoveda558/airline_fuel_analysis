import pandas as pd
import numpy as np

data = {
    'Fecha': ['2023-01-01', '2023-02-01', '2023-03-01', '04/2023/01', '2023-05-01', None],
    'Precio_Barril': [85.5, 90.2, None, 88.7, 92.0, 95.1],
    'Aerolinea': ['Avianca', 'LATAM', 'Avianca', 'Copa', 'LATAM', 'Avianca']
}

df = pd.DataFrame(data)
df.to_csv('fuel_data_raw.csv', index=False)
print("¡Dataset 'sucio' creado exitosamente como fuel_data_raw.csv!")