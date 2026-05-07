import argparse
import os

def generate_full_beat(output_path):
    print("🔥 Rendering Atmospheric Trap Beat (808 + Hats + Snare + Melody)...")
    
    # 1. The Heavy 808
    bass = 'sine=frequency=45:duration=1,volume=20dB'
    
    # 2. The Hi-Hat Triplets
    hats = 'anoisesrc=d=1:c=white,tremolo=f=12:d=0.9,volume=5dB'
    
    # 3. The Snare
    snare = 'anoisesrc=d=0.1:c=white,volume=15dB,adelay=500|500'
    
    # 4. The Melody (4 separate plucky notes)
    n1 = 'sine=f=440:d=0.2,afade=t=out:st=0.1:d=0.1,adelay=0|0'
    n2 = 'sine=f=466:d=0.2,afade=t=out:st=0.1:d=0.1,adelay=250|250'
    n3 = 'sine=f=349:d=0.2,afade=t=out:st=0.1:d=0.1,adelay=500|500'
    n4 = 'sine=f=329:d=0.2,afade=t=out:st=0.1:d=0.1,adelay=750|750'
    
    cmd = (
        f'ffmpeg -hide_banner -loglevel error '
        f'-f lavfi -i "{bass}" '
        f'-f lavfi -i "{hats}" '
        f'-f lavfi -i "{snare}" '
        f'-f lavfi -i "{n1}" -f lavfi -i "{n2}" -f lavfi -i "{n3}" -f lavfi -i "{n4}" '
        f'-filter_complex "amix=inputs=7" '
        f'"{output_path}" -y'
    )
    os.system(cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--style', type=str, default='Aggressive Trap')
    args = parser.parse_args()

    output_audio = f"{args.style.replace(' ', '_')}_Beat.mp3"
    output_path = f"/Volumes/12121231/heartmula/outputs/{output_audio}"
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    generate_full_beat(output_path)
    
    if os.path.exists(output_path):
        print(f"--- Playing: {output_audio} ---")
        os.system(f"afplay '{output_path}'")
