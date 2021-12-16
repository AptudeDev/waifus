#!/bin/bash
set -v
cowsay "Build project $1"
cd $1
PATH="$PATH:/root/.dotnet/tools"

dotnet build --configuration Release
cowsay "End build project $1"
