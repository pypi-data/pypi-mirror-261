# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pretty_cli']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'mff-pretty-cli',
    'version': '0.2.1',
    'description': 'Simple helper to get pretty printing in the CLI.',
    'long_description': '# Pretty-CLI: Pretty Printing for the CLI\n\nThis package provides `PrettyCli`, a utility class for structured printing in the CLI. Simply use its `print()` and helper methods instead of the default `print()` and you\'re good to go!\n\nThe package is available in PyPi as `mff-pretty-cli`. You can install it with:\n```sh\npip install mff-pretty-cli\n```\n\nHere is a full example of the available function calls:\n\n```python\nfrom pretty_cli import PrettyCli\n\n\ncli = PrettyCli()\n\ncli.main_title("my example file:\\nAmazing")\n\ncli.print("Hello, world!")\ncli.print("你好！")\n\ncli.big_divisor() # Divisors, titles, etc. add blank space above/under as needed.\n\ncli.print("Let\'s print a dict:")\ncli.blank() # Add a blank if the previous line is not blank already.\ncli.blank()\ncli.blank()\ncli.print({ # Enforces nice alignment of dict contents.\n    "foo": "bar",\n    "nested": { "hi": "there" },\n    "another one": { "how": "are you?", "fine": "thanks" },\n})\n\ncli.small_divisor()\n\ncli.print("Some header styles:")\ncli.chapter("a chapter")\ncli.subchapter("a sub-chapter")\ncli.section("a section")\ncli.print("That\'s all, folks!")\n```\n\nAnd the produced output:\n\n```\n==================================================================\n======================== MY EXAMPLE FILE: ========================\n============================ AMAZING =============================\n==================================================================\n\nHello, world!\n你好！\n\n================================\n\nLet\'s print a dict:\n\nfoo:         bar\nnested:\n    hi:      there\nanother one:\n    how:     are you?\n    fine:    thanks\n\n----------------\n\nSome header styles:\n\n================ A Chapter ================\n\n-------- A Sub-Chapter --------\n\n[A Section]\n\nThat\'s all, folks!\n```\n\n## Dataclass Support\n\nBy default, dataclasses are converted to dicts. This code:\n\n```python\nimport math\nfrom dataclasses import dataclass\nfrom pretty_cli import PrettyCli\n\n\n@dataclass\nclass MyData:\n    some_int: int\n    some_float: float\n    some_string: str\n\n\ncli = PrettyCli()\n\nmy_data = MyData(\n    some_int=42,\n    some_float=math.pi,\n    some_string="Lorem ipsum dolor sit amet.",\n)\n\ncli.print(my_data)\n```\n\nProduces this output:\n\n```\nsome_int:    42\nsome_float:  3.141592653589793\nsome_string: Lorem ipsum dolor sit amet.\n```\n\n## Replicating to File\n\nSometimes, we want to save a copy of the output to a log file. In Unix systems, one can use `tee`:\n\n```sh\necho "Hi there" | tee hi.log\n```\n\nHowever, this is inconvenient in more complicated scenarios. For example, we might want to generate a timestamp within Python and use it for the file name, or we might want to strip color codes from the file output without using command-line tricks. `PrettyCli` has built-in support for replicating output to a file, with optional stripping of ANSI codes (on by default):\n\n```python\ncli = PrettyCli(log_file="path/to/file", strip_ansi=False) # strip_ansi defaults to True.\n```\n',
    'author': 'Marc Fraile',
    'author_email': 'marc.fraile.fabrega@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
