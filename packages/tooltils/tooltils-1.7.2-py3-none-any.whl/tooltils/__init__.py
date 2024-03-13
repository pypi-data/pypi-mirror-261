"""
# tooltils | v1.7.2

A lightweight python utility package built on the standard library

```py
>>> import tooltils
>>> data = tooltils.requests.get('httpbin.org/get')
>>> data.status_code
'200 OK'
>>> data.end_data.url
'https:/httpbin.org/get'
>>> data.end_data.sent_headers
{'User-Agent': 'Python-tooltils/1.7.2', 'Accept-Encoding': 'gzip, deflate', ...}
>>> data.headers
{'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', ...}
```

## API

Read the full documentation within `API.md` included in the github project directory
"""

import tooltils.requests as requests
import tooltils.errors as errors
import tooltils.info as info
import tooltils.os as os

class _bm:
    from time import time, localtime, gmtime, perf_counter
    from datetime import datetime, timezone, timedelta
    from os.path import abspath, getsize, exists
    from typing import Any, Union, Dict, List
    from shutil import copyfileobj, rmtree
    from tarfile import open as topen
    from gzip import open as gopen
    from io import TextIOWrapper
    from os import mkdir, remove
    
    class EPOCH_seconds:
        pass

    class FileDescriptorOrPath:
        pass

    months:  list = [
        'January', 'February', 
        'March', 'April', 
        'May', 'June', 
        'July', 'August', 
        'September', 'October', 
        'November', 'December'
    ]
    sMonths: list = [
        'Jan', 'Feb', 'Mar', 'Apr', 
        'May', 'Jun', 'Jul', 'Aug', 
        'Sep', 'Oct', 'Nov', 'Dec'
    ]

    def fv(*values) -> tuple:
        return [str(i) if i > 9 else f'0{i}' for i in values]

    logger = info._logger('')


ANSI_colours: _bm.Dict[str, int] = {
    "white":  97,
    "cyan":   36,
    "pink":   35,
    "blue":   34,
    "yellow": 33,
    "green":  32,
    "red":    31,
    "gray":   30,
}
"""List of major colours as ANSI integer codes"""

def length(file: _bm.FileDescriptorOrPath) -> float:
    """Get the length of a wave file in seconds"""

    if type(file) is not str:
        raise TypeError('File must be a valid \'str\' instance')
    if file.split('.')[-1] != 'wav':
        raise ValueError('File is not a WAVE type')
    if not _bm.exists(file):
        raise FileNotFoundError('Could not locate WAVE file')

    try:
        with open(file, encoding='latin-1') as _f:
            _f.seek(28)
            sdata = _f.read(4)
    except IsADirectoryError:
        raise FileNotFoundError('An error occured while opening the WAVE file')

    rate: int = 0
    for i in range(4):
        rate += ord(sdata[i]) * pow(256, i)

    return round((_bm.getsize(file) - 44) * 1000 / rate / 1000, 2)

def style(text: str, 
          colour: str='',
          bold: bool=False,
          italic: bool=False,
          fill: bool=False,
          crossed: bool=False,
          underline: bool=False,
          double_underline: bool=False
          ) -> str:
    """Create text in the specified colour and or style"""

    if type(text) is not str:
        raise TypeError('Text must be a valid \'str\' instance')
    if not isinstance(colour, (str, int)):
        raise TypeError('Colour must be a valid \'str\' instance')

    if not colour:
        code = 0
    else:
        code = ANSI_colours.get(colour.lower(), colour)

    style: str = ''
    for k, v in {'1': bold, '3': italic, '9': crossed, 
                 '4': underline, '21': double_underline}.items():
        if v:
            style += ';' + k

    if fill:
        code += 10

    return '\u001b[{}{}m{}\u001b[0m'.format(code, style, text)

