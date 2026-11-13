# news-image-01 entry (Python 3.13, standard library only): the image is the
# entry.png beside this file, and the program copies it to /output/entry.png.
# The gate takes a whole PNG of at most 1 MiB and 1024 by 1024 pixels, and the
# judge sees exactly the bytes copied. Deterministic: the same bytes every run.
import os
import shutil

_SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
_DST = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")
os.makedirs(os.path.dirname(_DST), exist_ok=True)
shutil.copyfile(_SRC, _DST)
