# A proposal for a generalised Charney--Phillips-like staggering of variables for arbitrarily-structured meshes

The Charney--Phillips vertical staggering of variables ([Charney and Phillips 1953](https://doi.org/10.1175/1520-0469(1953)010<0071:NIOTQG>2.0.CO;2)) is suitable for structured meshes with cells stacked in columns.
This staggering has been adopted by several operational models ([Davies et al. 2005](https://doi.org/10.1256/qj.04.101), [Girard et al. 2014](https://doi.org/10.1175/MWR-D-13-00255.1)) because it avoids the computational mode that is associated with the Lorenz vertical staggering ([Arakawa and Konor 1996](https://doi.org/10.1175/1520-0493(1996)124<0511:VDOTPE>2.0.CO;2)).
The generalisation of the Lorenz staggering for unstructured or arbitrarily-structured meshes is straightforward ([Weller and Shahrokhi 2014](https://doi.org/10.1175/MWR-D-14-00054.1)) but this is not true for the Charney--Phillips staggering.

On a finite volume mesh, variables are ordinarily placed at cell centres or cell faces.  In the Charney--Phillips staggering, the thermodynamic variable is placed at only those cell faces that lie on the vertical coordinate surfaces, and vertically-oriented faces have no thermodynamic information.  This existing staggering is unsuitable for arbitrarily-structured finite volume meshes because faces can have any orientation.

## Mesh refinement

Mesh refinement has received growing attention in atmospheric modelling literature because it could enable atmospheric models to produce more accurate forecasts with less computation.
While much of this literature concentrates on horizontal refinement, some investigations have been made into vertical refinement on two-dimensional `x`–`z` planes: [Müller et al. 2013](https://doi.org/10.1016/j.jcp.2012.10.038) have used conforming refinement of triangular meshes for simulating the standard rising bubble and density current test cases, and [Yamazaki & Satomura 2012](https://doi.org/10.1002/asl.358) have used block-refinement to better resolve idealised mountains.

TODO: talk about tf coords and how they naturally allow high res near the ground.  then talk about alternatives (cut-cells, slanted-cells) and how mesh refinement could be a route for achieving high res near the ground for such meshes.


We propose to develop a generalised Charney--Phillips staggering for arbitrarily-structured meshes which means that
  * we investigate issues of vertical refinement and vertical staggerings that have not previously been explored
  * using arbitrarily-structured meshes allows us to support both conforming and nonconforming approaches
  * it also allows us to model terrain using terrain-following, cut-cell or slanted-cell methods


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

<!---
Almost all atmospheric models treat horizontal and vertical dimensions separately, leading to separate choices of horizontal and vertical staggerings.  In the horizontal, the Arakawa C-grid is commonly used because inertio-gravity waves have accurate dispersion properties [Arakawa and Lamb 1977](https://books.google.co.uk/books?id=nN_4561KTIIC&lpg=PA173&ots=yKV39fe7eu&dq=Computational%20design%20of%20the%20basic%20dynamical%20processes%20of%20the%20UCLA%20general%20circulation%20model&lr&pg=PA173#v=onepage&q&f=false).
-->
