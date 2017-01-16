# A proposal for a generalised Charney--Phillips-like staggering of variables for arbitrarily-structured meshes

The Charney--Phillips vertical staggering of variables [Charney and Phillips 1953] is suitable for structured meshes with cells stacked in columns.
This staggering has been adopted by several operational models [Davies et al. 2005, Girard et al. 2014] because it avoids the computational mode that is associated with the Lorenz vertical staggering [Arakawa and Konor 1996].
The generalisation of the Lorenz staggering for unstructured or arbitrarily-structured meshes is straightforward [Weller and Shahrokhi 2014] but this is not true for the Charney--Phillips staggering.

On a finite volume mesh, variables are ordinarily placed at cell centres or cell faces.  In the Charney--Phillips staggering, the thermodynamic variable is placed at only those cell faces that lie on the vertical coordinate surfaces, and vertically-oriented faces have no thermodynamic information.

## who uses unusual meshes?

* unstructured (triangular) meshes [Smolarkiewicz and Szmelter 2011]
* locally-refined block-structured meshes [Yamazaki and Satomura 2012, Hubbard and Nikiforakis?]
* other AMR: behrens1996,1998 and giraldo2000 on triangular grids, see hubbard-nikiforakis
* grid nesting?

<!---
Almost all atmospheric models treat horizontal and vertical dimensions separately, leading to separate choices of horizontal and vertical staggerings.  In the horizontal, the Arakawa C-grid is commonly used because inertio-gravity waves have accurate dispersion properties [Arakawa and Lamb 1977].
-->


## References 

[Arakawa and Konor 1996] 10.1175/1520-0493(1996)124<0511:VDOTPE>2.0.CO;2
[Arakawa and Lamb 1977] Computational design of the basic dynamical processes of the UCLA general circulation model
[Charney and Phillips 1953] 10.1175/1520-0469(1953)010<0071:NIOTQG>2.0.CO;2
[Davies et al. 2005] 10.1256/qj.04.101
[Girard et al. 2014] 10.1175/MWR-D-13-00255.1
[Smolarkiewicz and Szmelter 2011] 10.2478/s11600-011-0043-z
[Weller and Shahrokhi 2014] 10.1175/MWR-D-14-00054.1
[Yamazaki and Satomura 2012] 10.1002/asl.358
