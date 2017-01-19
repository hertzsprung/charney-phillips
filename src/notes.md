# Misc notes...
## who uses unusual meshes?

* conforming AMR in the vertical would create off-vertical faces
* non-conforming AMR would create degenerate pentagons that look like rectangles

* unstructured (triangular) meshes ([Smolarkiewicz and Szmelter 2011](https://doi.org/10.2478/s11600-011-0043-z))
* locally-refined block-structured meshes ([Yamazaki and Satomura 2012](https://doi.org/10.1002/asl.358), [Hubbard and Nikiforakis 2003](https://doi.org/10.1175//2568.1)?)
* other AMR, all advection/shallow-water: behrens1996,1998 and giraldo2000 on triangular grids, see hubbard-nikiforakis2003
* more AMR: jablonowski2009 does 3D hydrostatic dynamics with floating Lagrangian layers
* grid nesting?
* skamarock1989, skamarock-klemp1993
* OMEGA, adaptive non-hydrostatic LAM, unstructured triangular prisms, bacon2000, boybeyi2001, haven't checked if they do refinement/coarsening in the vertical but I think no
* stcyr-2008

* some literature that uses conforming refinement:
  - walko-avissar2011 10.1175/MWR-D-11-00021.1 triangles
  - skamarock2012 10.1175/MWR-D-11-00215.1 hexagons
  - zarzycki2015 10.1175/JCLI-D-14-00599.1 quads (cubed-sphere)
  - muller2013 10.1016/j.jcp.2012.10.038 triangles (but arranged in quads)
* pros/cons of conforming/nonconforming:
  - jablonowski2009 says nonconforming block-refinement can be more computationally efficient
  * TODO: more ...
* TODO: is there any literature that deals with the treatment of orography with horizontal mesh refinement?

* does anyone do AMR in the vertical?
  * yamazaki-satomura2012 do
  * hubbard-nikiforakis2003 do, but for advection-only tests
  * muller2013 do


## more general texts

* [Block-structured Adaptive Mesh Refinement -- Theory, Implementation and Application](https://doi.org/10.1051/proc/201134002)

Almost all atmospheric models treat horizontal and vertical dimensions separately, leading to separate choices of horizontal and vertical staggerings.  In the horizontal, the Arakawa C-grid is commonly used because inertio-gravity waves have accurate dispersion properties [Arakawa and Lamb 1977](https://books.google.co.uk/books?id=nN_4561KTIIC&lpg=PA173&ots=yKV39fe7eu&dq=Computational%20design%20of%20the%20basic%20dynamical%20processes%20of%20the%20UCLA%20general%20circulation%20model&lr&pg=PA173#v=onepage&q&f=false).

