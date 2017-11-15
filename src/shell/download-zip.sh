#!/bin/bash
#
#


# load configurations
download_url=$1
download_directory=`cat config.json | jq '.["download-directory"]'|  sed -e 's/^"//' -e 's/"$//'`
majiang_desktop_path=`cat config.json | jq '.["majiang-desktop-path"]' | sed -e 's/^"//' -e 's/"$//'`

if [ "${download_url}"x = "x" ] ; then
    exit 1
fi

if [ ! -e ${download_directory} ] ; then
    mkdir download
fi

cd download

# download file
wget ${download_url}

# unzip and copy to majiang-desktop
find . -name "*.zip"| xargs unzip
projectName=`ls | grep -v 'zip'`

rm -rf ${majiang_desktop_path}/src
rm -rf ${majiang_desktop_path}/res
mv $projectName/res ${majiang_desktop_path}
mv $projectName/src ${majiang_desktop_path}

## replace the UserInfo.lua
## replace the Network.lua
## replace the MainScene.lua

# delete download zip file and mj directory
rm -rf $projectName.zip* $projectName



