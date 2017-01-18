# A proposal for a generalised Charney--Phillips-like staggering of variables for arbitrarily-structured meshes

The Charney--Phillips vertical staggering of variables ([Charney and Phillips 1953](https://doi.org/10.1175/1520-0469(1953)010<0071:NIOTQG>2.0.CO;2)) is suitable for structured meshes with cells stacked in columns.
This staggering has been adopted by several operational models ([Davies et al. 2005](https://doi.org/10.1256/qj.04.101), [Girard et al. 2014](https://doi.org/10.1175/MWR-D-13-00255.1)) because it avoids the computational mode that is associated with the Lorenz vertical staggering ([Arakawa and Konor 1996](https://doi.org/10.1175/1520-0493(1996)124<0511:VDOTPE>2.0.CO;2)).
The generalisation of the Lorenz staggering for unstructured or arbitrarily-structured meshes is straightforward ([Weller and Shahrokhi 2014](https://doi.org/10.1175/MWR-D-14-00054.1)) but this is not true for the Charney--Phillips staggering.

On a finite volume mesh, variables are ordinarily placed at cell centres or cell faces.  In the Charney--Phillips staggering, the thermodynamic variable is placed at only those cell faces that lie on the vertical coordinate surfaces, and vertically-oriented faces have no thermodynamic information.  This existing staggering is unsuitable for arbitrarily-structured finite volume meshes because faces can have any orientation.

## Mesh refinement

Controlling the vertical mesh spacing near the ground is straightforward when terrain-following meshes are used because the mesh is organised in rows of cells that are uninterrupted by mountain peaks.  With other mesh types such as cut-cell meshes or slanted-cell meshes, controlling vertical mesh spacing is less straightforward because mountain peaks interrupt the rows of cells nearest sea level.   On such meshes, if fine vertical mesh spacing was used near sea level and coarse mesh spacing used aloft, then the mesh above a high-altitude mountain range would have coarse spacing and boundary layer processes would be poorly resolved.

Mesh refinement could help to increase the resolution of the boundary layer above high-altitude mountain ranges for cut-cell meshes and slanted-cell meshes.
Mesh refinement has received growing attention in atmospheric modelling literature because it could enable atmospheric models to produce more accurate forecasts with less computation.
While much of this literature concentrates on horizontal refinement, some investigations have been made into vertical refinement on two-dimensional `x`–`z` planes: [Müller et al. 2013](https://doi.org/10.1016/j.jcp.2012.10.038) have used conforming refinement of triangular meshes for simulating the standard rising bubble and density current test cases, and [Yamazaki & Satomura 2012](https://doi.org/10.1002/asl.358) have used nonconforming block-refinement to better resolve the atmosphere immediately above idealised mountains.

<!---TODO: is there any other literature about high resolution near the ground for cut-cells?-->

According to [Thuburn and Woollings 2005](https://doi.org/10.1016/j.jcp.2004.08.018), the vertical discretisation that Yamazaki & Satomura 2012 used supports computational modes and instabilities, although these errors were not excited by the test cases performed by Yamazaki & Satomura 2012.  The Charney--Phillips staggering is unsusceptible to such errors, but we are not aware of any existing literature that combines mesh refinement with a Charney--Phillips staggering.

We propose to develop a generalised Charney--Phillips staggering for arbitrarily-structured meshes.  By allowing for any mesh structure we can support almost any type of mesh including conforming and non-conforming mesh refinement, terrain-following meshes, cut-cell meshes and slanted-cell meshes.
We will develop a new generalised Charney--Phillips variant of the non-hydrostatic model by Weller & Shahrokhi 2014 that will enable a like-for-like comparison of Lorenz and generalised Charney--Phillips staggerings.
<!--TODO: explain tests that we want to do-->
<!--TODO: close by reiterating benefits-->


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

<!---
Almost all atmospheric models treat horizontal and vertical dimensions separately, leading to separate choices of horizontal and vertical staggerings.  In the horizontal, the Arakawa C-grid is commonly used because inertio-gravity waves have accurate dispersion properties [Arakawa and Lamb 1977](https://books.google.co.uk/books?id=nN_4561KTIIC&lpg=PA173&ots=yKV39fe7eu&dq=Computational%20design%20of%20the%20basic%20dynamical%20processes%20of%20the%20UCLA%20general%20circulation%20model&lr&pg=PA173#v=onepage&q&f=false).
-->
