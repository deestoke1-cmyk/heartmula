import argparse
import os

def generate_trap_beat(output_path):
    print("🔥 Rendering Aggressive Trap Bounce...")
    
    # 1. The Heavy 808 (45Hz deep bass)
    bass = 'sine=frequency=45:duration=1,volume=20dB'
    
    # 2. The Hi-Hat Triplets (White noise with a fast 12Hz pulse)
    hats = 'anoisesrc=d=1:c=white,tremolo=f=12:d=0.9,volume=5dB'
    
    # Mix them together into one track
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

    # Routing to your external drive
    output_audio = f"{args.style.replace(' ', '_')}_Beat.mp3"
    output_path = f"/Volumes/12121231/heartmula/outputs/{output_audio}"
    
    # Create folder if it's missing
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Run the engine
    generate_trap_beat(output_path)
    
    if os.path.exists(output_path):
        print(f"--- Playing: {output_audio} ---")
        # Play directly on your iMac
        os.system(f"afplay '{output_path}'")
