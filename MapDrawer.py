from geopy import distance
import folium
import DataLoading


class MapDrawer:

    def __init__(self, cor, dis):
        self.cor = cor
        self.dis = dis

    def draw(self):
        dataloading = DataLoading.DataLoading()
        lists = dataloading.LoadTSVFilesDataIntoString()
        docIncluded = []
        for rec in lists:
            rec = rec.split("\t")
            if (rec[6] == "NA" or rec[7] == "NA"):
                continue
            docCor = (float(rec[6]), float(rec[7]))
            if (distance.distance(self.cor, docCor).km <= self.dis):
                docIncluded.append([float(rec[6]), float(rec[7]), rec[8], rec[9]])
        m = folium.Map(location=self.cor)
        folium.Circle(
            location=self.cor,
            radius=self.dis * 1000,
            color='#3186cc',
            fill=True,
            fill_color='#3186cc'
        ).add_to(m)
        folium.Marker(
            location=self.cor,
            tooltip='You are here!',
            icon=folium.Icon(color='green')
        ).add_to(m)
        for rec in docIncluded:
            folium.Marker(
                location=[rec[0], rec[1]],
                tooltip=rec[2],
                popup=rec[3],
                icon=folium.Icon(color='blue')
            ).add_to(m)
        m.save('map.html')
