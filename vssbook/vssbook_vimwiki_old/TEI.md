TEI °s:
:%s/>°/ rend="circlefront">/g
:%s/>.*°/ rend="circleback">&/g
:%s/rend="circlefront rend="circleback"/rend="circlearound"/g
:%s/°//g       

Indexing the xml file:
%index_geo etc.
 
