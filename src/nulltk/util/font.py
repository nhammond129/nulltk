from PIL import ImageFont
import sys
import os

FONT_START_SIZE = 14

def get_filling_font(font: ImageFont.FreeTypeFont, text: str, area: tuple):
	width, height = area

	size = FONT_START_SIZE
	step_interval = size
	while step_interval > 1:
		(_, _, fw, fh) = font.getbbox(text)
		print(fw, fh, step_interval)
		if (fw > width) or (fh > height):
			step_interval = step_interval // 2
			size -= step_interval
		else:
			size += step_interval
		font = font.font_variant(size=size)
	(_, _, fw, fh) = font.getbbox(text)
	print(fw, fh)
	return font

# https://github.com/python-pillow/Pillow/blob/master/src/PIL/ImageFont.py#L861-L895
def find_system_fonts():
	dirs = []
	fonts = []
	if sys.platform == "win32":
		# check the windows font repository
		# NOTE: must use uppercase WINDIR, to work around bugs in
		# 1.5.2's os.environ.get()
		windir = os.environ.get("WINDIR")
		if windir:
			dirs.append(os.path.join(windir, "fonts"))
	elif sys.platform in ("linux", "linux2"):
		lindirs = os.environ.get("XDG_DATA_DIRS", "")
		if not lindirs:
			# According to the freedesktop spec, XDG_DATA_DIRS should
			# default to /usr/share
			lindirs = "/usr/share"
		dirs += [os.path.join(lindir, "fonts") for lindir in lindirs.split(":")]
	elif sys.platform == "darwin":
		dirs += [
			"/Library/Fonts",
			"/System/Library/Fonts",
			os.path.expanduser("~/Library/Fonts"),
		]

	for directory in dirs:
		for walkroot, walkdir, walkfilenames in os.walk(directory):
			for walkfilename in walkfilenames:
				if walkfilename.endswith(".ttf"):
					fonts.append(walkfilename)

	return fonts

def main():
	f = ImageFont.truetype('arialbd.ttf', FONT_START_SIZE)
	print(get_filling_font(f, "hi", (80,79)))

if __name__ == '__main__':
	main()
