from matplotlib import rcParams

rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
import matplotlib

matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True
import io.BytesIO
import matplotlib.pyplot as plt


def renderlatex(formula, fontsize=18, dpi=300, format_='png'):
    """Renders LaTeX formula into image.
    """
    fig = plt.figure(figsize=(0.01, 0.01))
    fig.text(0, 0, u'${}$'.format(formula), fontsize=fontsize)
    buffer_ = io.BytesIO()
    fig.savefig(buffer_, dpi=dpi, transparent=True, format=format_, bbox_inches='tight', pad_inches=0.0)
    return buffer_.getvalue()
