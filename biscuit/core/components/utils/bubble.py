import tkinter as tk

from .toplevel import Toplevel
from .label import Label


class Bubble(Toplevel):
    """
     +===============+
    ||      Text     ||
     +===============+
    """
    def __init__(self, master, text, bd=1, *args, **kw):
        super().__init__(master, *args, **kw)
        self.overrideredirect(True)
        self.config(bg=self.base.theme.border)
        Label(self, text=text, padx=5, pady=5, **self.base.theme.utils.bubble).pack(padx=bd, pady=bd)
        self.withdraw()

    def show(self, *_):
        self.update_idletasks()
        self.geometry(f"+{self.master.winfo_rootx() + self.master.winfo_width() + 5}" +
                             f"+{int(self.master.winfo_rooty() + (self.master.winfo_height() - self.winfo_height())/2)}")
        self.deiconify()
    
    def hide(self, *_):
        self.withdraw()
