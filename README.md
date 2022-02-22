# Poset-Hypergraph-Curvature
 
This repository contains the codes and datasets associated with the following paper:<br>
<i>A Poset-Based Approach to Curvature of Hypergraphs.</i><br>
Yasharth Yadav, Areejit Samal, Emil Saucan*.<br>
Symmetry **2022**, 14, 420. https://doi.org/10.3390/sym14020420<br>

In the above paper, we represent hypergraphs as partially ordered sets or posets, and provide a geometric framework based on posets to compute the Forman–Ricci curvature of vertices as well as hyperedges in hypergraphs. Thereafter, we perform an empirical study involving computation and analysis of the Forman–Ricci curvature of hyperedges in 12 real-world hypergraphs.

## Codes

1. **_generate_poset.py_**: Python script to generate the two-dimensional simplicial complex associated with a hypergraph. Details of the input and output files are provided within the script. 
2. **_poset_geometry.py_**: Python script to compute the Forman-Ricci curvatures, scalar curvatures and the Euler characteristic of the two-dimensional simplicial complex associated with a hypergraph. Details of the input and output files are provided within the script. 

## Hypergraph datasets

The directory [hypergraph_datasets]() contains the 12 real-world hypergraphs considered in our work. 

**Note:** Please cite the mentioned references if you use a dataset in your work.

- **biogrid**
  - Stark, C.; Breitkreutz, B.J.; Reguly, T.; Boucher, L.; Breitkreutz, A.; Tyers, M. BioGRID: A general repository for interaction datasets.
Nucleic Acids Res. 2006, 34, D535–D539.

- **protein-complex**
  - Giurgiu, M.; Reinhard, J.; Brauner, B.; Dunger-Kaltenbach, I.; Fobo, G.; Frishman, G.; Montrone, C.; Ruepp, A. CORUM: The comprehensive resource of mammalian protein complexes-2019. Nucleic Acids Res. 2018, 47, D559–D563.

- **disease-gene**
  - Pi&#241;ero, J.; Ram&#237;rez-Anguita, J.M.; Saüch-Pitarch, J.; Ronzano, F.; Centeno, E.; Sanz, F.; Furlong, L.I. The DisGeNET knowledge platform for disease genomics: 2019 update. Nucleic Acids Res. 2019, 48, D845–D855.

- **corporate-memberships**
  - Faust, K. Centrality in affiliation networks. Soc. Netw. 1997, 19, 157–191.
 
- **senate-committees** 
  - Benson, A.R.; Abebe, R.; Schaub, M.T.; Jadbabaie, A.; Kleinberg, J. Simplicial closure and higher-order link prediction. Proc. Natl. Acad. Sci. USA 2018, 115, E11221–E11230.
  - Stewart, C.; Woon, J. Congressional Committee Assignments, 103rd to 114th Congresses, 1993–2017. Available online: http://web.mit.edu/17.251/www/data_page.html (accessed on 10 February 2022).

- **norwegian-directorate**
  - Seierstad, C.; Opsahl, T. For the few not the many? The effects of affirmative action on presence, prominence, and social capital of women directors in Norway. Scand. J. Manag. 2011, 27, 44–54.
  
- **youtube-groups**
  - Mislove, A.; Marcon, M.; Gummadi, K.P.; Druschel, P.; Bhattacharjee, B. Measurement and Analysis of Online Social Networks. In Proceedings of the 5th ACM/Usenix Internet Measurement Conference (IMC’07), San Diego, CA, USA, 24–26 October 2007.

- **facebook-forum**
  - Opsahl, T. Triadic closure in two-mode networks: Redefining the global and local clustering coefficients. Soc. Netw. 2013, 35, 159–167.

- **enron-email**
  - Klimt, B.; Yang, Y. The Enron Corpus: A New Dataset for Email Classification Research. In Machine Learning: ECML 2004; Boulicaut, J.F., Esposito, F., Giannotti, F., Pedreschi, D., Eds.; Springer: Berlin/Heidelberg, Germany, 2004; pp. 217–226.

- **contact-highschool**
  - Mastrandrea, R.; Fournet, J.; Barrat, A. Contact Patterns in a High School: A Comparison between Data Collected UsingWearable Sensors, Contact Diaries and Friendship Surveys. PLoS ONE 2015, 10, e0136497.

- **github-projects**
  - Kunegis, J. KONECT: The Koblenz Network Collection. In Proceedings of the 22nd International Conference onWorldWideWeb (WWW ’13 Companion), Rio de Janeiro, Brazil, 13–17 May 2013; pp. 1343–1350.

- **cond-mat-publications**
  - Newman, M.E.J. The structure of scientific collaboration networks. Proc. Natl. Acad. Sci. USA 2001, 98, 404–409.
