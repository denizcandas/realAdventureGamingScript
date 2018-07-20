from distutils.core import setup
import py2exe

adventure = [("",["adventure.txt"])]

setup(
	name="RAGpro",
	console=[{"script": "rag.py"}],
	zipfile=None,
	data_files= adventure,
	options={'py2exe': {'bundle_files': 1, 'dll_excludes': ['w9xpopen.exe']}}
)