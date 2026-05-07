import os

def generate_heavy_beat(output_path):
    print("🔊 Mixing V26: Forcing Bass Dominance...")
    
    # 1. Hi-Hats: Thinned and attenuated
    hats = 'sine=f=8000:d=0.01,afade=t=out:st=0.005:d=0.005,volume=0.5dB'
    
    # 2. 808 Bass: Fundamental frequency at 50Hz for that 'thump'
    bass = 'sine=f=50:d=0.3,afade=t=out:st=0.1:d=0.2,volume=20dB'
    
    # 3. Trap Clap: Staggered and bright
    clap = 'anoisesrc=d=0.1:c=white,highpass=f=1000,volume=15dB'
    
    # 4. Filter Complex: Normalize levels before mixing
    # [0:a] is hats, [1:a] is bass, [2:a] is clap
    filter_str = (
        "[0:a]aloop=loop=30:size=1.0*44100,volume=0.2[h]; "
        "[1:a]aloop=loop=7:size=4.0*44100,volume=2.5[b]; "
        "[2:a]aloop=loop=7:size=4.0*44100,adelay=2000|2000,volume=1.8[c]; "
        "[h][b][c]amix=inputs=3:duration=first:dropout_transition=0,volume=2.0"
    )
    
    cmd = (
        f"ffmpeg -hide_banner -loglevel error "
        f"-f lavfi -i '{hats}' -f lavfi -i '{bass}' -f lavfi -i '{clap}' "
        f"-filter_complex \"{filter_str}\" "
        f"'{output_path}' -y"
    )
    os.system(cmd)

if __name__ == '__main__':
    output_path = "/Volumes/12121231/heartmula/outputs/HeartMuLa_V26.mp3"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    generate_heavy_beat(output_path)
    if os.path.exists(output_path):
        print("--- Playing: HeartMuLa_V26 (Bass Priority) ---")
        os.system(f"afplay '{output_path}'")
