��#� �B�r�a�i�l�l�e�y�e�
�
�

running mobile camera integration from command line (so far)
raspberry pi: package used = motion
phone app: ip webcam

1. start live server session on ip webcam
2. run command 'sudo service motion start' on terminal
3. go to the IP address listed on ip webcam
4. switch video renderer to browser (for now)


INTEGRATION BETWEEN MEW AND KRABBY:
- sshpass module downloaded: sudo apt-get install sshpass
- sending file straight in terminal from mew to krabby: scp /home/pi/readDot/software/textfile pi@ipaddress:/home/pi/readdot
- bypassing ssh into other pi: sshpass -p "r00t" ssh -o StrictHostKeyChecking=no pi@ipaddress 
----------------------- ssh and transferring files from mew to krabby ---------------------------------
run "sshpass -p "r00t" scp /home/pi/readDot/software/textfile pi@ipaddress:/home/pi/readdot
