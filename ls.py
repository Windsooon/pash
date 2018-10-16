from arg_parse import parser
from List import LS

# Get args
args = parser.parse_args()
ls = LS(args)
ls.get_and_display()
