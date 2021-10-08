import PIL
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans2


# Exports
__all__ = [
    'extract_nodes',
    'solve_tsp',
    'draw_nodes',
    'draw_tour'
]


def extract_nodes(image_path, n=None):

    # Open image and convert it to black and white
    image = PIL.Image.open(image_path)
    bw_image = image.convert('1', dither=PIL.Image.NONE)
    gs_image = image.convert('1', dither=PIL.Image.FLOYDSTEINBERG)

    # Get set of black pixels
    bw_pixels = np.array(bw_image, dtype=np.int)
    gs_pixels = np.array(gs_image, dtype=np.int)
    nodes = [(np.float(v[1]), np.float(v[0])) for v in np.argwhere(bw_pixels + gs_pixels == 0)]

    # Define n nodes with k-means algorithm (with k = n)
    n = len(nodes) if n is None else n
    n = min(n, len(nodes))

    centroid, label = kmeans2(nodes, n, minit='points')
    chosen_nodes = [(float(v[0]), float(v[1])) for v in centroid]

    return chosen_nodes


def solve_tsp(nodes, solver='lkh'):

    # Lin-Kernighan
    if solver == 'lkh':
        from .solver.linkernighan import linkernighan
        return linkernighan(nodes)

    # Greedy
    if solver == 'greedy':
        pass


def draw_nodes(filename, nodes, width=None, height=None, dpi=300):

    # Coordinates
    x = [v[0] for v in nodes]
    y = [v[1] for v in nodes]

    # Calculate width and height for the figure
    w = width if width is not None else max(x)
    h = height if height is not None else max(y)

    width = int((w / min(w, h)) * 20)
    height = int((h / min(w, h)) * 20)

    # Draw figure
    plt.figure(figsize=(width, height), dpi=dpi)
    plt.plot(x, y, linestyle='', marker='o', markerfacecolor='black', markeredgewidth=0, markersize=2)
    plt.xlim(-5, max(x) + 5)
    plt.ylim(-5, max(y) + 5)
    plt.gca().invert_yaxis()
    plt.xticks([])
    plt.yticks([])
    plt.box(False)
    plt.savefig(filename)


def draw_tour(filename, tour, nodes, width=None, height=None, dpi=300):

    # Coordinates
    x = [nodes[i][0] for i in tour] + [nodes[tour[0]][0]]
    y = [nodes[i][1] for i in tour] + [nodes[tour[0]][1]]

    # Calculate width and height for the figure
    w = width if width is not None else max(x)
    h = height if height is not None else max(y)

    width = int((w / min(w, h)) * 20)
    height = int((h / min(w, h)) * 20)

    # Draw figure
    plt.figure(figsize=(width, height), dpi=dpi)
    plt.plot(x, y, linestyle='-', color='black', linewidth=1)
    plt.xlim(-5, max(x) + 5)
    plt.ylim(-5, max(y) + 5)
    plt.gca().invert_yaxis()
    plt.xticks([])
    plt.yticks([])
    plt.box(False)
    plt.savefig(filename)
