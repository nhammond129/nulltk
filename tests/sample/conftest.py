import nulltk as tk
def pytest_generate_tests(metafunc):
    if "widget" in metafunc.fixturenames:
        BLACKLIST = (tk.Menu, tk.OptionMenu, tk.Widget)
        widgets = []
        for attr in [getattr(tk, attr) for attr in dir(tk)]:
            if isinstance(attr, type) and issubclass(attr, tk.Widget):
                if attr in BLACKLIST: continue
                widgets.append(attr)
        metafunc.parametrize("widget", widgets)