# -*- mode: python ; coding: utf-8 -*-

from argparse import ArgumentParser
from platform import system

parser = ArgumentParser()
parser.add_argument("--binary", action="store_true")
options = parser.parse_args()

a = Analysis(
    ['helloworldtk.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('LICENSE', '.')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

if system() == "Linux":
    if not options.binary:
        exe = EXE(
            pyz,
            a.scripts,
            [],
            exclude_binaries=True,
            name='hello-world-tk',
            debug=False,
            bootloader_ignore_signals=False,
            strip=False,
            upx=True,
            console=False,
            disable_windowed_traceback=False,
            argv_emulation=False,
            target_arch=None,
            codesign_identity=None,
            entitlements_file=None,
        )
        coll = COLLECT(
            exe,
            a.binaries,
            a.datas,
            strip=False,
            upx=True,
            upx_exclude=[],
            name='hello-world-tk',
        )
    else:
        exe = EXE(
            pyz,
            a.scripts,
            a.binaries,
            a.datas,
            [],
            name='hello-world-tk',
            debug=False,
            bootloader_ignore_signals=False,
            strip=False,
            upx=True,
            upx_exclude=[],
            runtime_tmpdir=None,
            console=False,
            disable_windowed_traceback=False,
            argv_emulation=False,
            target_arch=None,
            codesign_identity=None,
            entitlements_file=None,
        )
elif system() == "Darwin":
    if not options.binary:
        exe = EXE(
            pyz,
            a.scripts,
            [],
            exclude_binaries=True,
            name='hello-world-tk',
            icon='macos/org.example.HelloWorldTk.icns',
            debug=False,
            bootloader_ignore_signals=False,
            strip=False,
            upx=True,
            console=False,
            disable_windowed_traceback=False,
            argv_emulation=False,
            target_arch=None,
            codesign_identity=None,
            entitlements_file=None,
        )
        coll = COLLECT(
            exe,
            a.binaries,
            a.datas,
            strip=False,
            upx=True,
            upx_exclude=[],
            name='hello-world-tk',
        )
        app = BUNDLE(
            coll,
            name='Hello World.app',
            icon='macos/org.example.HelloWorldTk.icns',
            bundle_identifier=None,
            version=None,
        )
    else:
        exe = EXE(
            pyz,
            a.scripts,
            a.binaries,
            a.datas,
            [],
            name='hello-world-tk',
            icon='macos/org.example.HelloWorldTk.icns',
            debug=False,
            bootloader_ignore_signals=False,
            strip=False,
            upx=True,
            upx_exclude=[],
            runtime_tmpdir=None,
            console=False,
            disable_windowed_traceback=False,
            argv_emulation=False,
            target_arch=None,
            codesign_identity=None,
            entitlements_file=None,
        )
elif system() == "Windows":
    if not options.binary:
        exe = EXE(
            pyz,
            a.scripts,
            [],
            exclude_binaries=True,
            name='hello-world-tk',
            icon='windows/org.example.HelloWorldTk.ico',
            debug=False,
            bootloader_ignore_signals=False,
            strip=False,
            upx=True,
            console=False,
            disable_windowed_traceback=False,
            argv_emulation=False,
            target_arch=None,
            codesign_identity=None,
            entitlements_file=None,
        )
        coll = COLLECT(
            exe,
            a.binaries,
            a.datas,
            strip=False,
            upx=True,
            upx_exclude=[],
            name='hello-world-tk',
        )
    else:
        exe = EXE(
            pyz,
            a.scripts,
            a.binaries,
            a.datas,
            [],
            name='hello-world-tk',
            icon='windows/org.example.HelloWorldTk.ico',
            debug=False,
            bootloader_ignore_signals=False,
            strip=False,
            upx=True,
            upx_exclude=[],
            runtime_tmpdir=None,
            console=False,
            disable_windowed_traceback=False,
            argv_emulation=False,
            target_arch=None,
            codesign_identity=None,
            entitlements_file=None,
        )
