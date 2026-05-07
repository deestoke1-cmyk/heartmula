import os

def generate_trap_drums(output_path):
    print("🥁 Rendering V19: Layered Snare & Rhythmic Hats...")
    
    # 1. The 808 Bass (Lowered to 60Hz for more sub)
    bass = 'sine=f=60:d=0.3,afade=t=out:st=0.1:d=0.2,volume=10dB'
    
    # 2. Layered Snare (The 'Crack' + The 'Body')
    snare_body = 'sine=f=180:d=0.1,afade=t=out:st=0.05:d=0.05,volume=10dB'
    snare_crack = 'anoisesrc=d=0.1:c=white,highpass=f=2000,volume=8dB'
    
    # 3. Metallic Hats (1/8th note rhythm with volume swing)
    hats = 'sine=f=8000:d=0.02,afade=t=out:st=0.01:d=0.01,tremolo=f=4:d=0.4,volume=5dB'
    
    # 4. Sequencing Logic
    filter_str = (
        "[0]aloop=loop=60:size=0.5*44100[h]; "   # 1/8th hats
        "[1]aloop=loop=15:size=2*44100,adelay=1000|1000[b]; " # 808 on the 1
        "[2][3]amix=inputs=2[s_raw]; [s_raw]aloop=loop=15:size=2*44100,adelay=2000|2000[s]; " # Snare on the 2
        "[h][b][s]amix=inputs=3"
    )
    
    cmd = (
        f"ffmpeg -hide_banner -loglevel error "
        f"-f lavfi -i '{hats}' -f lavfi -i '{bass}' "
        f"-f lavfi -i '{snare_body}' -f lavfi -i '{snare_crack}' "
        f"-filter_complex \"{filter_str}\" "
        f"'{output_path}' -y"
    )
    os.system(cmd)

if __name__ == '__main__':
    output_path = "/Volumes/12121231/heartmula/outputs/HeartMuLa_V19.mp3"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    generate_trap_drums(output_path)
    if os.path.exists(output_path):
        print("--- Playing: HeartMuLa_V19 (Drums) ---")
        os.system(f"afplay '{output_path}'")
