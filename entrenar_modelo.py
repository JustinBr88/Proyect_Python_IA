import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Datos de ejemplo: puedes reemplazar por datos reales ampliados
data = [
    {"heart_rate": 45, "condition": "Bajo"},
    {"heart_rate": 58, "condition": "Bajo"},
    {"heart_rate": 65, "condition": "Normal"},
    {"heart_rate": 85, "condition": "Normal"},
    {"heart_rate": 110, "condition": "Alerta"},
    {"heart_rate": 120, "condition": "Alerta"},
    {"heart_rate": 142, "condition": "Crítico"},
    {"heart_rate": 25, "condition": "Crítico"},
]

df = pd.DataFrame(data)
X = df[["heart_rate"]]
y = df["condition"]

clf = RandomForestClassifier()
clf.fit(X, y)

# Guarda el modelo entrenado
joblib.dump(clf, "modelo_ia.pkl")
print("Modelo entrenado y guardado como modelo_ia.pkl")