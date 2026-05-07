import argparse
import os

def generate_808(output_path):
    print("🔥 Rendering Aggressive 808...")
    # Simplified FFmpeg command for maximum compatibility
    cmd = (
        f'ffmpeg -hide_banner -loglevel error -f lavfi '
        f'-i "sine=frequency=45:duration=1" '
        f'-af "volume=20dB" '
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
    generate_808(output_path)
    
    if os.path.exists(output_path):
        print(f"--- Playing: {output_audio} ---")
        os.system(f"afplay '{output_path}'")
