from tkinter.constants import W
import nulltk as tk
from typing import Callable

def test_widget(widget: Callable):
	try:
		root = tk.Tk()
		widget(root).pack()
		root.quit()
	except tk.TclError:
		print("Github Actions throws an error of 'no display'. Ignoring.")
