#!/usr/bin/env python3
from pathlib import Path
import os
import sys

tooldir = str(Path(__file__).parent)
homedir = str(Path.home())

print(f'Tool dir: {tooldir}')
print(f'Home dir: {homedir}')
print()

def make_symlink(fro, to):
	try:
		Path(fro).symlink_to(to)
	except FileExistsError:
		print(f"Not creating symbolic link {fro} because it already exists.")
		pass

def install_linux():
	make_symlink(f'{tooldir}/dgbuild', f'{tooldir}/dgbuild.py')
	os.makedirs(f'{homedir}/.bashrc.d', exist_ok=True)
	Path(f"{homedir}/.bashrc.d/dgbuild-path.sh").write_text(f'#!/usr/bin/env bash\nexport PATH="$PATH:{tooldir}"\n')
	os.chmod(f"{homedir}/.bashrc.d/dgbuild-path.sh", 0o755)
	
	print("Installed! :3")

def uninstall_linux():
	os.remove(f'{homedir}/.bashrc.d/dgbuild-path.sh')
	try:
		os.rmdir(f'{homedir}/.bashrc.d')
	except OSError:
		pass
	os.unlink(f'{tooldir}/dgbuild')
	
	print("Uninstalled!")

if len(sys.argv) < 2 or sys.argv[1] == "install":
	install_linux()
elif sys.argv[1] == "uninstall":
	uninstall_linux()
else:
	print(f"Unknown operation: {sys.argv[1]}")
