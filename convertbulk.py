# convert the photo file to thumbs in bulk
import os
indir = "/www/built/besite/media/photo/"
outdir = "/www/built/besite/media/thumbs/photo/"
for root, dirs, filenames in os.walk(indir):
	for f in filenames:
		if f[-4:] == ".jpg" or f[-4:] == ".JPG":
			shellCom = "convert " + indir + f + " -resize 40\% " + outdir + f
			os.system(shellCom)
		# end if
	# next f
# next root

