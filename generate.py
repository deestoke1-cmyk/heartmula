import os

def generate_humanized_beat(output_path):
    print("🔥 Rendering V18: Fixed Humanized Rhythm & Dynamic Mixing...")
    
    # 1. Humanized Hats (Randomized volume for 'swing' feel)
    hats = 'sine=f=6000:d=0.02,afade=t=out:st=0.01:d=0.01,tremolo=f=4:d=0.5,volume=4dB'
    
    # 2. Punchy 808 Bass
    bass = 'sine=f=90:d=0.2,afade=t=out:st=0.1:d=0.1,volume=8dB'
    
    # 3. Layered Snare (Body + Crack)
    snare_body = 'sine=f=180:d=0.1,afade=t=out:st=0.05:d=0.05,volume=10dB'
    snare_crack = 'anoisesrc=d=0.1:c=white,highpass=f=2000,volume=8dB'
    
    # 4. Sequencing with Variation
    filter_str = (
        "[0]aloop=loop=30:size=1.0*44100[h]; "   
        "[1]aloop=loop=15:size=2*44100,adelay=2000|2000[b]; " 
        "[2][3]amix=inputs=2[s_raw]; [s_raw]aloop=loop=15:size=2*44100,adelay=2500|2500[s]; "
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
    output_path = "/Volumes/12121231/heartmula/outputs/HeartMuLa_V18.mp3"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    generate_humanized_beat(output_path)
    if os.path.exists(output_path):
        print("--- Playing: HeartMuLa_V18.mp3 ---")
        os.system(f"afplay '{output_path}'")
