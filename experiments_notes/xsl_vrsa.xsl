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


<xsl:template match="sloka">
  <xsl:copy>
<xsl:choose>
        <xsl:when test="uvaca">
		<xsl:apply-templates select="uvaca"/><br/>
	</xsl:when>
        <xsl:otherwise></xsl:otherwise>
</xsl:choose>
<xsl:apply-templates select="padaab"/>|<br/>
     <xsl:choose>
        <xsl:when test="padaef">
<xsl:apply-templates select="padacd"/>|<br/>
<xsl:apply-templates select="padaef"/><font color="blue"><font size="3">||<xsl:value-of select="../../@chapterno" />.<xsl:value-of select="../@verseno" />||</font></font><br/>
</xsl:when>
        <xsl:otherwise>
<xsl:apply-templates select="padacd"/>
<font color="blue"><font size="3">||<xsl:value-of select="../../@chapterno" />.<xsl:value-of select="../@verseno" />||</font></font><br/>
</xsl:otherwise>
</xsl:choose>
<xsl:choose>
        <xsl:when test="paral">
<details><summary><font color="red">[Testimonia ad <xsl:value-of select="../../@chapterno" />.<xsl:value-of select="../@verseno" />]</font></summary><div style="word-wrap: break-word; width: 800px" >
<xsl:apply-templates select="paral"/><hr width="150px" align="left"/></div>
</details>
</xsl:when>
        <xsl:otherwise></xsl:otherwise>
</xsl:choose>
  </xsl:copy>
<xsl:choose>
        <xsl:when test="apparatus">
<details><summary><font color="red">[Apparatus ad <xsl:value-of select="../../@chapterno" />.<xsl:value-of select="../@verseno" />]</font></summary>
<xsl:apply-templates select="apparatus"/>
<hr width="150px" align="left"/>
</details>
</xsl:when>
        <xsl:otherwise></xsl:otherwise>
</xsl:choose>
</xsl:template>    

<!--<xsl:template match="sometag[@type='sometype']"> -->
<xsl:template match="apparatus">
&#160;&#160;&#160;&#160;
<font size="1"><span style="font-weight:bold;">
<font color="red"><xsl:value-of select="../../@verseno" /><xsl:value-of select="@pada" /></font>
&#160;</span>
<xsl:apply-templates />&#160;</font><br/>
</xsl:template>

<xsl:template match="paral">
<font size="1"><span style="font-weight:bold;">
<font color="green">&#160;&#160;&#160;&#160;<xsl:value-of select="../../@verseno" /><xsl:value-of select="@pada" /></font>
&#160;</span>
<xsl:apply-templates />&#160;</font>
</xsl:template>    

<xsl:template match="uvaca">
<xsl:apply-templates />
</xsl:template>    

<xsl:template match="l">
<font size="3">
<br/>
<font color="#4e0f01">
<xsl:apply-templates /></font>
</font>
</xsl:template>    

<xsl:template match="chapterheader">
<h2><xsl:apply-templates /></h2>
</xsl:template>    

<xsl:template match="sktchapter">
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;
<span style="font-weight:bold;">
[<xsl:apply-templates />]<br/>
</span>
</xsl:template>    

<xsl:template match="colophon">
&#160;&#160;&#160;&#160;&#160;&#160;&#160;
||<xsl:apply-templates />||
</xsl:template>    

<xsl:template match="colophonapparatus">
<details><summary><font color="red">[Apparatus ad Colophon]</font></summary>
&#160;&#160;&#160;&#160;&#160;&#160;&#160;<xsl:apply-templates />
</details>
</xsl:template>    



<xsl:template match="msW">
W</xsl:template>    

<xsl:template match="msJa">
J<sub>a</sub></xsl:template>    

<xsl:template match="msJb">
J<sub>b</sub></xsl:template>    

<xsl:template match="msJc">
J<sub>c</sub></xsl:template>    

<xsl:template match="msJd">
J<sub>d</sub></xsl:template>    

<xsl:template match="msJab">
J<sub>ab</sub></xsl:template>    

<xsl:template match="msJcd">
J<sub>cd</sub></xsl:template>    

<xsl:template match="msJall">
J</xsl:template>    

<xsl:template match="bullet">
&#8226;</xsl:template>    

<xsl:template match="lem">
<font size="2"> ] </font>
</xsl:template>    

<xsl:template match="eme">
<span style="font-style:italic;">eme.</span></xsl:template>    

<xsl:template match="corr">
<span style="font-style:italic;">corr.</span></xsl:template>    

<xsl:template match="conj">
<span style="font-style:italic;">conj.</span></xsl:template>    

<xsl:template match="Codd">
Codd.</xsl:template>    

<xsl:template match="person">
<xsl:apply-templates /></xsl:template>    

<xsl:template match="appnote">
<span style="font-style:italic;"><xsl:apply-templates /></span></xsl:template>    

<xsl:template match="skt">
<span style="font-style:italic;"><xsl:apply-templates /></span>
</xsl:template>    

</xsl:stylesheet>
