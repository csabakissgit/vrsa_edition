<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" indent="yes"/>

<!--<xsl:template match="*/text()[normalize-space()]">
    <xsl:value-of select="normalize-space()"/>
</xsl:template>

<xsl:template match="*/text()[not(normalize-space())]" />
-->

<xsl:template match="/">
<body>
<link rel="stylesheet" href="style.css"/>
           <xsl:apply-templates/>
<br/><br/><br/><br/>
</body>
</xsl:template>




<xsl:template match="TEXT">
  <xsl:copy>
<!-- <font size="3" color="black"> -->
	<xsl:apply-templates />
	<br/>
<!--</font>-->
  </xsl:copy>
</xsl:template>    

<xsl:template match="TITLE">
<span style="font-weight:bold;">
<font size="6" color="black">
	<xsl:apply-templates />&#160;
	<br/>
</font>
</span>
</xsl:template>    

<xsl:template match="CHAPTER">
<!--<span style="font-weight:bold;">
<font size="4" color="black">-->
<h1>[<xsl:apply-templates/>]</h1>
<!--</font>
</span>-->
</xsl:template>    

<xsl:template match="SUBCHAPTER">
<!--<span style="font-weight:bold">
<font size="3" color="grey">-->
<h2>[<xsl:apply-templates/>]</h2>
<!--</font>
</span>-->
</xsl:template>    


<xsl:template match="APP">
</xsl:template>    

<xsl:template match="PARAL">
</xsl:template>    

<xsl:template match="SKT">
<!--<details open="yes">-->
	<i><xsl:apply-templates /></i>
</xsl:template>    

<xsl:template match="PVAR">
</xsl:template>    

<xsl:template match="SKT">
<!--<details open="yes">-->
	<i><xsl:apply-templates /></i>
</xsl:template>    


<xsl:template match="LEM">
<!--<font size="1" style="font-weight:bold;">    --> 
<lem><xsl:apply-templates /></lem> 
] 
<!--</font>-->
</xsl:template>    


<xsl:template match="ms">
<!--<font size="1" style="font-weight:bold;">    --> 
<ms><xsl:apply-templates /></ms> 
<!--</font>-->
</xsl:template>    


<xsl:template match="sub">
<sub><xsl:apply-templates/></sub>
</xsl:template>    

<xsl:template match="sup">
<sup><xsl:apply-templates/></sup>
</xsl:template>    


<xsl:template match="corr">
<!--<font size="1" style="font-weight:bold;">    --> 
<corr><xsl:apply-templates /></corr> 
<!--</font>-->
</xsl:template>    


<xsl:template match="vsnum">
<!--<font size="1" style="font-weight:bold;">    --> 
<vsnum><xsl:apply-templates /></vsnum>
<!--</font>-->
</xsl:template>    

<xsl:template match="NEWCHAPTER">
<br/><br/><br/><xsl:apply-templates />
</xsl:template>    

<xsl:template match="uvaca">
<!--<span style="font-weight:bold;">
<font size="2" color="red">-->
<uv><xsl:apply-templates /></uv>
<!--</font>
</span>-->
</xsl:template>    


</xsl:stylesheet>
