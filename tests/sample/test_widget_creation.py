from tkinter.constants import W
import nulltk as tk

def test_widget(widget: tk.Widget):
	try:
		root = tk.Tk()
		widget(root).pack()
		root.quit()
	except tk.TclError:
		print("Github Actions throws an error of 'no display'. Ignoring.")