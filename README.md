RainbowReader MKII

The backend on this version has been redesigned to work with Flask. This will reduce operating costs, and with the added scheduler will eliminate lengthy load times. 

Currently there is 1 known bug:

If you type in a different URL (i.e. switching from /#news to /#technology) - this will not result in change. This is due to the nature of using '#', anchors, to differentiate between 'pages'. This was assumed to be an edge case so was not dealt with in this build session. If this becomes a major conern, a fix can be implemented.