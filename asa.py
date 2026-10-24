
import pandas as pd

path = "/Users/tugcecelik/Desktop/ASA/WPP2024_Demographic_Indicators_Medium_csv (1)"

medium = pd.read_csv(
    path,
    encoding="utf-8-sig",
    low_memory=False
)

print(medium.head(10))
print("Veri boyutu:", medium.shape)


# Sütun isimlerini göster
print(medium.columns.tolist())

# Her sütundaki eksik değer sayısı
print(medium.isna().sum())

# Veri tiplerini göster
print(medium.dtypes)