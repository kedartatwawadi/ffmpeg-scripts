#!/bin/zsh
echo "Filename,PixelWidth,PixelHeight,DisplayRatio,Bitrate,FrameRate,Duration"
find $1 -type f | grep -i \.mkv | while read movie;do
echo -n "$movie,"
mediainfo --Inform="Video;%Width%,%Height%,%DisplayAspectRatio/String%,%BitRate%,%FrameRate%, %Duration%" $movie
done
