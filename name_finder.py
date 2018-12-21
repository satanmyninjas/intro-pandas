import pandas as pd
import glob
import os
import matplotlib.pyplot as plt


# Just replacing the names and stuff. Command-C and Command-V for the win.
# ================================================================================

data_2003 = pd.read_csv('~/intro-pandas/data/yob2003.txt', header=None, names=['Name', 'Sex', 'Count'])
data_2003.head()

females_2003 = data_2003[data_2003['Sex'] == 'F']
females_2003.head()

females_2003 = females_2003.reset_index(drop=True)
females_2003.head()

females_2003.index = range(1, len(females_2003) + 1)
females_2003.head()

females_2003.index.name = 'Rank'
females_2003.head()

females_2003[females_2003['Name'] == 'Kayla']

# BONUS 1!
# ================================================================================
# Section below shows popularity of my name for both sexes.

both_sexes_2003 = data_2003[data_2003['Sex'] == 'F'] + data_2003[data_2003['Sex'] == 'M']
both_sexes_2003.head()

both_sexes_2003 = both_sexes_2003.reset_index(drop=True)
both_sexes_2003.head()

both_sexes_2003.index = range(1, len(both_sexes_2003) + 1)
both_sexes_2003.head()

both_sexes_2003.index.name = 'Rank'
both_sexes_2003.head()

both_sexes_2003[both_sexes_2003['Name'] == 'Kayla']

# BONUS 2!
# ================================================================================
# Looping time.

fnames = sorted(glob.glob('intro-pandas/data/*.txt'))
fnames[:5]

ranks = [range(1, 6)]

for _ in fnames:
    fnames += ranks

plt.title('Popularity of Kayla: 1882-2017')
plt.xlabel('Year')
plt.ylabel('Rank')
years = range(1882, 2018)
plt.plot(years, ranks, '.')
plt.show()

# ================================================================================
# ERRORS I GOT THAT I DON'T GET BELOW:

"""
Traceback (most recent call last):
  File "/Users/kayla_fernandez/PycharmProjects/intro-pandas/name_finder.py", line 10, in <module>
    data_2003 = pd.read_csv('yob2003.txt', header=None, names=['Name', 'Sex', 'Count'])
    
File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/io/parsers.py", line 678, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/io/parsers.py", line 440, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/io/parsers.py", line 787, in __init__
    self._make_engine(self.engine)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/io/parsers.py", line 1014, in _make_engine
    self._engine = CParserWrapper(self.f, **self.options)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/io/parsers.py", line 1708, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas/_libs/parsers.pyx", line 384, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas/_libs/parsers.pyx", line 695, in pandas._libs.parsers.TextReader._setup_parser_source
FileNotFoundError: File b'yob2003.txt' does not exist
"""
