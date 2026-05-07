import os

def generate_pocket_beat(output_path):
    print("🥁 Mixing: Cleaning the low-end and spacing the rhythm...")
    
    # 1. Cleaner 808 (Lowered volume, shortened for more 'bounce')
    bass = 'sine=f=55:d=0.15,afade=t=out:st=0.1:d=0.05,volume=6dB'
    
    # 2. Wide Trap Clap (Staggered for 'slop')
    c1 = 'anoisesrc=d=0.08:c=white,highpass=f=1200,volume=8dB,adelay=20|20'
    c2 = 'anoisesrc=d=0.1:c=white,highpass=f=1000,volume=10dB,adelay=35|35'
    
    # 3. Rhythmic Hats (1/8th notes with a 'swing' feel)
    hats = 'sine=f=8000:d=0.02,afade=t=out:st=0.01:d=0.01,volume=3dB'
    
    # 4. Arrangement: Bass drops on the 1, Clap on the 3
    filter_str = (
        "[0]aloop=loop=60:size=0.5*44100[h]; " # 8th note hats
        "[1]aloop=loop=7:size=4.0*44100,adelay=0|0[b]; " # Bass on the 1 every 4s
        "[2][3]amix=inputs=2[clap_raw]; [clap_raw]aloop=loop=7:size=4.0*44100,adelay=2000|2000[c]; " # Clap on the 3
        "[h][b][c]amix=inputs=3"
    )
    
    cmd = (
        f"ffmpeg -hide_banner -loglevel error "
        f"-f lavfi -i '{hats}' -f lavfi -i '{bass}' "
        f"-f lavfi -i '{c1}' -f lavfi -i '{c2}' "
        f"-filter_complex \"{filter_str}\" "
        f"'{output_path}' -y"
    )
    os.system(cmd)

if __name__ == '__main__':
    output_path = "/Volumes/12121231/heartmula/outputs/HeartMuLa_V23.mp3"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    generate_pocket_beat(output_path)
    if os.path.exists(output_path):
        print("--- Playing: HeartMuLa_V23 (Pocket Mix) ---")
        os.system(f"afplay '{output_path}'")
