from PIL import ImageFont

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



def main():
	f = ImageFont.truetype('arialbd.ttf', FONT_START_SIZE)
	
	print(get_filling_font(f, "hi", (80,79)))

if __name__ == '__main__':
	main()