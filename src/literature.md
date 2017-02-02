## Questions

* Who has made like-for-like comparisons between Lorenz and Charney--Phillips?
  * Tokioka 1978, Chang 1992, Sabutis 1994, Arakawa and Konor 1996, Zhu and Smith 2003
* What models have used C--P?
  * Operational: UKMO EndGame (Davies et al. 2005), Canadian GEM4 (Girard et al. 2014), Chinese Global/Regional Assimilation and PrEdiction System (GRAPES) (XueSheng et al. 2007)
  * Research: Robert et al. 1972, Qian et al. 1998, MC2 (Girard et al. 2005), FSU GSM (Krishnamurti 1969, Krishnamurti et al. 2007), Melvin et al. 2010, Durran and Blossey 2012, Wood et al. 2014
* What evidence is there for the Lorenz computational mode?
* What evidence is there that C--P is superior to Lorenz?
* Has anyone discussed advection schemes for C--P?
  * Guerra and Ullrich 2016
  * Yamazaki et al. 2016
  * Cotter and Kuzmin 2016
  
## Possible discrepancies

Are these correct assertions:
* Tokioka 1978 advocate their C' staggering which Zhu and Smith 2003 seem to call an A-grid.  Zhu and Smith 2003 say that Arakawa and Moorthi 1988 show why it is bad.
* Yakimiw and Girard 1987 says that Staniforth and Daley 1977 are unstaggered but it seems that they might actually be staggered?  In any case Schneider 1987 says they avoid the Lorenz computational mode.

## Chronological list

The :white_check_mark: symbol shows those articles where I've finished taking notes.

