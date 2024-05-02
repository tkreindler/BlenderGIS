from os import path
import sys
import subprocess
import logging
log = logging.getLogger(__name__)

#GDAL
try:
	from osgeo import gdal
except:
	HAS_GDAL = False
	log.debug('GDAL Python binding unavailable')
else:
	HAS_GDAL = True
	log.debug('GDAL Python binding available')


#PyProj
try:
	import pyproj
except:
	HAS_PYPROJ = False
	log.debug('PyProj unavailable')
else:
	HAS_PYPROJ = True
	log.debug('PyProj available')


#PIL/Pillow
try:
	from PIL import Image
except:
	HAS_PIL = False
	log.debug('Pillow unavailable')
else:
	HAS_PIL = True
	log.debug('Pillow available')


#Imageio

try:
	python = path.abspath(sys.executable)
	log.info("Installing 'imageio' package.")
	# Verify 'pip' package manager is installed.
	try:
		subprocess.call([python, "-m", "ensurepip"])
	except Exception as e:
		log.error("Failed to verify 'pip' package manager installation.")
		raise e

	# Install 'imageio' package.
	try:
		subprocess.call([python, "-m", "pip", "install", "imageio"])
	except Exception:
		log.error("Failed to install 'imageio' package.")

except Exception as e:
	log.error("Cannot install ImageIO", exc_info=True)
	HAS_IMGIO = False
else:
	HAS_IMGIO = True
	log.debug('ImageIO plugin available')
