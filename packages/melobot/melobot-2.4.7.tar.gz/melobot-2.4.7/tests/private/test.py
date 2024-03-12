import sys

import docstring_parser

sys.path.append("..")
from melobot import MetaInfo

res = docstring_parser.parse(MetaInfo.get_all.__doc__)
print(res)
