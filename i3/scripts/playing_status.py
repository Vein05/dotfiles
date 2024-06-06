import subprocess

command = 'playerctl metadata --format "Now playing: {{ title }} "'
#"| Remaining: {{ duration(mpris:length - position) }}"'
try:
    output = subprocess.check_output(command, shell=True)
    now_playing = output.decode("utf-8")
    print (now_playing[:100])
except:
    pass
