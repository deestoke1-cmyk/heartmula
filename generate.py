import os

def generate_universal_beat(output_path):
    print("🔊 Rendering V29: Universal 808 Logic (No 'pitch' filter)...")
    
    # 1. 808 Bass: Start with a 440Hz tone and down-sample it to 
    # create a massive low-end thud (approx 60Hz)
    bass = "sine=f=440:d=0.3,asetrate=6000,aresample=44100,volume=18dB"
    
    # 2. Percussion (Keep it thin and sharp)
    hats = 'sine=f=8000:d=0.01,volume=1dB'
    clap = 'anoisesrc=d=0.1:c=white,highpass=f=1000,volume=15dB'
    
    # 3. Mixing Logic: Heavy on the bass [1], tucked hats [0], and claps [2]
    filter_str = (
        "[0:a]aloop=loop=30:size=1.0*44100,volume=0.2[h]; "
        "[1:a]aloop=loop=15:size=2.0*44100,volume=2.2[b]; "
        "[2:a]aloop=loop=7:size=4.0*44100,adelay=2000|2000,volume=1.8[c]; "
        "[h][b][c]amix=inputs=3:duration=first"
    )
    
    cmd = (
        f"ffmpeg -hide_banner -loglevel error "
        f"-f lavfi -i '{hats}' -f lavfi -i '{bass}' -f lavfi -i '{clap}' "
        f"-filter_complex \"{filter_str}\" "
        f"'{output_path}' -y"
    )
    os.system(cmd)

if __name__ == '__main__':
    output_path = "/Volumes/12121231/heartmula/outputs/HeartMuLa_V29.mp3"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    generate_universal_beat(output_path)
    if os.path.exists(output_path):
        print("--- Playing: HeartMuLa_V29 (Compatible Build) ---")
        os.system(f"afplay '{output_path}'")
