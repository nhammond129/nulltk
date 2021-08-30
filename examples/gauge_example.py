import nulltk as tk

def main():
	root = tk.Tk()

	def test(meter):
		meter.step()
		meter.after(10, test, meter)

	gauge = tk.RadialGauge(root, unitstext='units', labeltext='label text', stripethickness=4)
	gauge.pack(fill=tk.BOTH, expand=True)

	test(gauge)

	root.mainloop()

if __name__ == "__main__": main()
