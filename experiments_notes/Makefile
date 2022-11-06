# must use tabs!
# this does not produce output in itself
myVrsasarasamgrahaProject: /home/csaba/indology/skt/saiva/sivadharma/vrsasarasamgraha.xml text_version_of_vrsa.txt  /home/csaba/indology/skt/saiva/sivadharma/vrsasarasangraha_velth.txt vrsasara_input.tex vrsasara_input_devnag.dn vrsasara_input_devnag.tex vrsasara_ed_rm.tex vrsasara_ed_devnag.tex vrsasara_ed_rm.pdf vrsasara_ed_devnag.pdf



# IAST only text version
text_version_of_vrsa.txt: /home/csaba/indology/skt/saiva/sivadharma/vrsasarasamgraha.xml
	textprocess.py -txt /home/csaba/indology/skt/saiva/sivadharma/vrsasarasamgraha.xml > ~/indology/dharma_project/vrsa_edition/text_version_of_vrsa.txt

# Velthuis only text version
/home/csaba/indology/skt/saiva/sivadharma/vrsasarasangraha_velth.txt: /home/csaba/indology/skt/saiva/sivadharma/vrsasarasamgraha.xml
	textprocess.py -velth /home/csaba/indology/skt/saiva/sivadharma/vrsasarasamgraha.xml > /home/csaba/indology/skt/saiva/sivadharma/vrsasarasangraha_velth.txt 
	
# LaTeX Roman version
vrsasara_ed_rm.pdf: vrsasara_input.tex vrsasara_ed_rm.tex
	pdflatex vrsasara_ed_rm.tex 

vrsasara_input.tex: /home/csaba/indology/skt/saiva/sivadharma/vrsasarasamgraha.xml
	textprocess.py -texrm2col /home/csaba/indology/skt/saiva/sivadharma/vrsasarasamgraha.xml > vrsasara_input.tex

# XaTeX Devanagari version
vrsasara_ed_devnag.pdf: vrsasara_input_devnag.tex vrsasara_ed_devnag.tex 
	xelatex vrsasara_ed_devnag.tex 

vrsasara_input_devnag.tex: vrsasara_input_devnag.dn
	devnag vrsasara_input_devnag.dn

vrsasara_input_devnag.dn: /home/csaba/indology/skt/saiva/sivadharma/vrsasarasamgraha.xml
	textprocess.py -texdn /home/csaba/indology/skt/saiva/sivadharma/vrsasarasamgraha.xml > vrsasara_input_devnag.dn

####xelatex vrsasara_ed_rm.tex 

