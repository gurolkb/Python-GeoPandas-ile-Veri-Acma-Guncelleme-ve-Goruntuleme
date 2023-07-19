import geopandas as gpd
import matplotlib.pyplot as plt

# Dosyanin acilmasi
file_path = "provience.geojson"
gdf = gpd.read_file(file_path)

# Dosyanin gorsellestirilmesi
mapStandart = gdf.plot()
mapStandart.set_title("Rize Haritası")
plt.show()

# Ilcelerin 2022 nufus verilerine ait sozluk olusturulmasi
populationData = {
    "İKİZDERE": 6176,
    "İYİDERE": 8446,
    "ÇAMLIHEMŞİN": 6911,
    "ARDEŞEN": 42572,
    "ÇAYELİ": 42865,
    "DEREPAZARI": 6847,
    "FINDIKLI": 16448,
    "GÜNEYSU": 14952,
    "HEMŞİN": 2356,
    "KALKANDERE": 12903,
    "PAZAR": 31484,
    "RIZE": 152056
}

#nufus verisinin 'adm2_tr' sutunu kullanılarak ilce verisinde entegre edilmesi
gdf["population"] = gdf["adm2_tr"].map(populationData)

# Ilcelerin nufus miktarına gore renklendirilerek gorsellestirilmesi
mapPopulation = gdf.plot(column="population", cmap="viridis", linewidth=0.8, edgecolor="0.8", legend=True)
mapPopulation.set_title("Rize Nüfus Haritası")
plt.show()

# Ilcelere ait alan ve km^2 basina dusen kisi sayisinin hesaplanmasi
gdf = gdf.to_crs(epsg=32637) #Elimizdeki veri cografi koordinat sisteminde oldugu icin alan hesaplayabilmek icin UTM koordinat sistemine donus yapiyoruz
gdf["area"] = gdf.geometry.area / 10**6
gdf["density"] = gdf["population"] / gdf["area"]

# Olusturdugumuz nufus yogunluk verisin gorsellestirilmesi
mapDensity = gdf.plot(column="density", cmap="Spectral", linewidth=0.8, edgecolor="0.8", legend=True)
mapDensity.set_title("Rize Nüfus Yoğunluğu Haritası")
plt.show()

# Yeni ekledigimiz veriler ile birlikte dosyayi kaydediyoruz
gdf.to_file("updatedProvience.geojson", driver="GeoJSON")
