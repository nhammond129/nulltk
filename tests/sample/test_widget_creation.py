from tkinter.constants import W
import nulltk as tk

def test_widget(widget: tk.Widget):
	try:
		root = tk.Tk()
	except tk.TclError as e:
		print(e.__cause__)
	widget(root).pack()
	root.quit()