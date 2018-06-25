#!/bin/bash

LANGUAGES="ca es en"

for language in $LANGUAGES
do
if [ -f "$language/LC_MESSAGES/ulearn5.upc.mo" ]
then
  msgfmt -o $language/LC_MESSAGES/ulearn5.upc.mo  $language/LC_MESSAGES/ulearn5.upc.po
fi
done
