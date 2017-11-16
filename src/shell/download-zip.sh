#!/bin/bash
#
#

PATH=/usr/local/bin/:$PATH

# load configurations
download_url=$1
download_directory=`cat config.json | jq '.["download-directory"]'|  sed -e 's/^"//' -e 's/"$//'`
majiang_desktop=`cat config.json | jq '.["majiang-desktop-path"]' | sed -e 's/^"//' -e 's/"$//'`

if [ "${download_url}"x = "x" ] ; then
    exit 1
fi

if [ ! -e ${download_directory} ] ; then
    mkdir download
fi

cd download

# download file
wget -q ${download_url}

# unzip and copy to majiang-desktop
find . -name "*.zip"| xargs unzip --qq
projectName=`ls | grep -v 'zip' | sed -e 's/^"//' -e 's/"$//'`

rm -rf ${majiang_desktop}/src
rm -rf ${majiang_desktop}/res

mv $projectName/encrypt/res ${majiang_desktop}
mv $projectName/encrypt/src ${majiang_desktop}

## replace the UserInfo.lua
## replace the Network.lua
## replace the MainScene.lua
## create userif.lua
echo "return \"110\"" > ${majiang_desktop}/src/userid.lua

# delete download zip file and mj directory
rm -rf *.zip* $projectName

echo "Deploy Done!!!!"



