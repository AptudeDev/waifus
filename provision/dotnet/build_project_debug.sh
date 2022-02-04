#!/bin/bash
set -v
cowsay "Build project $1"
cd $1
echo "cargando variables de $2"
cat $2
export $(grep -v '^#' $2 | xargs -d '\n')
PATH="$PATH:/root/.dotnet/tools"

dotnet build --configuration Debug
cowsay "End build project $1"
