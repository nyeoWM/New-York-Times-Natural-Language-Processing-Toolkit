# -*- mode: python ; coding: utf-8 -*-
import PyInstaller


block_cipher = None

newData = [
          ('df-semeval2010.tsv.gz','.'), 
          ('en_core_web_md-2.3.1','en_core_web_md-2.3.1')
          # ('/Users/Nicholas/repositories/Monash/FYP2020/testProduction/Preprocessing/en_core_web_md-2.3.1', 'Preprocessing/en_core_web_md-2.3.1' )
          ]

# newData.extend(PyInstaller.utils.hooks.collect_data_files('spacy.lang', include_py_files = True))
# newData.extend(PyInstaller.utils.hooks.collect_data_files('spacy_lookups_data'))
# newData.extend(PyInstaller.utils.hooks.collect_data_files('thinc'))
newData.extend(PyInstaller.utils.hooks.collect_data_files('en_core_web_md'))


a = Analysis(['guiNews.py'],
             pathex=['/Users/Nicholas/repositories/Monash/FYP2020/testProduction', '/Users/Nicholas/repositories/Monash/FYP2020/testProduction/Preprocessing'],
             binaries=[('/System/Library/Frameworks/Tk.framework/Tk', 'tk'), ('/System/Library/Frameworks/Tcl.framework/Tcl', 'tcl')],
             datas=newData,
             hiddenimports=['srsly.msgpack.util',
    'spacy.kb',
    'spacy.lexeme',
    'spacy.matcher._schemas',
    'spacy.morphology',
    'spacy.parts_of_speech',
    'spacy.syntax._beam_utils',
    'spacy.syntax._parser_model',
    'spacy.syntax.arc_eager',
    'spacy.syntax.ner',
    'spacy.syntax.nn_parser',
    'spacy.syntax.stateclass',
    'spacy.syntax.transition_system',
    'spacy.tokens._retokenize',
    'spacy.tokens.morphanalysis',
    'spacy.tokens.underscore',
    'blis',
    'blis.py',
    'cymem',
    'cymem.cymem',

    'murmurhash',

    'preshed.maps',

    'srsly.msgpack.util',

    'thinc.extra.search',
    'thinc.linalg',
    'thinc.neural._aligned_alloc',
    'thinc.neural._custom_kernels',
    'Preprocessing.Text_Preprocessing',
    'Preprocessing.XParser_Module',
    'sklearn.utils._cython_blas',
    'en_core_web_md'
],
             hookspath=["."],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
'''
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='guiNews',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
'''
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='guiNews',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='guiNews')
