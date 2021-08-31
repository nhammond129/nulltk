import nulltk as tk
import nulltk.colors as colors
import random

def main():
	root = tk.Tk()

	# arbitrary color
	root.option_add('*foreground', colors.Chartreuse.as_hex())

	def test(meter):
		meter.step()
		meter.after(20, test, meter)

	def make_gauge(root, **kwargs):
		gauge = tk.RadialGauge(root,
				unitstext='units', labeltext='label text',
				stripethickness=2,
				**kwargs
			)
		gauge.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
		return gauge

	for i in range(1):
		g=make_gauge(root)
		g.amountused = random.randint(1,100)
		test(g)

	root.mainloop()

if __name__ == "__main__": main()
