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

<xsl:template match="lg">
  <xsl:copy>
	<div class="tooltip"><xsl:apply-templates />
|| <xsl:value-of select="@n"/></div>
  </xsl:copy>
</xsl:template>    

<xsl:template match="l">
  <xsl:copy>
	<br/><xsl:apply-templates />
  </xsl:copy>
</xsl:template>    

<xsl:template match="app">
  <xsl:copy>
	<div class="tooltiptext"><xsl:apply-templates /></div>
  </xsl:copy>
</xsl:template>    


</xsl:stylesheet>
