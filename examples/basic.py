import nulltk as tk

def main():
    root = tk.Tk()

    tabbed = tk.TabbedFrame(root, tabs=("Tab one", "Tab two", "Tab three"))
    tabbed.pack()

    tk.Label(tabbed.tab_frame(0), text="This is the contents of tab one.").pack()
    tk.Label(tabbed.tab_frame(1), text="This is the contents of tab two.").pack()
    tk.Label(tabbed.tab_frame(2), text="This is the contents of tab three.").pack()

    root.mainloop()

if __name__ == "__main__": main()