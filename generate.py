import os

def generate_crisp_snare_beat(output_path):
    print("🥁 Engineering: Layering Snare 'Body' and 'Crack'...")
    
    # 1. The New Snare: Layering a 180Hz pop with high-frequency noise
    # sine=f=180 is the 'thump', anoisesrc is the 'snap'
    snare_body = 'sine=f=180:d=0.1,afade=t=out:st=0.05:d=0.05,volume=10dB'
    snare_crack = 'anoisesrc=d=0.1:c=white,highpass=f=2000,volume=8dB'
    snare_final = f"[in_s1][in_s2]amix=inputs=2,volume=12dB"

    # 2. Other elements (Keep them subtle)
    hats = 'sine=f=6000:d=0.02,afade=t=out:st=0.01:d=0.01,volume=3dB'
    bass = 'sine=f=90:d=0.2,afade=t=out:st=0.1:d=0.1,volume=8dB'
    m1 = 'sine=f=440:d=0.1,afade=t=out:st=0.05:d=0.05,volume=2dB'
    
    # 3. Sequencing (Slow 1/4 note rhythm)
    filter_str = (
        "[0]aloop=loop=30:size=1.0*44100[h]; "
        "[1]aloop=loop=30:size=1.0*44100[mel]; "
        "[2]aloop=loop=15:size=2*44100,adelay=2000|2000[b]; "
        "[3][4]amix=inputs=2[snare_mix]; [snare_mix]aloop=loop=15:size=2*44100,adelay=2500|2500[s]; "
        "[h][mel][b][s]amix=inputs=4"
    )
    
    cmd = (
        f"ffmpeg -hide_banner -loglevel error "
        f"-f lavfi -i '{hats}' -f lavfi -i '{m1}' "
        f"-f lavfi -i '{bass}' -f lavfi -i '{snare_body}' -f lavfi -i '{snare_crack}' "
        f"-filter_complex \"{filter_str}\" "
        f"'{output_path}' -y"
    )
    os.system(cmd)

if __name__ == '__main__':
    output_path = "/Volumes/12121231/heartmula/outputs/Crisp_Snare_V17.mp3"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    generate_crisp_snare_beat(output_path)
    if os.path.exists(output_path):
        os.system(f"afplay '{output_path}'")
