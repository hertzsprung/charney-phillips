## Questions

* Who has made direct comparisons between Lorenz and Charney--Phillips?
* What models have used C--P?
  * Operational: UKMO EndGame (Davies et al. 2005), Canadian GEM4 (Girard et al. 2014), Chinese Global/Regional Assimilation and PrEdiction System (GRAPES) (XueSheng et al. 2007)
  * Research: Robert et al. 1972, Melvin et al. 2010, Wood et al. 2014
* What evidence is there for the Lorenz computational mode?
* What evidence is there that C--P is superior to Lorenz?
* Has anyone discussed advection schemes for C--P?
  * Guerra and Ullrich 2016

## Chronological list

The :white_check_mark: symbol shows those articles where I've finished taking notes.

* [Robert et al. 1972](https://doi.org/10.1175/1520-0493(1972)100<0329:AITISF>2.3.CO;2)
  * Use C--P staggering (but don't give it a name)

* [Tokioka 1978](https://www.jstage.jst.go.jp/article/jmsj1965/56/2/56_2_98/_article)

* [Yakimiw and Girard 1987](https://doi.org/10.1080/07055900.1987.9649277)

* [Schnieder 1987](https://doi.org/10.1175/1520-0493(1987)115<2166:AIIVDI>2.0.CO;2)

* [Arakawa and Moorthi 1988](https://doi.org/10.1175/1520-0469(1988)045<1688:BIIVDS>2.0.CO;2)

* [Cullen 1989](https://doi.org/10.1016/0021-9991(89)90211-8)

* [Tanguay et al. 1990](https://doi.org/10.1175/1520-0493(1990)118<1970:ASISLF>2.0.CO;2)

* [Laprise and Girard 1990](https://doi.org/10.1175/1520-0442(1990)003<0032:ASGCMU>2.0.CO;2)

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

* [Cullen and James 1994](https://digital.nmla.metoffice.gov.uk/file/sdb%3AdigitalFile|38388ae5-134a-4d00-87cc-72b3a4b7de9b/)

* [Hollingsworth 1995](http://www.ecmwf.int/en/elibrary/9943-spurious-mode-lorenz-arrangement-y-and-t-which-does-not-exist-charney-phillips)

* [Semazzi et al. 1995](https://doi.org/10.1175/1520-0493(1995)123<2534:AGNSLA>2.0.CO;2)

* [Fox-Rabinovitz 1996](https://doi.org/10.1175/1520-0493(1996)124<0498:CDPOSG>2.0.CO;2)

* [Arakawa and Konor 1996](https://doi.org/10.1175/1520-0493(1996)124<0511:VDOTPE>2.0.CO;2) 
  * C--P originally applied to QG model
  * C--P conserves advected QGPV 
  * Lorenz conserves total energy, mean and variance of theta
  * Lorenz has computational mode (Tokioka 1978; Arakawa 1988; Cullen and James 1994; Hollingsworth 1995)
  * Spurious short-wave amplification due to baroclinic instability (Arakawa and Moorthi 1988)
  * C--P has been used for primitive equation models: Krishnamurti 1969, Robert et al. 1972

* [Konor and Arakawa 1997](https://doi.org/10.1175/1520-0493(1997)125<1649:DOAAMB>2.0.CO;2)

* [Cullen et al. 1997](https://doi.org/10.1080/07055900.1997.9687359)

* [Skamarock et al. 1997](https://doi.org/10.1175/1520-0493(1997)125<0587:PCRSFH>2.0.CO;2) :white_check_mark:
  * A Helmholtz solver that is suitable for nonhydrostatic flows over steep slopes
  * Lorenz staggering complicates the Helmholtz solver, the problem is not present with C--P staggering (see very end of section 2)

* [Bell 2003](https://doi.org/10.1175/1520-0493(2003)131<1498:COPVOL>2.0.CO;2) :white_check_mark:
  * distinguishes between original Lorenz and modified Lorenz staggerings
  * original Lorenz used by Lorenz 1960, Arakawa and Lamb 1997
  * modified Lorenz was used by Tokioka 1978, Simmons and Burridge 1981, Arakawa and Suarez 1983
  * formulates QGPV-conserving scheme using modified Lorenz staggering

* [Thuburn et al. 2002](https://doi.org/10.1256/003590002320603403)
  * section 5 discusses C--P

* [Zhu and Smith 2003](https://doi.org/10.1256/qj.02.78)
  * minimal hurricane model

* [Zadra et al. 2004](https://doi.org/10.1256/qj.03.208)
  * "Vertical diffusion is essential to prevent the growth of spurious modes near the surface"

* [Bourchtein et al. 2004](https://doi.org/10.1016/S0377-0427(03)00640-X)
  * hydrostatic models

* [Untch and Hortal 2004](https://doi.org/10.1256/qj.03.173)
  * vertical finite-elements for ECMWF compared with Lorenz and C--P finite difference
  * FEM suffers less from Lorenz computational mode
  * Holdaway et al. 2013 Part I say that ECMWF (presumably the FEM) is a modification of the Lorenz staggering

* [Thuburn and Woolings 2005](https://doi.org/10.1016/j.jcp.2004.08.018)
  * Exhaustive testing of vertical configurations (vertical coordinate, prognostic variables, and staggering)

* [Girard et al. 2005](https://doi.org/10.1175/MWR2931.1)

* [Davies et al. 2005](https://doi.org/10.1256/qj.04.101)
  * UKMO EndGame model uses C--P staggering
  * Main drawback of C--P: temperature at pressure points is approximated by vertical averaging, but this is not appropriate in the lowest layer where there are large temperature gradients
  * EndGame works around this by assuming θ at the pressure point is the same as θ at the half-level immediately above (if I understand correctly)

* [Thuburn 2006](https://doi.org/10.1256/qj.06.10)

* [Toy and Randall 2007](https://doi.org/10.1016/j.jcp.2006.08.022)

* [XueSheng et al. 2007](https://doi.org/10.1007/s11430-007-0124-7)
  * Chinese GRAPES model uses C--P staggering

* [Melvin et al. 2010](https://doi.org/10.1002/qj.603) :white_check_mark:
  * UKMO vertical slice model uses C--P staggering

* [Qaddouri and Lee 2011](https://doi.org/10.1002/qj.873)
  * Canadian GEM model uses C--P staggering

* [Bourchtein and Bourchtein 2012](https://doi.org/10.1016/j.cam.2011.05.037)
  * mathematical analysis of vertical modes for hydrostatic models in generalised vertical coordinates

* Holdaway et al. 2013 ([Part I](https://doi.org/10.1002/qj.2016), [Part II](https://doi.org/10.1002/qj.2017))
  * Must choose a combination of: vertical coordinate, prognostic variables (three velocity and two thermodynamic), and staggering

* [Girard et al. 2014](https://doi.org/10.1175/MWR-D-13-00255.1)
  * Canadian GEM4 model uses C--P staggering
  * GEM3 model used collation in the vertical that caused spurious 2Δz waves (Zadra et al. 2004)
  * Lots of discussion on staggering configurations and lots of citations

* [Wood et al. 2014](https://doi.org/10.1002/qj.2235) :white_check_mark:
  * SISL nonhydrostatic deep atmosphere model using C--P staggering

* [Guerra and Ullrich 2016](https://doi.org/10.5194/gmd-9-2007-2016) :white_check_mark:
  * local, flow-dependent hyperviscosity is applied in the vertical, akin to advective upwinding
  * Schär wave test shows spurious oscillations in vertical velocity on vertically-collocated mesh that is not present on Lorenz or C--P staggerings
  * Straka density current test reveals **problem with advection of θ** that leads to a discontinuity at the lower boundary (p. 2019)
  * Not clear whether rising bubble tests are performed on collocated/Lorenz/C--P mesh
