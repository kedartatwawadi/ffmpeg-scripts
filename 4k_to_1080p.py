import os
import subprocess
import argparse


def main():
    parser = argparse.ArgumentParser(description="Crop video files to the duration specified")
    parser.add_argument("--dir", type=str, help="input dir path")
    parser.add_argument("--ext", type=str, default="y4m", help="extension of videos")

    args = parser.parse_args()
    list_files = os.listdir(args.dir)

    output_list = []
    for filename in list_files:
        # check for.yuv extension
        _temp = filename.split(".")
        assert len(_temp) == 2, "only one . allowed in filename"
        base_name, ext = _temp
        if ext == "mov":
            # write output name
            output_name = base_name + f"_1080p.{args.ext}"
            print(f"{filename}, {output_name}")
            filepath = os.path.join(args.dir, filename)
            output_path = os.path.join(args.dir, output_name)
            output_list.append((filepath, output_path))
    
    for filename, output_name in output_list:
        scale_option = "-vf scale=1920x1080:flags=lanczos"
        cmd = f"ffmpeg -i {filename} {scale_option} {output_name}"
        print(cmd)
        subprocess.run(
            cmd, shell=True
        )


if __name__ == "__main__":
    main()
