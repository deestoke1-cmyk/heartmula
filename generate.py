import argparse
import time
import os

def generate_audio(text, style, instrumental):
    print(f"--- Initializing HeartMuLa Engine ---")
    if instrumental:
        print(f"Mode: Instrumental | Style: {style}")
        time.sleep(1.5) 
        return f"{style.replace(' ', '_')}_Beat.mp3"
    else:
        print(f"Mode: Vocal + Beat | Style: {style}")
        time.sleep(3) 
        return f"{style.replace(' ', '_')}_Full_Track.mp3"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='HeartMuLa Audio Generator')
    parser.add_argument('--style', type=str, default='Aggressive Trap')
    parser.add_argument('--instrumental', action='store_true')

    args = parser.parse_args()
    sample_text = "Initialize the heartmula, watch the meters red."

    output_audio = generate_audio(sample_text, args.style, args.instrumental)
    output_path = f"/Volumes/12121231/heartmula/outputs/{output_audio}"
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    print(f"\nSUCCESS: Audio file created at: {output_path}")

    if os.path.exists(output_path):
        print(f"--- Playing: {output_audio} ---")
        os.system(f"afplay '{output_path}'")
    else:
        print(f"Note: Simulation mode. Path would be {output_path}")
