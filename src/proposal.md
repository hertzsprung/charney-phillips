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

## A generalised Charney--Phillips staggering

We propose to formulate a generalised Charney--Phillips staggering for arbitrarily-structured meshes.  By allowing for any mesh structure we can support almost any type of mesh including conforming and non-conforming mesh refinement, terrain-following meshes, cut-cell meshes and slanted-cell meshes.
We will implement a new, generalised Charney--Phillips variant of the non-hydrostatic model by Weller & Shahrokhi 2014 that will enable a like-for-like comparison of Lorenz and generalised Charney--Phillips staggerings.
Two series of tests will be performed that verify the generalised Charney--Phillips formulation and implementation.  First, we will reimplement one or more test cases from Arakawa & Konor 1996 that are expected to excite the computational mode in the Lorenz variant of this model, and we expect no such errors when the generalised Charney--Phillips variant is used.
Second, we will perform the mountain waves test case by [Schär et al. 2002](https://doi.org/10.1175/1520-0493%282002%29130<2459:ANTFVC>2.0.CO;2) using meshes with conforming and nonconforming refinement.  Results will be compared using the Lorenz and generalised Charney--Phillips model variants.

Two additional tasks might be performed if time permits.  First, results of the mountain waves test might be improved by designed a more accurate advection scheme for potential temperature for the generalised Charney--Phillips variant of the model.  Second, we might want to include a semi-implicit treatment of gravity-waves to enable longer time-steps.  This formulation already exists in the Lorenz variant, but a new formulation would be required for the generalised Charney--Phillips variant.

We imagine that future atmospheric models could benefit from the improved accuracy that cut-cell meshes or slanted-cell meshes can offer, and use some form of mesh refinement to better resolve the boundary-layer at high altitudes.  By formulating a generalised Charney--Phillips staggering for arbitrarily-structured meshes we hope that these future models can benefit from improved meshes while avoiding errors associated with the Lorenz computational mode.

## Estimation of work

This is my attempt to estimate the items of work that I expect to be completed:

1. 1 month -- Recreate one or more Arakawa & Konor 1996 test cases in OpenFOAM
2. 2 months -- Formulate the generalised Charney--Phillips staggering and implement it in OpenFOAM
3. 1 month -- Create the Schär et al. 2002 mountain waves test with conforming and nonconforming mesh refinement, and obtain ‘acceptable’ results with the new generalised Charney--Phillips model variant

Additional tasks:

4. 2 months -- Develop a new advection scheme for potential temperature
5. 1 month -- Design a semi-implicit treatment for gravity waves for the generalised Charney--Phillips model variant

## Comparing the merits of Charney--Phillips and Lorenz staggerings

* [Chang 1992](https://doi.org/10.1175/1520-0469(1992)049<2452:RNMOTE>2.0.CO;2)
  * spurious short-wave amplification found in Lorenz and C--P primitive equation model
  * waves are similar to Arakawa and Moorthi 1988
  * growth rate smaller in C--P variant

* Arakawa and Konor 1994, Comparison of atmospheric models based on the Lorenz and Charney-Phillips grids

* [Fox-Rabinovitz 1994](https://doi.org/10.1175/1520-0493(1994)122<0377:CDPOVS>2.0.CO;2)

* [Clark and Haynes 1994](https://doi.org/10.1175/1520-0469(1994)051<2101:EIIEOV>2.0.CO;2)
  * equatorial inertial instability
  * growing modes of any wavenumber are supported by Lorenz staggering
  * wavenumber has upper bound for C--P staggering

* [Sabutis 1994](https://doi.org/10.1175/1520-0493(1994)122<2868:TCOAVG>2.0.CO;2)
  * compares unstaggered, Lorenz and C--P staggerings
  * studies vertical waves of varying lengths
  * finds spurious waves propagating vertically with Lorenz staggering

* [Hollingsworth 1995](http://www.ecmwf.int/en/elibrary/9943-spurious-mode-lorenz-arrangement-y-and-t-which-does-not-exist-charney-phillips)

* [Fox-Rabinovitz 1996](https://doi.org/10.1175/1520-0493(1996)124<0498:CDPOSG>2.0.CO;2)

* [Arakawa and Konor 1996](https://doi.org/10.1175/1520-0493(1996)124<0511:VDOTPE>2.0.CO;2) 
  * C--P originally applied to QG model
  * C--P conserves advected QGPV 
  * Lorenz conserves total energy, mean and variance of theta
  * Lorenz has computational mode (Tokioka 1978; Arakawa 1988; Cullen and James 1994; Hollingsworth 1995)
  * Spurious short-wave amplification due to baroclinic instability (Arakawa and Moorthi 1988)
  * C--P has been used for primitive equation models: Krishnamurti 1969, Robert et al. 1972

* [Konor and Arakawa 1997](10.1175/1520-0493(1997)125<1649:DOAAMB>2.0.CO;2)

* [Bell 2003](https://doi.org/10.1175/1520-0493(2003)131<1498:COPVOL>2.0.CO;2)
  * distinguishes between original Lorenz and modified Lorenz staggerings
  * original Lorenz used by Lorenz 1960, Arakawa and Lamb 1997
  * modified Lorenz was used by Tokioka 1978, Simmons and Burridge 1981, Arakawa and Suarez 1983
  * formulates QGPV-conserving scheme using modified Lorenz staggering

* [Thuburn et al. 2002](https://doi.org/10.1256/003590002320603403)
  * section 5 discusses C--P

* [Zhu and Smith 2003](https://doi.org/10.1256/qj.02.78)
  * minimal hurricane model

* [Bourchtein et al. 2004](https://doi.org/10.1016/S0377-0427(03)00640-X)
  * hydrostatic models

* [Untch and Hortal 2004](https://doi.org/10.1256/qj.03.173)
  * vertical finite-elements for ECMWF compared with Lorenz and C--P finite difference
  * FEM suffers less from Lorenz computational mode

* [Davies et al. 2005](https://doi.org/10.1256/qj.04.101)
  * UKMO EndGame model uses C--P staggering

* [XueSheng et al. 2007](https://doi.org/10.1007/s11430-007-0124-7)
  * Chinese GRAPES model uses C--P staggering

* [Melvin et al. 2010](https://doi.org/10.1002/qj.603)

* [Qaddouri and Lee 2011](https://doi.org/10.1002/qj.873)
  * Canadian GEM model uses C--P staggering

* [Bourchtein and Bourchtein 2012](https://doi.org/10.1016/j.cam.2011.05.037)
  * mathematical analysis of vertical modes for hydrostatic models in generalised vertical coordinates

* Holdaway et al. 2013 ([Part I](https://doi.org/10.1002/qj.2016), [Part II](https://doi.org/10.1002/qj.2017))

* [Girard et al. 2014](https://doi.org/10.1175/MWR-D-13-00255.1)
  * Canadian GEM model uses C--P staggering

* [Wood et al. 2014](https://doi.org/10.1002/qj.2235)

* [Guerra and Ullrich 2016](https://doi.org/10.5194/gmd-9-2007-2016)
