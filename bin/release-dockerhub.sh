#!/bin/bash

docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_API_KEY

VERSION=`python setup.py --version`
echo "Building $VERSION"
docker build -t code-video-generator:$VERSION --build-arg VERSION=$VERSION .
docker tag code-video-generator:$VERSION mrdonbrown/code-video-generator:$VERSION
docker tag code-video-generator:$VERSION mrdonbrown/code-video-generator:latest

echo "Pushing $VERSION"
docker push mrdonbrown/code-vide-generator:$VERSION
docker push mrdonbrown/code-vide-generator:latest