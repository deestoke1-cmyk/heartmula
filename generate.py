import os

def generate_final_beat(output_path):
    print("🚀 Finalizing Arrangement: Intro -> Drop -> Outro...")
    
    # Sound Definitions
    bass = 'sine=f=90:d=2,volume=5dB'
    snare = 'anoisesrc=d=0.1:c=white,volume=8dB,adelay=500|500'
    m1 = 'sine=f=440:d=0.2,afade=t=out:st=0.1:d=0.1,adelay=0|0,volume=10dB'
    m2 = 'sine=f=493:d=0.2,afade=t=out:st=0.1:d=0.1,adelay=250|250,volume=10dB'
    
    # Logic: 4-bar intro, then 8-bar drop, 4-bar outro
    filter_str = (
        "[0][1]amix=inputs=2,aloop=loop=15:size=2*44100[music]; "
        "[2]aloop=loop=7:size=2*44100,adelay=8000|8000[drums_b]; "
        "[3]aloop=loop=7:size=2*44100,adelay=8000|8000[drums_s]; "
        "[music][drums_b][drums_s]amix=inputs=3"
    )
    
    cmd = (
        f"ffmpeg -hide_banner -loglevel error "
        f"-f lavfi -i '{m1}' -f lavfi -i '{m2}' "
        f"-f lavfi -i '{bass}' -f lavfi -i '{snare}' "
        f"-filter_complex \"{filter_str}\" "
        f"'{output_path}' -y"
    )
    os.system(cmd)

if __name__ == '__main__':
    output_path = "/Volumes/12121231/heartmula/outputs/HeartMuLa_V12.mp3"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    generate_final_beat(output_path)
    if os.path.exists(output_path):
        print(f"--- Playing: HeartMuLa_V12.mp3 ---")
        os.system(f"afplay '{output_path}'")
