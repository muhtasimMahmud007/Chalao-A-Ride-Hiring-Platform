from pathlib import Path
import subprocess

directory = r"C:\Users\ASUS\Downloads\Assignment 4"

subdirs = [x for x in Path(directory).iterdir() if x.is_dir()]

count = 0
for subdir in subdirs:
    with open(str(subdir) + "/log.txt", "w") as f:
        pathlist = Path(subdir).glob("**/*.py")
        for path in pathlist:
            f.write(str(path).split("\\")[-1] + "\n")
            command = "python " + '"' + str(path) + '"'
            file_dir = str(Path(path).parent)
            try:
                result = subprocess.run(
                    command, cwd=file_dir, capture_output=True, text=True, timeout=30
                )
                f.write(f"Output:{result.stdout}\n")
                f.write(f"Errors:{result.stderr}\n")
            except subprocess.TimeoutExpired:
                f.write("Timeout expired while running the script.\n")
            except Exception as e:
                f.write(f"An error occurred: {e}\n")

            f.write("=" * 30 + "\n")

    count += 1
    print(f"{count}/{len(subdirs)}")

print("DONE")