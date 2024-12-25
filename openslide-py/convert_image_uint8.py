# HISTOQC
# Performed better when I uncommented that junk in the dockerfile

2020-01-29 15:40:09,262 - INFO - These images failed (available also in error.log), warnings are listed in warnings column in output:
2020-01-29 15:40:09,262 - INFO - /opt/HistoQC/sample.svs	<class 'ZeroDivisionError'> Second argument to a division or modulo operation was zero. ('division by zero', '/opt/HistoQC/sample.svs', '<code object finalProcessingSpur at 0x7fc67ea8ca50, file "/opt/HistoQC/BasicModule.py", line 28>')
2020-01-29 15:40:08,582 - WARNING - Lossy conversion from int64 to uint8. Range [0, 255]. Convert image to uint8 prior to saving to suppress this warning.
2020-01-29 15:40:09,202 - ERROR - /opt/HistoQC/sample.svs - 	 - Error analyzing file (skipping): 	 <class 'ZeroDivisionError'> Second argument to a division or modulo operation was zero. ('division by zero', '/opt/HistoQC/sample.svs', '<code object finalProcessingSpur at 0x7fc67ea8ca50, file "/opt/HistoQC/BasicModule.py", line 28>')

# Attempt conversion, as recommended

> python3.6
>>> from skimage import img_as_ubyte
>>> save_path="/opt/HistoQC/sample1.png"
#>>> save_path="/opt/HistoQC/sample1.tiff"
>>> from skimage import io
>>> import os
>>> from skimage.io import imread
>>> img = imread("/opt/HistoQC/sample.svs")
# >>> io.imsave(os.path.join(save_path),img_as_ubyte(img))
>>> io.imsave(save_path,img_as_ubyte(img))


# If you try to convert to svs, it freaks out. So then => PNG.
# But then you get:
2020-01-29 16:00:48,061 - INFO - -----Working on:	/opt/HistoQC/sample1.png		1 of 1
2020-01-29 16:00:48,063 - ERROR - /opt/HistoQC/sample1.png - 	 - Error analyzing file (skipping): 	 <class 'openslide.lowlevel.OpenSlideUnsupportedFormatError'> OpenSlide does not support the requested file.      Import this from openslide rather than from openslide.lowlevel.      ('Unsupported or missing image file', '/opt/HistoQC/sample1.png', '<code object __init__ at 0x7f13f1825a50, file "/opt/HistoQC/BaseImage.py", line 44>')
2020-01-29 16:00:48,165 - INFO - ------------Done---------

2020-01-29 16:00:48,165 - INFO - These images failed (available also in error.log), warnings are listed in warnings column in output:
2020-01-29 16:00:48,165 - INFO - /opt/HistoQC/sample1.png	<class 'openslide.lowlevel.OpenSlideUnsupportedFormatError'> OpenSlide does not support the requested file.      Import this from openslide rather than from openslide.lowlevel.      ('Unsupported or missing image file', '/opt/HistoQC/sample1.png', '<code object __init__ at 0x7f13f1825a50, file "/opt/HistoQC/BaseImage.py", line 44>')

# 'Unsupported or missing image file'.  Okay, try TIFF.
# TIFF also errored:
2020-01-29 16:04:14,237 - ERROR - /opt/HistoQC/sample1.tiff - 	 - Error analyzing file (skipping): 	 <class 'openslide.lowlevel.OpenSlideUnsupportedFormatError'> OpenSlide does not support the requested file.      Import this from openslide rather than from openslide.lowlevel.      ('Unsupported or missing image file', '/opt/HistoQC/sample1.tiff', '<code object __init__ at 0x7f1dac217a50, file "/opt/HistoQC/BaseImage.py", line 44>')
2020-01-29 16:04:14,341 - INFO - ------------Done---------

2020-01-29 16:04:14,341 - INFO - These images failed (available also in error.log), warnings are listed in warnings column in output:
2020-01-29 16:04:14,341 - INFO - /opt/HistoQC/sample1.tiff	<class 'openslide.lowlevel.OpenSlideUnsupportedFormatError'> OpenSlide does not support the requested file.      Import this from openslide rather than from openslide.lowlevel.      ('Unsupported or missing image file', '/opt/HistoQC/sample1.tiff', '<code object __init__ at 0x7f1dac217a50, file "/opt/HistoQC/BaseImage.py", line 44>')
2020-01-29 16:04:14,342 - INFO - Symlink to output directory created

# HEH?  save as layered image failed, then?
