import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import GeoIP

def readFile(fileName):
        fileName = fileName
	ipList=[]
	print "reading file"
	ipFile = open(fileName,'r')
	for line in ipFile:
		ipList.append(line.strip())
	print "Total number of IPs",len(ipList)
	return ipList

	
def make_map(lat,lon):
	lons=lon
	lats=lat
	print("Generating map")
	#m = Basemap(projection='cyl', resolution='l',     you can specify the coordinates here of what you want to plot
         #       llcrnrlon=float(110), llcrnrlat=float(-8),
          #      urcrnrlon=float(155), urcrnrlat=float(-45))
	m = Basemap(projection='cyl', resolution='l')   #if you want the entire world map
	m.bluemarble()
	x, y = m(lons, lats)
	m.scatter(x, y, s=1, color='#ff0000', marker='o', alpha=1)
	print("Saving")
	plt.savefig('ipgeo.png', dpi=300, bbox_inches='tight')

def local_database_getip(databaseObj, ipList):
    lat = []
    lon = []
    for add in ipList:
        try:
            info = databaseObj.record_by_addr(add)
        except Exception:
            print (" IP address not found")
            continue
	if info is not None:
		print("%s {country_code} {latitude}, {longitude}".format(**info) % add)
		lat.append(info['latitude'])
		lon.append(info['longitude'])
    print "Total number of Lats",len(lat)
    return lat, lon

def main():
	fileName = '/home/arwin/Documents/Code/Python/IP/moodle_IPs.txt'   # this should link to the .csv file of stats_limited-KD-CT-no_dup tab
	ipList= readFile(fileName)
	databaseObj = GeoIP.open("/home/arwin/Documents/Code/Python/IP/GeoLiteCity.dat", GeoIP.GEOIP_STANDARD)
	lat, lon = local_database_getip(databaseObj,ipList)
	make_map(lat,lon)

main()
	

