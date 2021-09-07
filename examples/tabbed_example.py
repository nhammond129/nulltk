import nulltk as tk

def main():
    root = tk.Tk()

    tabbed_main = tk.TabbedFrame(root, tabs=("Static tabs", "Dynamic tabs"))
    tabbed_main.pack(fill=tk.BOTH, expand=True)

    tabbed_sub1 = tk.TabbedFrame(tabbed_main.tab_frames()[0], tabs=("one", "two"))
    tabbed_sub1.pack(fill=tk.BOTH, expand=True)

    tabbed_sub2 = tk.TabbedFrame(tabbed_main.tab_frames()[1], tabs=("one", "two"), allow_tab_creation=True)
    tabbed_sub2.pack(fill=tk.BOTH, expand=True)

    tk.Label(tabbed_sub1.tab_frames()[0], text="Contents of tab one.", padx=40, pady=40).pack(fill=tk.BOTH, expand=True)
    tk.Label(tabbed_sub1.tab_frames()[1], text="Contents of tab two.", padx=40, pady=40).pack(fill=tk.BOTH, expand=True)

    tk.Label(tabbed_sub2.tab_frames()[0], text="Contents of tab one.", padx=40, pady=40).pack(fill=tk.BOTH, expand=True)
    tk.Label(tabbed_sub2.tab_frames()[1], text="Contents of tab two.", padx=40, pady=40).pack(fill=tk.BOTH, expand=True)

    root.mainloop()

if __name__ == "__main__": main()
