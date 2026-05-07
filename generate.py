import argparse
import os

def generate_trap_beat(output_path):
    print("🔥 Rendering Aggressive Trap Bounce...")
    
    # 1. The Heavy 808 (45Hz)
    bass = 'sine=frequency=45:duration=1,volume=20dB'
    
    # 2. The Hi-Hat Triplets (White noise with a fast pulse)
    # This creates that "chatter" sound by pulsing white noise every 0.125 seconds
    hats = 'anoisesrc=d=1:c=white,tremolo=f=12:d=0.9,volume=5dB'
    
    # Mix them together
    cmd = (
        f'ffmpeg -hide_banner -loglevel error -f lavfi -i "{bass}" '
        f'-f lavfi -i "{hats}" -filter_complex "amix=inputs=2" '
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
