from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'dye',
  packages = ['dye'],
  version = '0.3',
  description = 'Lightweight module with ANSI control codes to dye python scripts, the simplest and lightest module to work with colors and formatting.',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'ax',
  author_email = 'ax.tryin@gmail.com',
  url = 'https://github.com/ax-tryin/dye',
  download_url = 'https://github.com/ax-tryin/dye/archive/0.3.tar.gz',
  keywords = ['ANSI', 'color', 'terminal', 'lightweight']
)
