from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


def mapTut():
    m = Basemap(projection='mill', llcrnrlat=20, urcrnrlat=50, \
                llcrnrlon=-130, urcrnrlon=-60, resolution='c')
    m.drawcoastlines()
    m.drawcountries()
    m.drawstates()
    m.fillcontinents(color='#04BAE3', lake_color='#FFFFFF')
    m.drawmapboundary(fill_color='#FFFFFF')

    # Houston, Texas

    lat, lon = 29.7630556, -95.3630556
    x, y = m(lon, lat)
    m.plot(x, y, 'ro')

    lon, lat = -104.237, 40.125  # Location of Boulder

    xpt, ypt = m(lon, lat)
    m.plot(xpt, ypt, 'go')

    plt.title("Geo Plotting")
    plt.show()
mapTut()
map = Basemap(projection='ortho',
              lat_0=0, lon_0=0)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()


x, y = map(2, 41)
x2, y2 = (-90, 10)

plt.annotate('Barcelona', xy=(x, y),  xycoords='data',
                xytext=(x2, y2), textcoords='offset points',
                color='r',
                arrowprops=dict(arrowstyle="fancy", color='g')
                )

x2, y2 = map(0, 0)
plt.annotate('Barcelona', xy=(x, y),  xycoords='data',
                xytext=(x2, y2), textcoords='data',
                arrowprops=dict(arrowstyle="->")
                )
plt.show()