import nulltk as tk
import nulltk.colors as colors

def main():
	root = tk.Tk()

	# arbitrary color
	root.option_add('*foreground', colors.Chartreuse.as_hex())

	def test(meter):
		meter.step()
		meter.after(20, test, meter)

	gauge = tk.RadialGauge(root,
			unitstext='units', labeltext='label text',
			stripethickness=2,
			amounttotal=60,
			arcoffset=-90,
			arcrange=360
		)
	gauge.pack(fill=tk.BOTH, expand=True)

	test(gauge)

	root.mainloop()

if __name__ == "__main__": main()
