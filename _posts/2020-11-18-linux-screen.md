# screen

    screen -ls 

    screen -r 1332
    
    ctrl a d            -> detach window


--

    pi@raspberrypi-3d-1:~ $ screen -ls
    There are screens on:
	    29473.pts-0.raspberrypi-3d-1	(27/08/20 15:27:10)	(Detached)
	    2190.pts-4.raspberrypi-3d-1	(25/07/20 01:06:57)	(Detached)
	    1968.pts-2.raspberrypi-3d-1	(25/07/20 00:49:40)	(Detached)
	    1334.pts-0.raspberrypi-3d-1	(24/07/20 21:57:06)	(Detached)
    4 Sockets in /run/screen/S-pi.
    pi@raspberrypi-3d-1:~ $ screen -r 1334
    [detached from 1334.pts-0.raspberrypi-3d-1]

## linux screen Cheat sheet 

<https://gist.github.com/bhurlow/3043629> 


