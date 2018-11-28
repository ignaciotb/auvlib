#!/usr/bin/python

import matplotlib.pyplot as plt
from pybathy_maps import draping_viewer
from numpy import sign
import numpy as np
from copy import deepcopy
import sys

patch_views = draping_viewer.sss_patch_views.read_data(sys.argv[1])
#patch_views.append(patch_views[0])

print "Number of patches :", len(patch_views)

world_size = 8.

max_patches = max(len(p.sss_views) for p in patch_views)

f, axarr = plt.subplots(len(patch_views), max_patches+1)

for i, p in enumerate(patch_views):

    axarr[i, 0].imshow(p.patch_height, cmap=plt.jet())
    print "Patch view dirs: ", p.patch_view_dirs

    for j, (im, pos, d) in enumerate(zip(p.sss_views, p.patch_view_pos, p.patch_view_dirs)):
        axarr[i, j+1].imshow(im, vmin=0., vmax=1., cmap=plt.gray())

        image_size = float(im.shape[0])
        impos = image_size/world_size*pos
        x, y = impos[0], impos[1]
        if abs(x) < .5*image_size and abs(y) < .5*image_size:
            pass
        elif abs(y) < abs(x):
            y = .5*image_size*y/abs(x)
            x = .5*image_size*sign(x)
        else:
            x = .5*image_size*x/abs(y)
            y = .5*image_size*sign(y)

        x = x + .5*image_size
        y = y + .5*image_size

        print impos
        print x, y
        print d

        axarr[i, j+1].set_title("Dist: %d" % int(np.linalg.norm(pos[:2])))
        axarr[i, j+1].scatter(x, y, s=20, c='white', marker='o')
        axarr[i, j+1].arrow(x, y, 10.*d[0], 10.*d[1], color='red', width=0.01, head_width=0.1)

    for j in range(len(p.sss_views), max_patches):
        axarr[i, j+1].axis('off')

plt.show()