def halve(array: _bm.Union[str, list, tuple, set, dict]) -> list:
    """Return the halves of a string or array"""

    if not isinstance(array, (str, list, tuple, set, dict)):
        raise TypeError('Array must be a valid \'str\' or array instance')

    i: int = len(array)
    if i % 2 == 0:
        return [array[:i // 2], array[i // 2:]]
    else:
        return [array[:(i // 2 + 1)], array[(i // 2 + 1):]]

def cipher(text: str, shift: int) -> str:
    """A simple caeser cipher"""

    if type(text) is not str:
        raise TypeError('Text must be a valid \'str\' instance')
    elif len(text) < 1:
        raise ValueError('Invalid text')
    if type(shift) is not int:
        raise TypeError('Shift must be a valid \'int\' instance')
    elif shift == 0:
        raise ValueError('Shift must not be 0')
    
    result: str = ''

    for i in text:
        start: int = 65 if i.isupper() else 97
        result    += chr((ord(i) + shift - start) % 26 + start)

    return result

def mstrip(text: str, values: dict) -> str:
    """Change some text from a dictionary pair of values"""

    if type(text) is not str:
        raise TypeError('Text must be a valid \'str\' instance')
    if type(values) is not dict:
        raise TypeError('Values must be a valid \'dict\' instance ')
    
    for k, v in values.items():
        text = text.replace(k, v)
    
    return text

def date(epoch: _bm.EPOCH_seconds=..., 
         timezone: str='local', 
         format: int=0
         ) -> str:
    """
    Convert the current date timestamp to a readable format
    
    #### Format:
    - `0:` "2024/03/08 17:29:46"
    - `1:` "5:30 PM on the 8th of March, 2024"
    - `2:` "Mar 8 2024, 17:30:23"
    """

    if not isinstance(epoch, (int, float)) and epoch != ...:
        raise TypeError('Epoch must be a valid \'int\' or \'float\' instance')
    if type(timezone) is not str:
        raise TypeError('Timezone must be a valid \'str\' instance')
    if type(format) is not int:
        raise TypeError('Format must be a valid \'int\' instance')

    try:
        if epoch == ...: 
            epoch = _bm.time()
        
        timezone = timezone.lower()

        if timezone == 'local':
            sdate = _bm.localtime(epoch)
        elif timezone == 'gm' or '00:00' in timezone:
            sdate = _bm.gmtime(epoch)
        elif timezone.startswith('+') or timezone.startswith('-'):
            timezone = _bm.timezone(_bm.timedelta(
                       hours=int(timezone[:3]), 
                       minutes=int(timezone[4:])))
            sdate    = _bm.datetime.fromtimestamp(epoch, 
                       tz=timezone).timetuple()
        else:
            raise ValueError('Invalid timezone')
    except (ValueError, IndexError):
        raise TypeError('Timezone not found')
    except OverflowError:
        raise OverflowError('Epoch timestamp too large')

    if format == 0:
        return '{}/{}/{} {}:{}:{}'.format(sdate.tm_year,
               *_bm.fv(sdate.tm_mon, sdate.tm_mday, sdate.tm_hour,
               sdate.tm_min, sdate.tm_sec))

    elif format == 1:
        hour: int = sdate.tm_hour % 12 if sdate.tm_hour % 12 != 0 else 12
        end: list = ['th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th'
                     ][int(str(sdate.tm_mday)[-1])]
        if sdate.tm_mday in [11, 12, 13]:
            end: str = 'th'

        return '{}:{} {} on the {}{} of {}, {}'.format(hour, *_bm.fv(sdate.tm_min), 
               'PM' if sdate.tm_hour >= 12 else 'AM', sdate.tm_mday, end, 
               _bm.months[sdate.tm_mon - 1], sdate.tm_year)

    elif format == 2:
        return '{} {} {}, {}:{}:{}'.format(_bm.sMonths[sdate.tm_mon - 1], sdate.tm_mday,
                                          sdate.tm_year, *_bm.fv(sdate.tm_hour, sdate.tm_min, 
                                          sdate.tm_sec))

    else:
        raise ValueError('Format ({}) not found'.format(format))

def epoch(date: str) -> int:
    """Get the epoch timestamp from a formatted date"""

    if type(date) is not str:
        raise TypeError('Date must be a valid \'str\' instance')

    if '/' in date:
        splitDate: list = str(date).split(' ')
    elif '-' in date:
        splitDate: list = str(date).replace('-', '/').split(' ')
    elif ',' in date:
        try:
            # Remove '1st' to avoid stripping Augu[st]
            sdate: list = mstrip(date, 
                          {':': ' ', ' on the': '', 
                           ' of': '', ',': '',
                           'th': '', '1st': '',
                           'nd': '', 'rd': ''}).split(' ')
            hours, minutes, meridan, days, month, year = sdate

            if '1st' in date:
                days = '1'
            if meridan == 'PM':
                hours = str(int(hours) + 12)

            splitDate: list = [year + '/' + str(int(_bm.months.index(month)) + 1)
                               + '/' + days, hours + ':' + minutes + ':00']
        except (IndexError, ValueError):
            try:
                month, days, year, hours, minutes, seconds = mstrip(
                    date, {":": " ", ",": ""}).split(' ')

                splitDate: list = [year + '/' + str(int(_bm.sMonths.index(month)) + 1)
                                   + '/' + days, hours + ':' + minutes + ':' + seconds]
            except (IndexError, ValueError):
                raise ValueError('Invalid date')
    else:
        raise ValueError('Unknown date format')

    try:
        sdate = _bm.datetime(*[int(i) for i in splitDate[0].split(
                             '/') + splitDate[1].split(':')])
    except IndexError:
        raise ValueError('Invalid date')

    days: int = _bm.datetime(sdate.year, sdate.month, 
                             sdate.day, sdate.hour,
                             sdate.minute, sdate.second).toordinal(
                             ) - _bm.datetime(1970, 1, 1).toordinal() - 1

    # Add 13 hours because of obscure glitch
    hours = days * 24 + sdate.hour + 13
    minutes = hours * 60 + sdate.minute
    epoch = minutes * 60 + sdate.second
    
    return epoch

def squeeze(array: _bm.Union[list, tuple, set, dict],
            item: _bm.Any=None
            ) -> _bm.Union[list, tuple, set, dict]:
    """Remove empty or the specified item(s) from an array"""
    
    if not isinstance(array, (list, tuple, set, dict)):
        raise TypeError('Array must be a valid iterable container')

    op = type(array)
    if op is not dict:
        array = list(array)

    if item is None:
        if op is dict:
            for i in tuple(array.keys()):
                if not array[i]:
                    array.pop(i)
        
            return array
        else:
            return op(filter(None, array))
    else:
        if op is dict:
            for i in tuple(array.keys()):
                if array[i] == item:
                    array.pop(i)
        else:
            for i, it in enumerate(array):
                if it == item:
                    array.pop(i)

        return op(array)

def reverseDictSearch(array: dict, value: _bm.Any) -> tuple:
    """Find the unknown key(s) of a value in a dictionary"""

    if type(array) is not dict:
        raise TypeError('Array must be a valid dictionary instance')

    # Create an isolated dict inside of the list to avoid
    # duplicate values getting merged/deleted
    swappedDict: list = [{v: k} for (k, v) in array.items()]
    results:     list = []

    for i in range(len(swappedDict)):
        try:
            results.append(swappedDict[i][value])
        except KeyError:
            continue
    else:
        if results == []:
            raise IndexError('There was no key matching the specified value')
        else:
            return tuple(results)

def getArrayValues(array: _bm.Union[list, tuple, dict]) -> tuple:
    """Recursively obtain all of the values of any keys or items within an array"""

    if not isinstance(array, (list, tuple, dict)):
        raise TypeError('Array must be a valid \'list\', \'tuple\' or \'dict\' instance')

    values: list = []

    if isinstance(array, dict):
        items: list = [i[1] for i in array.items()]
    else:
        items: list = list(array)

    for i in items:
        if isinstance(i, dict):
            for ii in getArrayValues(i):
                values.append(ii) 
        elif isinstance(i, (list, tuple)):
            for ii in i:
                if isinstance(ii, (dict, list, tuple)):
                    for iii in getArrayValues(ii):
                        values.append(iii)
                else:
                    values.append(ii)
        else:
            values.append(i)

    return tuple(values)

def timeTest(method, 
             params: dict={},
             accuracy: int=10
             ) -> float:
    """Run a method with optional kwargs {accuracy} amount of times, sum then divide by {accuracy} for precise run time"""

    avg: list = []

    if type(accuracy) is not int:
        raise TypeError('Accuracy must be a valid \'int\' instance')
    elif accuracy < 1:
        raise ValueError('Accuracy must be 1 or bigger')

    if not hasattr(method, '__call__'):
        raise TypeError('Method must be a callable instance')

    if type(params) is not dict:
        raise TypeError('Params must be a valid \'dict\' instance')

    for i in range(accuracy):
        start = _bm.perf_counter()
        method(**params)
        one = _bm.perf_counter() - start

        avg.append(one)

    return sum(avg) / accuracy

def varName(**vars: dict) -> _bm.Union[str, _bm.List[str]]:
    """Get the namespace name of one or more variables"""

    names: list = [x for x in vars]

    if len(names) == 1:
        return names[0]
    else:
        return names

def tgzOpen(file: _bm.FileDescriptorOrPath, 
            output: _bm.FileDescriptorOrPath=None,
            ) -> str:
    """Open a gzipped tar file"""

    if type(file) is not str:
        raise TypeError('File must be a valid \'str\' instance')
    elif not file.endswith('.tar.gz') and not file.endswith('.tgz'):
        raise ValueError('File is not a valid gzipped tar instance')
    elif not _bm.exists(file):
        raise FileNotFoundError('Could not locate the specified gzipped tar file')
    else:
        file: str = _bm.abspath(file)

    if file.endswith('.tar.gz'):
        tfile: str = '.'.join(file.split('.')[:-1])
    elif file.endswith('.tgz'):
        tfile: str = '.'.join(file.split('.')[:-1]) + '.tar'
    if output is None:
        output: str = '.'.join(tfile.split('.')[:-1])
    elif type(output) is not str:
        raise TypeError('Output must be a valid \'str\' instance')
    else:
        output: str = _bm.abspath(output)
    if _bm.exists(output) or _bm.exists(tfile):
        raise FileExistsError('Output file/folder already file exists')

    with _bm.gopen(file, 'rb') as _f, open(tfile, 'wb') as _f2:
        _bm.copyfileobj(_f, _f2)
    
    _bm.logger._debug(f'Uncompressed gzip file {file} to {tfile}', 'tgzOpen')

    with _bm.topen(tfile) as _f:
        _f.extractall(output)
    
    _bm.logger._debug(f'Extracted tarfile {tfile} to {output}', 'tgzOpen')

    _bm.remove(tfile)

    _bm.logger._debug(f'Deleted tarfile {tfile}', 'tgzOpen')

    return output

def lengthSort(array: _bm.Union[list, tuple, set, dict],
               fromLowest: bool=True,
               sortByKey: bool=False
               ) -> _bm.Union[list, tuple, set, dict]:
    """Sort an array by it's length"""

    if not isinstance(array, (list, tuple, set, dict)):
        raise TypeError('Array must be a valid \'list\', \'tuple\', \'set\' or \'dict\' instance')
    elif len(array) == 0:
        raise ValueError('Array cannot be empty')
    
    if isinstance(array, (list, tuple, set)):
        return sorted(array, key=lambda l: len(l), reverse=not fromLowest)
    elif type(array) is dict:
        return dict(sorted(array.items(), key=lambda l: len(l[1 if sortByKey else 0]),
                           reverse=fromLowest)) # sorted() isn't flipped here for some reason,
                                                # that's why fromLowest is being passed as is

class interpreter():
    """Custom top-level Python interpreter to add useful typing features"""

    def __init__(self, 
                 file: str,
                 output: str='%(name)s.interpreted.py',
                 override: bool=False,
                 ternary: bool=True,
                 comments: bool=True):
        if type(file) is not str:
            raise TypeError('File must be a valid \'str\' instance')
        if not _bm.exists(file):
            raise FileNotFoundError('Could not locate Python file')
        if type(output) is not str:
            raise TypeError('Output must be a valid \'str\' instance')

        self.file: str = file

        if '.' in file:
            file: str = '.'.join(file.split('.')[0:-1])
        else:
            file: str = file

        self.output:        str = output % {"name": file}
        self.override:     bool = bool(override)
        self.ternary:      bool = bool(ternary)
        self.comments:     bool = bool(comments)
        self._interpreted: list = []

        if not self.override and _bm.exists(self.output):
            raise FileExistsError('Output file already present')

        try:
            with open(self.file) as _f:
                _content = _f.readlines()
        except IsADirectoryError:
            raise FileNotFoundError('There was a problem locating the file')

        for i, line in enumerate(_content):
            if line.strip() == '\n' or line.strip() == '':
                self._interpreted.append(line)
            elif self.comments and line.lstrip()[:2] == '//':
                self._interpreted.append(self._convertComment(line))

                _bm.logger.debug(f'Found comment on line {i} on tooltils.interpreter() for file \'{self.file}\'')
            elif self.ternary and line.lstrip()[0] != '#' and len(line.split('=')) != 1 and \
                 len(line.split('=')[1].split('?')) != 1:
                self._interpreted.append(self._convertTernary(line))

                _bm.logger.debug(f'Found ternary condition on line {i} on tooltils.interpreter() for file \'{self.file}\'')
            else:
                self._interpreted.append(line)

        with open(self.output, 'a+') as _f:
            _f.truncate(0)
            _f.writelines(self._interpreted)
        
        self.file:   str = _bm.abspath(self.file)
        self.output: str = _bm.abspath(self.output)

    def __str__(self):
        return '<Interpreter instance [{}]>'.format(self.file.split(info._bm.split)[-1])

    def _getIndent(self, line: str) -> str:
        return ''.join([' ' for i in range(len(line) - len(line.lstrip()))])

    def _convertTernary(self, line: str) -> _bm.Union[str, None]:
        statement: list = line.split('=')

        try:
            condition: str = statement[1].split('?')[0][1:-1]
            values:   list = statement[1].split('?')[1].split(':')

            return '{} = {} if {} else {}\n'.format(statement[0][:-1], values[0].strip(), condition, 
                                                    values[1].strip().replace('\n', ''))
        except Exception as error:
            raise error

    def _convertComment(self, line: str) -> _bm.Union[str, None]:
        return self._getIndent(line) + '#' + line.lstrip()[2:]

    def read(self) -> str:
        """Read the output file and return the content as a string"""

        if ''.join(self._interpreted)[-1:] == '\n':
            return ''.join(self._interpreted)[:-1]
        else:
            return ''.join(self._interpreted)
    
    def readlines(self) -> list:
        """Read the output file and return the content as a list containing strings split at every newline"""

        return self._interpreted
