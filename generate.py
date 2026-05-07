import argparse
import os

def generate_trap_beat(output_path):
    print("🔥 Rendering Full Trap Loop (808 + Hats + Snare)...")
    
    # 1. The Heavy 808
    bass = 'sine=frequency=45:duration=1,volume=20dB'
    
    # 2. The Hi-Hat Triplets
    hats = 'anoisesrc=d=1:c=white,tremolo=f=12:d=0.9,volume=5dB'
    
    # 3. The Snare (White noise burst on the half-second mark)
    snare = 'anoisesrc=d=0.1:c=white,volume=15dB,adelay=500|500'
    
    # Mix all 3 layers
    cmd = (
        f'ffmpeg -hide_banner -loglevel error -f lavfi -i "{bass}" '
        f'-f lavfi -i "{hats}" -f lavfi -i "{snare}" '
        f'-filter_complex "amix=inputs=3" '
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
    generate_trap_beat(output_path)
    
    if os.path.exists(output_path):
        print(f"--- Playing: {output_audio} ---")
        os.system(f"afplay '{output_path}'")
