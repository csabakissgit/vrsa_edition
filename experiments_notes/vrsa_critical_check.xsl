<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" indent="yes"/>

<!--<xsl:template match="*/text()[normalize-space()]">
    <xsl:value-of select="normalize-space()"/>
</xsl:template>

<xsl:template match="*/text()[not(normalize-space())]" />
-->

<xsl:template match="/">
<body>
<link rel="stylesheet" href="style_wrap_check.css"/>
<!--<link rel="stylesheet" href="style_wrap.css"/>-->
<!--<link rel="stylesheet" href="style_only_app.css"/>-->
<!--<script xmlns="http://www.w3.org/1999/xhtml" src="myfunction.js"></script>-->
       <xsl:apply-templates/>
</body>
</xsl:template>




<xsl:template match="TEXT">
<txt><xsl:apply-templates /> </txt>
<!--&#160;&#160;&#160;<button onclick="hideFunction()">↓</button>-->
</xsl:template>    




<xsl:template match="divv">
<div class="divv">
<xsl:apply-templates />
</div>
</xsl:template>    








<xsl:template match="PTEXT">
<!-- <font size="3" color="black"> -->
 &#160;&#160;&#160;<ptext><xsl:apply-templates /></ptext>
<!--</font>-->
</xsl:template>    


<xsl:template match="mainwrap">
<div class="tooltip-wrap"> 
<!-- <font size="3" color="black"> -->
	<versewrap><p><xsl:apply-templates /></p></versewrap>
<!--</font>-->
</div>
</xsl:template>    


<xsl:template match="apparatuswrap">
&#160;<input type="checkbox"></input>
<label>
<!--<div class="tooltip-content" type="checkbox">-->
<!-- <font size="3" color="black"> -->
	<app><xsl:apply-templates /></app>
<!--</font>-->
<!--</div>-->
</label>
</xsl:template>    



<xsl:template match="DhP">
 <a href="dharmaputrika_kafle.dn" target="_blank">
 <xsl:apply-templates /></a>
</xsl:template>    



<xsl:template match="i">

<i>
       <xsl:apply-templates />
</i>
</xsl:template>    

<xsl:template match="APP">
<input type="checkbox" checked="checked">
</input> Variants
<label>    
       <xsl:apply-templates />
</label>
</xsl:template>    

<xsl:template match="sub">
<sub><xsl:apply-templates/></sub>
</xsl:template>    

<xsl:template match="sup">
<sup><xsl:apply-templates/></sup>
</xsl:template>    


<xsl:template match="colophon">
<br/>
<colophon>||<xsl:apply-templates />||</colophon>
</xsl:template>  
  
<xsl:template match="TITLE">
<h1>
|<xsl:apply-templates />|
</h1>
</xsl:template>    

<xsl:template match="CHAPTER">
<h2>[<xsl:apply-templates/>]</h2>
</xsl:template>    

<xsl:template match="SUBCHAPTER">
<h3>[<xsl:apply-templates/>]</h3>
</xsl:template>    



<xsl:template match="PVAR">
       <pvar><p><xsl:apply-templates /></p></pvar>
</xsl:template>    


<xsl:template match="PARAL">
	 <paral><p><xsl:apply-templates /></p></paral>
</xsl:template>    


<xsl:template match="TR">
<input type="checkbox">
</input> Translation
<label>    
<trs> 
	"<xsl:apply-templates />"
</trs>
</label>
</xsl:template>    

<xsl:template match="NOTE">
<input type="checkbox">
</input> Notes
<label>    
       <xsl:apply-templates />
</label>
</xsl:template>    


<xsl:template match="PARAL">
<input type="checkbox">
</input> Parallel passages
<label>    
       <xsl:apply-templates />
</label>
</xsl:template>    


<xsl:template match="SKT">
<!--<details open="yes">-->
	<i><xsl:apply-templates /></i>
</xsl:template>    


<xsl:template match="LEM">
<lem><xsl:apply-templates /></lem> 
] 
</xsl:template>    

<xsl:template match="ms">
<ms><xsl:apply-templates /></ms> 
</xsl:template>    

<xsl:template match="corr">
<corr><xsl:apply-templates /></corr> 
</xsl:template>    


<xsl:template match="vsnum">
<vsnum><xsl:apply-templates /></vsnum>
</xsl:template>    

<xsl:template match="NEWCHAPTER">
<xsl:apply-templates />
</xsl:template>    

<xsl:template match="uvaca">
<xsl:apply-templates />
</xsl:template>    


</xsl:stylesheet>
