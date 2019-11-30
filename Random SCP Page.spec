# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Random SCP Page.pyw'],
             pathex=['C:\\Users\\zachm\\PycharmProjects\\rand-scp'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Random SCP Page',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=['vcruntime140.dll'],
          runtime_tmpdir=None,
          console=False , icon='Random SCP Page.ico')
