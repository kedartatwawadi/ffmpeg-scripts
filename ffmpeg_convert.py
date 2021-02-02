import os
import subprocess
import argparse


def main():
    parser = argparse.ArgumentParser(description="Convert yuv files to y4m")
    parser.add_argument("dir", type=str, help="input dir path")

    args = parser.parse_args()
    list_files = os.listdir(args.dir)

    output_list = []
    for filename in list_files:
        # check for.yuv extension
        _temp = filename.split(".")
        assert len(_temp) == 2, "only one . allowed in filename"
        base_name, ext = _temp
        if ext == "yuv":
            # extract fps
            _temp = base_name.split("_")
            assert len(_temp) == 2, "only one _ allowed in base_name"
            vid_name, fps_str = _temp
            fps = int(fps_str[:-3])
            output_name = vid_name + f"_1080p_{fps}fps.y4m"
            print(f"{filename}, {output_name}")
            output_list.append((filename, output_name, fps))

    for filename, output_name, fps in output_list:
        subprocess.run(
            f"ffmpeg -video_size 1920x1080 -framerate {fps} -pixel_format yuv420p -i {filename}  {output_name}",
            shell=True,
        )


if __name__ == "__main__":
    main()
