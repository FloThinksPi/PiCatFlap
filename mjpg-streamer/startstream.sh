sudo killall mjpg_streamer > /dev/null 2>&1
sudo killall raspistill > /dev/null 2>&1

export LD_LIBRARY_PATH=/home/pi/mjpg-streamer/mjpg-streamer-experimental
nice -n 2 /home/pi/mjpg-streamer/mjpg-streamer-experimental/mjpg_streamer -o "output_http.so -p 9000 -c pi:123" -i "input_raspicam.so -q 30 -x 640 -y 360 -fps 8 -ex night -br 55 -sh 50 -ev 10" > /dev/null 2>&1 &
