import os
import subprocess
import time

VIDEOS_DIR = "/home/ubuntu/pelis"
STREAM_KEY = "La Key"
RTMP_URL = f"rtmp://live.twitch.tv/app/{STREAM_KEY}"

def stream_video(video_path):
    filename = os.path.basename(video_path)
    print(f"\nTransmitiendo: {filename}")

    command = [
        "ffmpeg",
        "-re",
        "-i", video_path,
        "-r", "30",
        "-vf", "scale=w=1280:h=720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2",
        "-vcodec", "libx264",
        "-preset", "superfast",
        "-maxrate", "2500k",
        "-bufsize", "5000k",
        "-pix_fmt", "yuv420p",
        "-g", "60",
        "-acodec", "aac",
        "-b:a", "128k",
        "-ar", "44100",
        "-ac", "2",
        "-f", "flv",
        RTMP_URL
    ]

    process = subprocess.run(command)
    return process.returncode

def get_video_list():
    allowed_extensions = (".mkv", ".mp4")
    return sorted([
        os.path.join(VIDEOS_DIR, f)
        for f in os.listdir(VIDEOS_DIR)
        if f.lower().endswith(allowed_extensions)
    ])

def main():
    played = set()

    while True:
        all_videos = get_video_list()

        if not all_videos:
            print("No hay películas. Esperando 10 segundos...")
            time.sleep(10)
            continue

        new_videos = [v for v in all_videos if v not in played]

        if not new_videos:
            print("Repetiremos todas las películas desde el principio.")
            played.clear()
            new_videos = all_videos

        for video_path in new_videos:
            ret = stream_video(video_path)
            played.add(video_path)

            if ret != 0:
                print(f"Error al transmitir {os.path.basename(video_path)}.")
            time.sleep(3)

if __name__ == "__main__":
    main()