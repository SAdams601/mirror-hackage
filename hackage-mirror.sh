#!/bin/sh

echo "Cleaning up..."
rm 00-index.tar.gz
mkdir -p package
echo "Downloading index..."
wget http://hackage.haskell.org/packages/archive/00-index.tar.gz
for splitpk in `tar tf 00-index.tar.gz | cut -d/ -f 2,3`; do
	pk=`echo $splitpk | sed 's|/|-|'`
	name=$pk.tar.gz
#   echo $splitpk
#   echo $name
   url=http://hackage.haskell.org/package/$splitpk/$name
   echo $url
	if [ ! -a package/$name ]
     then
	      wget $url -O package/$name
	fi
done
