#!/usr/bin/env python3
"""Package an already-built local fork; never touches the official Zed app."""
import json
import os
from pathlib import Path
import plistlib
import shutil
import sys

repo = Path(os.environ.get('ZED_PIXEL_REPO', '/Users/jumonteiro/Documents/zed'))
binary = repo / 'target' / os.environ.get('ZED_PIXEL_PROFILE', 'debug') / 'zed'
cli_binary = binary.parent / 'cli'
if not cli_binary.is_file():
    sys.exit(f'Build the companion CLI first: missing {cli_binary}')
if not binary.is_file():
    sys.exit(f'Build the local fork first: missing {binary}')
output = Path('/Users/jumonteiro/Documents/Codex/2026-10-23/fa/outputs')
app = output / 'Zed Pixel.app'
macos = app / 'Contents/MacOS'
resources = app / 'Contents/Resources'
macos.mkdir(parents=True, exist_ok=True)
resources.mkdir(parents=True, exist_ok=True)
shutil.copy2(binary, macos / 'zed')
shutil.copy2(cli_binary, macos / 'cli')
shutil.copy2(repo / 'pixel-arcade/branding/ZedPixel.icns', resources / 'ZedPixel.icns')
shutil.copy2(repo / 'crates/zed/resources/Document.icns', resources / 'Document.icns')
plist = {
    'CFBundleExecutable': 'zed',
    'CFBundleIdentifier': 'local.zedpixel.editor',
    'CFBundleName': 'Zed Pixel',
    'CFBundleDisplayName': 'Zed Pixel',
    'CFBundleIconFile': 'ZedPixel.icns',
    'CFBundlePackageType': 'APPL',
    'CFBundleShortVersionString': '1.27.0',
    'CFBundleVersion': '1',
    'NSHighResolutionCapable': True,
    'LSMinimumSystemVersion': '13.0',
    'NSPrincipalClass': 'NSApplication',
}
with (app / 'Contents/Info.plist').open('wb') as file:
    plistlib.dump(plist, file)
# Copy only the explicitly prepared preferences; never import account tokens.
data = Path.home() / 'Library/Application Support/ZedPixel'
config = data / 'config'
(config / 'themes').mkdir(parents=True, exist_ok=True)
settings = json.loads((repo / 'pixel-arcade/settings.json').read_text())
settings['auto_update'] = False
settings['edit_predictions'] = {'provider': 'none'}
if not (config / 'settings.json').exists():
    (config / 'settings.json').write_text(json.dumps(settings, indent=2) + '\n')
if not (config / 'tasks.json').exists():
    shutil.copy2(repo / 'pixel-arcade/tasks.json', config / 'tasks.json')
shutil.copy2(repo / 'pixel-arcade/themes/pixel-arcade.json', config / 'themes/pixel-arcade.json')
installed = data / 'extensions/installed'
installed.mkdir(parents=True, exist_ok=True)
public_csv = Path.home() / 'Library/Application Support/Zed/extensions/installed/rainbow-csv'
if public_csv.is_dir() and not (installed / 'rainbow-csv').exists():
    shutil.copytree(public_csv, installed / 'rainbow-csv')
link = installed / 'pixel-arcade'
if not os.path.lexists(link):
    link.symlink_to(repo / 'pixel-arcade', target_is_directory=True)
print(app)
