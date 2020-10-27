mkdir -p videos/turntable_frames
# "-y" overwrites output
# "-ss 25" skips first 25 seconds of input
# "-i videos/IMGP4365.AVI" chooses the input
# "-frames:v 2220" limits output to 2220 frames
# "videos/turntable_%04d.jpeg" names the output jpeg frames
ffmpeg -y -ss 25 -i videos/IMGP4365.AVI -frames:v 2220 -ac 0 videos/turntable_frames/turntable_%04d.png
