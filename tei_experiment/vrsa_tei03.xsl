<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" indent="yes"/>

<!--<xsl:template match="*/text()[normalize-space()]">
    <xsl:value-of select="normalize-space()"/>
</xsl:template>

<xsl:template match="*/text()[not(normalize-space())]" />
-->

<xsl:template match="/">
<body>
<link rel="stylesheet" href="style_tei.css"/>

       <xsl:apply-templates/>


<br/><br/><br/><br/>

</body>
</xsl:template>

<!--
<xsl:template match="node()|@*">
  <xsl:copy>
   <xsl:apply-templates select="node()|@*"/>
  </xsl:copy>
 </xsl:template>
-->

    <xsl:template match="title">
        <b><xsl:text>Title: </xsl:text></b>
		<xsl:apply-templates/><br/>
    </xsl:template>

    <xsl:template match="teiHeader">
		<xsl:apply-templates/><br/><br/><br/><br/>
    </xsl:template>


    <xsl:template match="author">
        <b><xsl:text>Author: </xsl:text></b>
		<xsl:apply-templates/><br/>
    </xsl:template>

    <xsl:template match="l">
<br/><xsl:apply-templates/>
    </xsl:template>

    <xsl:template match="lg">
<tooltip>
		<xsl:apply-templates/>
||<xsl:value-of select="@n" />||
<xsl:variable name="myvar" select="@n" />
<tooltip-content>
            <xsl:value-of select="$myvar"/>
<xsl:value-of select="//app[@loc=$myvar]" />
</tooltip-content>
</tooltip>
    </xsl:template>

    <xsl:template match="app">
	<app><xsl:value-of select="@loc"/><xsl:apply-templates/></app>
    </xsl:template>


    <xsl:template match="lem">
		<lm><xsl:apply-templates/></lm> ] 
<sigla><xsl:value-of select="@wit" /></sigla>;
    </xsl:template>

    <xsl:template match="rdg">
		<xsl:apply-templates/>
	<xsl:value-of select="rdg"/>&#160;<sigla><xsl:value-of select="@wit" /></sigla>
    </xsl:template>


    <xsl:template match="div[@type='apparatus']">
<br/><br/><br/>
===========Apparatus==========
<br/><br/><br/>
		<xsl:apply-templates/>

    </xsl:template>




<!--
https://stackoverflow.com/questions/13422008/what-we-mean-by-this-xsl-notation-xsltemplate-match-node  :
"
/|@*|node() is a match pattern composed of three single patterns. / matches a root node, also called document node, @* matches any attribute node and node() as a pattern "matches any node other than an attribute node and the root node". So for any kind of node (as those three patterns describe all types of nodes) the template says <xsl:apply-templates select="@*|node()"/> which means process the union of the attribute nodes and the child nodes. Document nodes matched by / don't have attribute nodes and attributes don't have them either but as a compact way you often see templates like that. "
-->



</xsl:stylesheet>
