import subprocess

def capture_audio():
    command = "rtl_fm -f 162.400M -s 22050 -g 48 - | sox -t raw -r 22050 -es -b 16 -c 1 -V1 - emergency.wav"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    capture_audio()
