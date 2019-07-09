#!/bin/sh

#echo 's/'$1'/'$2'/g'
sed -i 's/'$1'/'$2'/g' ./content/pages/fr/*.md ./content/pages/*.md
