import os
import subprocess

def generate_real_trap(output_path):
    print("🔥 Rendering V36.1: Escaping Shell Characters & Fixing 808s...")
    
    # 1. Gritty 808 with sliding frequency
    bass = "aevalsrc='0.6*sin(2*PI*(60-5*t)*t)':d=0.5,lowpass=f=120,acrusher=level_in=1:level_out=1:bits=8:mode=log,volume=15dB"
    
    # 2. Dark Piano (C# -> D)
    piano = "aevalsrc='(0.2*sin(2*PI*277*t)+0.1*sin(2*PI*554*t))*exp(-2*t)*between(t,0,2)+(0.2*sin(2*PI*293*t)+0.1*sin(2*PI*587*t))*exp(-2*(t-2))*between(t,2,4)':d=4"
    
    # 3. Percussion
    hats = "anoisesrc=d=0.01:c=white,highpass=f=8000,volume=2dB"
    clap = "anoisesrc=d=0.08:c=white,bandpass=f=1200:width_type=h:width=500,volume=18dB"
    
    # 4. Arrangement Logic
    filter_str = (
        "[0:a]aloop=loop=60:size=0.42*44100,volume=0.3[h]; "
        "[1:a]aloop=loop=15:size=1.71*44100,volume=2.5[b]; "
        "[2:a]aloop=loop=7:size=3.42*44100,adelay=1710|1710,volume=2.0[c]; "
        "[3:a]aloop=loop=7:size=3.42*44100,volume=2.5,aecho=0.8:0.9:60:0.4[p]; "
        "[h][b][c][p]amix=inputs=4:duration=first,highpass=f=40,lowpass=f=15000"
    )
    
    # Using subprocess.run for safer shell execution on iMac
    cmd = [
        "ffmpeg", "-hide_banner", "-loglevel", "error",
        "-f", "lavfi", "-i", hats,
        "-f", "lavfi", "-i", bass,
        "-f", "lavfi", "-i", clap,
        "-f", "lavfi", "-i", piano,
        "-filter_complex", filter_str,
        output_path, "-y"
    ]
    
    subprocess.run(cmd)

if __name__ == '__main__':
    output_path = "/Volumes/12121231/heartmula/outputs/HeartMuLa_V36_1.mp3"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    generate_real_trap(output_path)
    if os.path.exists(output_path):
        print("--- Playing: HeartMuLa_V36.1 (No Shell Errors) ---")
        os.system(f"afplay '{output_path}'")
