library(ape)
library(ggtree)
        
tree <- read.tree("PhyML_tree")
tree <- groupClade(tree, c(25, 17, 22, 20))

p<-ggtree(tree)+geom_nodepoint()+geom_cladelabel(node=17, label="Группа D", align=T, geom='label', fill='lightblue',offset=.8,fontsize = 6)+geom_cladelabel(node=22, label="Группа A", align=T, geom='label', fill='lightblue', offset=.8, fontsize = 6)+geom_cladelabel(node=20, label="Группа Е", align=T, geom='label', fill='lightblue', offset=.8, fontsize = 6)+geom_cladelabel(node=25, label="Группа B", align=T, geom='label', fill='lightblue', offset=.8, fontsize = 6)+xlim(0, 4.9)

sp_leg<-data.frame(tip = tree$tip.label, Species =c("P_pictoides", "E_verrucosus", "M_parvulus", "O_flavus", "O_flavus", "E_verrucosus", "O_flavus", "E_verrucosus","P_pictoides", "M_parvulus", "P_pictoides", "E_verrucosus", "O_flavus", "M_parvulus" )
 )

p %<+% sp_leg + geom_tiplab(aes(color=Species), fontface = "bold")+theme(legend.position="bottom")
