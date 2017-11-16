#!/bin/bash

resolution="600x400"
win1="100,50"
win2="850,50"
win3="100,500"
win4="850,500"


if [ "$1"x = "1"x ] ; then
    open -n /Applications/majiang-desptop.app --args -resolution $resolution -position $win1
elif [ "$1"x = "2"x ] ; then
    open -n /Applications/majiang-desptop.app --args -resolution $resolution -position $win2
    open -n /Applications/majiang-desptop.app --args -resolution $resolution -position $win3
elif [ "$1"x = "3"x ] ; then
    open -n /Applications/majiang-desptop.app --args -resolution $resolution -position $win2
    open -n /Applications/majiang-desptop.app --args -resolution $resolution -position $win3
    open -n /Applications/majiang-desptop.app --args -resolution $resolution -position $win4
elif [ "$1"x = "4"x ] ; then
    open -n /Applications/majiang-desptop.app --args -resolution $resolution -position $win1
    open -n /Applications/majiang-desptop.app --args -resolution $resolution -position $win2
    open -n /Applications/majiang-desptop.app --args -resolution $resolution -position $win3
    open -n /Applications/majiang-desptop.app --args -resolution $resolution -position $win4
fi

