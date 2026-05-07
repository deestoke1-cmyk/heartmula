import os

def generate_melodic_beat(output_path):
    print("🎹 Rendering V30.1: Fixed Melody Syntax & Phrygian Scale...")
    
    # 1. Dark Melody: C4(261) -> Db4(277) -> G3(195)
    # Removed spaces and used escaped quotes for ffmpeg stability
    melody = "aevalsrc='0.15*sin(2*PI*261.63*t)*between(t,0,0.5)+0.15*sin(2*PI*277.18*t)*between(t,1,1.5)+0.12*sin(2*PI*195.99*t)*between(t,2,3.5)':d=4"
    
    # 2. Foundation
    bass = "sine=f=440:d=0.3,asetrate=6000,aresample=44100,volume=18dB"
    hats = 'sine=f=8000:d=0.01,volume=1dB'
    clap = 'anoisesrc=d=0.1:c=white,highpass=f=1000,volume=15dB'
    
    # 3. Mixing Logic
    filter_str = (
        "[0:a]aloop=loop=30:size=1.0*44100,volume=0.2[h]; "
        "[1:a]aloop=loop=15:size=2.0*44100,volume=2.2[b]; "
        "[2:a]aloop=loop=7:size=4.0*44100,adelay=2000|2000,volume=1.8[c]; "
        "[3:a]aloop=loop=7:size=4.0*44100,volume=1.0,aecho=0.8:0.88:40:0.4[m]; "
        "[h][b][c][m]amix=inputs=4:duration=first"
    )
    
    cmd = (
        f"ffmpeg -hide_banner -loglevel error "
        f"-f lavfi -i '{hats}' -f lavfi -i '{bass}' -f lavfi -i '{clap}' -f lavfi -i \"{melody}\" "
        f"-filter_complex \"{filter_str}\" "
        f"'{output_path}' -y"
    )
    os.system(cmd)

if __name__ == '__main__':
    output_path = "/Volumes/12121231/heartmula/outputs/HeartMuLa_V30_1.mp3"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    generate_melodic_beat(output_path)
    if os.path.exists(output_path):
        print("--- Playing: HeartMuLa_V30.1 (Melodic Fixed) ---")
        os.system(f"afplay '{output_path}'")
