#!/bin/bash
cowsay "Start Database Migration of $1"
cd $1
echo "cargando variables de $2"
sed -i 's/\r//g' $2
cat $2
export $(grep -v '^#' $2 | xargs -d '\n')

python3 manage.py migrate

cowsay "End Database Migration $1"
