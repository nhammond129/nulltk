from tkinter.constants import W
import nulltk as tk

def test_widget(widget: tk.Widget):
	root = tk.Tk()
	try:
		w = widget(root)
		w.pack()
	except tk.TclError as e:
		print(e.__cause__)

	root.quit()