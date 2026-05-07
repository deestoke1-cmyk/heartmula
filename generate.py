import os

def generate_melodic_beat(output_path):
    print("🔥 Rendering Balanced Trap + Soft Melody...")
    
    # 1. Balanced 808 (90Hz)
    bass = 'sine=f=90:d=2,volume=5dB'
    
    # 2. Clean Snares
    snare1 = 'anoisesrc=d=0.1:c=white,volume=8dB,adelay=500|500'
    snare2 = 'anoisesrc=d=0.1:c=white,volume=8dB,adelay=1500|1500'
    
    # 3. Soft Melody (Lowered volume and higher pitch for clarity)
    # Notes: A, B, C, D (440Hz, 493Hz, 523Hz, 587Hz)
    m1 = 'sine=f=440:d=0.2,afade=t=out:st=0.1:d=0.1,adelay=0|0,volume=3dB'
    m2 = 'sine=f=493:d=0.2,afade=t=out:st=0.1:d=0.1,adelay=250|250,volume=3dB'
    m3 = 'sine=f=523:d=0.2,afade=t=out:st=0.1:d=0.1,adelay=1000|1000,volume=3dB'
    m4 = 'sine=f=587:d=0.2,afade=t=out:st=0.1:d=0.1,adelay=1250|1250,volume=3dB'
    
    # Mix: Bass(0), Snare1(1), Snare2(2), Melodies(3,4,5,6)
    filter_str = '[3][4][5][6]amix=inputs=4[mel]; [0][1][2][mel]amix=inputs=4'
    
    cmd = (
        f"ffmpeg -hide_banner -loglevel error "
        f"-f lavfi -i '{bass}' "
        f"-f lavfi -i '{snare1}' "
        f"-f lavfi -i '{snare2}' "
        f"-f lavfi -i '{m1}' -f lavfi -i '{m2}' -f lavfi -i '{m3}' -f lavfi -i '{m4}' "
        f"-filter_complex '{filter_str}' "
        f"'{output_path}' -y"
    )
    os.system(cmd)

if __name__ == '__main__':
    output_path = "/Volumes/12121231/heartmula/outputs/Melodic_Beat.mp3"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    generate_melodic_beat(output_path)
    
    if os.path.exists(output_path):
        print(f"--- Playing: Melodic_Beat.mp3 ---")
        os.system(f"afplay '{output_path}'")
