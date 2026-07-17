"""Qt font picker widgets."""

__all__ = ["FontDialog", "FontWidget"]

def __getattr__(name: str):
    if name == "FontDialog":
        from qtpy_font_widgets.font_dialog import FontDialog
        return FontDialog
    if name == "FontWidget":
        from qtpy_font_widgets.font_widget import FontWidget
        return FontWidget
    raise AttributeError(name)
