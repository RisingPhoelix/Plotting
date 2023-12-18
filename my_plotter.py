'''Module for defining a consistant plotting scheme.'''
import matplotlib.pyplot as plt

def prepare_plt(plt):
    # DEFINING STYLES
    plt.style.use('seaborn-v0_8')

    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "serif",
        "font.serif": ["Palatino"],

        "axes.facecolor":"white",
        "grid.color":"#dddddd",

        "axes.spines.bottom":True,
        "axes.spines.left":True,
        "axes.spines.right":True,
        "axes.spines.top":True,

        "svg.fonttype":"path",
        "pdf.fonttype":"truetype",
    })

def format_ax(ax: plt.Axes) -> plt.Axes:
    ax.patch.set_edgecolor('#aaaaaa')
    ax.patch.set_linewidth(0.5)
    return ax

def finalize_figure(fig):
    for ax in fig.Axes:
        format_ax(ax)

def export_fig(fig, name, dpi=300):
    fig.tight_layout()
    fig.savefig(f'{name}.png', dpi=dpi)
    fig.savefig(f'{name}.pdf')
    fig.savefig(f'{name}.svg')
