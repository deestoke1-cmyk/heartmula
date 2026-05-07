import os

def generate_slow_clap_beat(output_path):
    print("👏 Rendering V21: Slow Half-Time Claps...")
    
    # 1. Triple-Layer Clap (Same texture, slower timing)
    c1 = 'anoisesrc=d=0.08:c=white,highpass=f=1000,volume=8dB,adelay=0|0'
    c2 = 'anoisesrc=d=0.08:c=white,highpass=f=1200,volume=6dB,adelay=10|10'
    c3 = 'anoisesrc=d=0.1:c=white,highpass=f=800,volume=10dB,adelay=20|20'
    
    # 2. Foundation (808 & Hats)
    bass = 'sine=f=60:d=0.3,afade=t=out:st=0.1:d=0.2,volume=10dB'
    hats = 'sine=f=8000:d=0.02,afade=t=out:st=0.01:d=0.01,tremolo=f=4:d=0.4,volume=5dB'
    
    # 3. Sequencing Logic (Changing loop size to 4.0 for half-time)
    filter_str = (
        "[0]aloop=loop=60:size=0.5*44100[h]; "
        "[1]aloop=loop=15:size=2*44100,adelay=1000|1000[b]; "
        "[2][3][4]amix=inputs=3[clap_raw]; [clap_raw]aloop=loop=7:size=4.0*44100,adelay=2000|2000[c]; "
        "[h][b][c]amix=inputs=3"
    )
    
    cmd = (
        f"ffmpeg -hide_banner -loglevel error "
        f"-f lavfi -i '{hats}' -f lavfi -i '{bass}' "
        f"-f lavfi -i '{c1}' -f lavfi -i '{c2}' -f lavfi -i '{c3}' "
        f"-filter_complex \"{filter_str}\" "
        f"'{output_path}' -y"
    )
    os.system(cmd)

if __name__ == '__main__':
    output_path = "/Volumes/12121231/heartmula/outputs/HeartMuLa_V21.mp3"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    generate_slow_clap_beat(output_path)
    if os.path.exists(output_path):
        print("--- Playing: HeartMuLa_V21 (Slow Claps) ---")
        os.system(f"afplay '{output_path}'")
