#!/bin/bash

DOMAINS="ulearn ulearn5.upc"
LANGUAGES="ca es en"

for domain in $DOMAINS
do
  for language in $LANGUAGES
  do
    if [ -f "$language/LC_MESSAGES/$domain.mo" ]
    then
      msgfmt -o $language/LC_MESSAGES/$domain.mo  $language/LC_MESSAGES/$domain.po
    fi
  done
done
