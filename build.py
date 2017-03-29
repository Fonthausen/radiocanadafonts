from fontmake.font_project import FontProject
import os

SRC_DIR = "src"


ufos = [
	os.path.join(SRC_DIR, "RC-Light.ufo"),
	os.path.join(SRC_DIR, "RC-Regular.ufo"),
	os.path.join(SRC_DIR, "RC-Bold.ufo"),
]

project = FontProject()

project.run_from_ufos(ufos, 
	output=("otf", "ttf", "ttf-interpolatable"), 
	designspace_path=None, 
	mti_source=None, 
	remove_overlaps=True, 
	reverse_direction=True, # only used for ttf and ttf-interpolatable
	conversion_error=None)
