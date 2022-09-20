#!/usr/bin/env python3
from datetime import datetime
import dev_aberto
from babel.dates import format_datetime

import gettext
gettext.install('cli', localedir='locale') 

if __name__ == '__main__':
    date, name = dev_aberto.hello()
    date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    print(_('Último commit feito em:'), format_datetime(date), _(' por'), name)
