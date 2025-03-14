#!/bin/bash
# −∗− shell−script −∗−

echo "Content-type: text:html"

echo "Mon script CGI"

echo "<br/>"

echo $QUERY_STRING

echo "Fin query_string"

echo "<br/>"

NOM = $(echo $QUERY_STRING | cut -d"=" -f2)

echo $NOM

echo "<br/>"