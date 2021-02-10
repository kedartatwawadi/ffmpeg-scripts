import os
import subprocess
import argparse


def main():
    parser = argparse.ArgumentParser(description="Crop video files to the duration specified")
    parser.add_argument("--src", type=str, help="input dir path")
    parser.add_argument("--dst", type=str, help="output dir path")
    parser.add_argument("--ext", type=str, default="y4m", help="extension of videos")

    args = parser.parse_args()
    list_files = os.listdir(args.src)
    print(list_files)
    output_list = []
    for filename in list_files:
        # check for.yuv extension
        _temp = filename.split(".")
        assert len(_temp) == 2, "only one . allowed in filename"
        base_name, ext = _temp
        if ext == args.ext:
            # write output name
            output_name = base_name + f"_img"
            print(f"{filename}, {output_name}")
            filepath = os.path.join(args.src, filename)
            output_path = os.path.join(args.dst, output_name)
            output_list.append((filepath, output_path))

    for filename, output_name in output_list:
        cmd = f"ffmpeg -i {filename} -r 0.08 {output_name}%02d.png"
        print(cmd)
        subprocess.run(
            cmd, shell=True
        )


if __name__ == "__main__":
    main()
