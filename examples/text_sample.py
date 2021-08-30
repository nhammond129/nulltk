from typing import Text
import nulltk as tk

def main():
	root = tk.Tk()

	txt = tk.Text(root)
	txt.pack(fill=tk.BOTH, expand=True)

	root.mainloop()

if __name__ == "__main__": main()
