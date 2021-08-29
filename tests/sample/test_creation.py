from tkinter.constants import W
import nulltk as tk

def test_widget(widget: tk.Widget):
	root = tk.Tk()
	widget(root).pack()
	root.quit()

if __name__ == "__main__":
	test_widgets()