* [Krishnamurti 1969](https://doi.org/10.1002/qj.49709540511) :white_check_mark:
  * Primitive equation model, later to become the FSM GMS, uses C--P staggering (but don't name it as such)

* [Robert et al. 1972](https://doi.org/10.1175/1520-0493(1972)100<0329:AITISF>2.3.CO;2) :white_check_mark:
  * Primitive equation model uses C--P staggering (but don't name it as such)
  
* [Mesinger 1973](https://doi.org/10.1111/j.2153-3490.1973.tb00629.x)

* [Tokioka 1978](https://www.jstage.jst.go.jp/article/jmsj1965/56/2/56_2_98/_article) :white_check_mark:
  * good vertical dispersion especially important for stratospheric modelling
  * consider 8 staggerings of u,w,rho,p that include Lorenz (their scheme A) and C--P (their scheme B)
  * C--P doesn't have computational mode but still has poor dispersion properties at high wavenumbers (don't properly understand this yet)
  * choose another staggering (their scheme C') with w and p collated at half-levels, u and rho collated at full-levels, already used by [Shuman and Hovermale 1968](https://doi.org/10.1175/1520-0450(1968)007<0525:AOSLPE>2.0.CO;2), [Kasahara and Washington 1967](https://doi.org/10.1175/1520-0493(1967)095<0389:NGGCMO>2.3.CO;2)
  
* H Sundquist 1979, Vertical coordinates and related discretization, GARP Report 17 Volume II, World Meteorological Organization, Geneva, 1--150

* [Arakawa and Suarez 1983](https://doi.org/10.1175/1520-0493(1983)111<0034:VDOTPE>2.0.CO;2)
  * use Tokioka 1978's C' scheme in a primitive equation model

* [Yakimiw and Girard 1987](https://doi.org/10.1080/07055900.1987.9649277) :white_check_mark:
  * staggering chosen to eliminate spurious 2dz waves (Mesinger 1973)
  * compares four vertical discretisations for a global spectral model:
    * FD staggered ([Daley et al. 1976](http://www.tandfonline.com/doi/pdf/10.1080/00046973.1976.9648405)) operational at Canadian Met Centre
    * Constant FE staggered/unstaggered
    * Linear FE unstaggered ([Staniforth and Daley 1977](https://doi.org/10.1175/1520-0493(1977)105<1108:AFEFFT>2.0.CO;2))
  * Finite difference poorest overall but not by much
  * Girard 1983 reviews more FEM vertical discretisations

* [Schneider 1987](https://doi.org/10.1175/1520-0493(1987)115<2166:AIIVDI>2.0.CO;2) :white_check_mark:
  * Lorenz staggering that is inconsistent with the continuous equations (shown by trying to invert a square matrix that is singular -- system is overdetermined)
  * computational mode excited by thermal forcing
  * suggest a C--P staggering as a remedy (but don't name it as such)

* [Arakawa and Moorthi 1988](https://doi.org/10.1175/1520-0469(1988)045<1688:BIIVDS>2.0.CO;2)

* [Cullen 1989](https://doi.org/10.1016/0021-9991(89)90211-8)

* [Tanguay et al. 1990](https://doi.org/10.1175/1520-0493(1990)118<1970:ASISLF>2.0.CO;2)

* [Laprise and Girard 1990](https://doi.org/10.1175/1520-0442(1990)003<0032:ASGCMU>2.0.CO;2)

* [Chang 1992](https://doi.org/10.1175/1520-0469(1992)049<2452:RNMOTE>2.0.CO;2) :white_check_mark:
  * compares Lorenz and C--P variants of QG model and primitive equation model
  * spurious waves found in Lorenz QG model
  * spurious waves found in Lorenz and slower-growing spurious waves in C--P primitive equation model
  * more diffusion required to eliminate spurious modes in Lorenz variant compared to C--P
  * waves are similar to Arakawa and Moorthi 1988
  * Lorenz model overestimates growth of Stone's nongeostrophy mode ([Stone 1996](https://doi.org/10.1175/1520-0469(1966)023<0390:ONGBS>2.0.CO;2), [1970](https://doi.org/10.1175/1520-0469(1970)027<0721:ONGBSP>2.0.CO;2), [Nakamura 1988](https://doi.org/10.1175/1520-0469(1988)045<3253:SSOBIO>2.0.CO;2)) more than C--P

* Arakawa and Konor 1994, Comparison of atmospheric models based on the Lorenz and Charney-Phillips grids

* [Fox-Rabinovitz 1994](https://doi.org/10.1175/1520-0493(1994)122<0377:CDPOVS>2.0.CO;2)

* [Clark and Haynes 1994](https://doi.org/10.1175/1520-0469(1994)051<2101:EIIEOV>2.0.CO;2)
  * equatorial inertial instability
  * growing modes of any wavenumber are supported by Lorenz staggering
  * wavenumber has upper bound for C--P staggering

* [Sabutis 1994](https://doi.org/10.1175/1520-0493(1994)122<2868:TCOAVG>2.0.CO;2) :white_check_mark:
  * compares unstaggered, Lorenz and C--P staggerings in zonally-averaged 2.5D model of the middle atmosphere
  * finds spurious waves propagating vertically with Lorenz staggering
  * closely follows Tokioka 1978's dispersion analysis but with a different equation set

* [Cullen and James 1994](https://digital.nmla.metoffice.gov.uk/file/sdb%3AdigitalFile|38388ae5-134a-4d00-87cc-72b3a4b7de9b/)

* [Hollingsworth 1995](http://www.ecmwf.int/en/elibrary/9943-spurious-mode-lorenz-arrangement-y-and-t-which-does-not-exist-charney-phillips)

* [Qian et al. 1998](https://doi.org/10.1175/1520-0493(1998)126<0747:AGNSLA>2.0.CO;2) :white_check_mark:
  * Semi-implicit semi-Lagrangian global model using C--P staggering
  * Did this model get developed further?

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

* [Zhu and Smith 2003](https://doi.org/10.1256/qj.02.78) :white_check_mark:
  * compare Lorenz and C--P variants of a three-layer hurricane model
  * computational mode in temperature triggered by latent heat release with Lorenz staggering
  * Anthes et al. 1979 and Anthes 1972 use "A-grid" (this is not the Arakawa A-grid!) but it still suffers from a computational mode
  * Tokioka 1978 advocated the A-grid but Arakawa and Moorthi 1988 showed why Tokioka was mistaken
  * computational mode is present in any staggering with horizontal velocity and theta collocated, not just Lorenz staggering

* [Zadra et al. 2004](https://doi.org/10.1256/qj.03.208) :white_check_mark:
  * GEM3 uses collocation in the vertical
  * "Vertical diffusion is essential to prevent the growth of spurious modes near the surface"
  * vertically propagating 2dz waves due to dynamical core (footnote on p.2549)

* [Bourchtein et al. 2004](https://doi.org/10.1016/S0377-0427(03)00640-X) :white_check_mark:
  * analysis of well-posedness of linearized, vertically-discrete hydrostatic equations
  * find that both Lorenz and C--P are well-posed

* [Untch and Hortal 2004](https://doi.org/10.1256/qj.03.173)
  * vertical finite-elements for ECMWF compared with Lorenz and C--P finite difference
  * FEM suffers less from Lorenz computational mode
  * Holdaway et al. 2013 Part I say that ECMWF (presumably the FEM) is a modification of the Lorenz staggering

* [Thuburn and Woolings 2005](https://doi.org/10.1016/j.jcp.2004.08.018)
  * Exhaustive testing of vertical configurations (vertical coordinate, prognostic variables, and staggering)

* [Girard et al. 2005](https://doi.org/10.1175/MWR2931.1) :white_check_mark:
  * Canadian MC2 model uses a form of C--P with a generalised buoyancy variable collated with w at half-levels

* [Davies et al. 2005](https://doi.org/10.1256/qj.04.101) :white_check_mark:
  * UKMO EndGame model uses C--P staggering
  * Main drawback of C--P: temperature at pressure points is approximated by vertical averaging, but this is not appropriate in the lowest layer where there are large temperature gradients
  * EndGame works around this by assuming θ at the pressure point is the same as θ at the half-level immediately above (if I understand correctly)

* [Thuburn 2006](https://doi.org/10.1256/qj.06.10)

* [Toy and Randall 2007](https://doi.org/10.1016/j.jcp.2006.08.022)

* [XueSheng et al. 2007](https://doi.org/10.1007/s11430-007-0124-7) :white_check_mark:
  * Chinese GRAPES model uses C--P staggering
  
* [Krishnamurti et al. 2007](https://doi.org/10.1111/j.1600-0870.2007.00278.x) :white_check_mark:
  * Florida State University Global Spectral Model (FSU GSM) uses C--P staggering

* [Melvin et al. 2010](https://doi.org/10.1002/qj.603) :white_check_mark:
  * UKMO vertical slice model uses C--P staggering

* [Durran and Blossey 2012](https://doi.org/10.1175/MWR-D-11-00088.1) :white_check_mark:
  * Use C--P staggering to test their IMEX timestepping

* [Bourchtein and Bourchtein 2012](https://doi.org/10.1016/j.cam.2011.05.037) :white_check_mark:
  * mathematical analysis of vertical modes for hydrostatic models in generalised vertical coordinates
  * explains why the Lorenz computational mode does not appear in their analysis (but acknowledges that it does exist nonetheless)
  * find that a discretisation using Lorenz staggering closely approximates the continuous equations
  
* Holdaway et al. 2013 ([Part I](https://doi.org/10.1002/qj.2016) :white_check_mark:, [Part II](https://doi.org/10.1002/qj.2017))
  * investigates physics-dynamics coupling
  * Must choose a combination of: vertical coordinate, prognostic variables (three velocity and two thermodynamic), and staggering
  * One optimal configuration for dynamical core is height/theta+pressure/C--P
  * C--P good for PV and wave propagation, Lorenz good for conservation
  * Richardson number can be calculated straightforwardly on Lorenz grid but C--P requires averaging
  * Lorenz provides cleaner route for energy conservation than C--P
  * Model comparison is OK but less general than steady/time-variant decomposition
  * Does the BL scheme suppress the Lorenz computational mode?

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
  
* [Cotter and Kuzmin 2016](https://doi.org/10.1016/j.jcp.2016.02.021) :white_check_mark:
  * Upwind DG advection scheme for temperature
  * A new limiter for advection schemes in C--P space
  
* [Yamazaki et al. 2016](https://arxiv.org/abs/1611.04929) :white_check_mark:
  * A new advection scheme for temperature
  * Upwind DG method in the horizontal blended with Streamline Upwind Petrov Galerkin (SUPG) method in the vertical direction
