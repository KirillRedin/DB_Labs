<?xml version="1.0" encoding="utf-16"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <meta charset="utf-8"/>
        <html>
            <body>
                <table border="1">
                    <xsl:for-each select="root/data/product">
                        <tr>
                            <td><xsl:value-of select="name"/></td>
                            <td><xsl:value-of select="price"/></td>
                            <td>
                            <img>
                                <xsl:attribute name="src">
                                    <xsl:value-of select="image"/>
                                </xsl:attribute>
                            </img>
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>