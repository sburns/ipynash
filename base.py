def style_nb():
    from IPython.core.display import HTML
    styles = open("css/slides.css", "r").read()
    return HTML(styles)