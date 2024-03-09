from datetime import timedelta
import shutil
import re
import os
import time
import traceback
import string
from urllib import parse
import yaml

from dateutil import parser
from glom import glom, assign

from .definitions import DEFAULT_LANGUAGE

from .loaders import ModuleLoader

# ---------------------------------------------------------
# Loggers
# ---------------------------------------------------------

from agptools.logs import logger

log = logger(__name__)

# subloger = logger(f'{__name__}.subloger')
# import jmespath


# ----------------------------------------------------------
# Progress
# ----------------------------------------------------------
class Progress:
    def __init__(self, x0=0, N=10):
        self.N = N
        self.samples = []
        self.update(x0)

    def update(self, x):
        sample = time.time(), x
        self.samples.append(sample)


def build_workspace(path=None, interactive=True, package_folder=None):
    if not path:
        path = "."

    if not package_folder:
        package_folder = os.path.dirname(os.path.dirname(__file__))

    root = expandpath(path)
    if interactive:
        log.info(f"Creating / updating workspace in {root}")
    os.makedirs(root, exist_ok=True)

    # mapping_path = os.path.join(root, "mapping.yaml")
    # if not os.path.exists(mapping_path):
    #     yaml.dump(MAPPING, open(mapping_path, "wt"), Dumper=yaml.Dumper)

    # # Interests
    # mapping = yaml.load(open(mapping_path), Loader=yaml.Loader)
    # LANG_UX_CONFIG["interest"][-1] = mapping["default"]

    # for table, (klass, default_names, default_mapping) in LANG_UX_CONFIG.items():
    #     default_names = default_names or {k: k for k in [e.value for e in klass]}
    #     names = {DEFAULT_LANG: default_names}
    #     build_configuration_ui_config(root, table, names, klass, default_mapping)

    # # markov chains
    # markov = build_markov_configuration(root)

    # Stats / KPI
    stats_path = os.path.join(root, "stats.yaml")
    db_path = expandpath(os.path.join(root, "db"))

    if not os.path.exists(stats_path):
        db = {
            "kpi_1": 0.73,
            "kpi_2": 0,
        }
        yaml.dump(db, open(stats_path, "wt"), Dumper=yaml.Dumper)

    # config file
    config_path = os.path.join(root, "config.yaml")
    if not os.path.exists(config_path):
        db = {
            "app_url": "https://domain:8000",
            "app_url_dev": "https://bigplanner.spec-cibernos.com",
            "app_dev": True,
            # "mapping_url": mapping_path,
            # "markov": markov,
            # "interest_url": interests_path,
            "templates": {
                "compiled": {
                    "{root}/{reldir}/compiled/{basename}.json": [
                        r"(?P<dirname>.*)[/\/](?P<basename>(?P<name>.*?)(?P<ext>\.[^\.]+$))"
                    ],
                },
                "error": {
                    "{root}/error/{reldir}/{basename}": [
                        r"(?P<dirname>.*)[/\/](?P<basename>(?P<name>.*?)(?P<ext>\.[^\.]+$))"
                    ],
                },
            },
            "stats": stats_path,
            "db_url": db_path,
            "folders": {
                "data": f"{root}/data/",
            },
            "num_threads": 8,
        }

        # initial active ports found
        from .api import ports

        # show found active ports
        # add '.*' regexp pattern to include any other port created later
        # later by default, so it must be visible until user manually will change
        # which ports wants to be exposed or not
        loader = ModuleLoader(ports)

        db[loader.ACTIVE_PORT_KEY] = loader.available_modules() + [".*"]

        # lang specific configuration
        lang = DEFAULT_LANGUAGE
        # for table, (klass, default_names, default_mapping) in LANG_UX_CONFIG.items():
        #     _path = os.path.join(root, f"{table}" + ".{lang}.yaml")
        #     db[f"{table}_url"] = _path

        yaml.dump(db, open(config_path, "wt"), Dumper=yaml.Dumper)

    # check folder in config file
    cfg = yaml.load(open(config_path, "rt"), Loader=yaml.Loader)

    # create working folders
    for name in cfg["folders"].values():
        path = os.path.join(root, name)
        os.makedirs(path, exist_ok=True)

    # coping deployments files
    shutil.copytree(
        os.path.join(
            package_folder,
            "deploy",
            "static",
        ),
        os.path.join(root, "static"),
        dirs_exist_ok=True,
    )

    # check .env file
    env_path = os.path.join(root, ".env")
    if not os.path.exists(env_path):
        content = f"""# ENV variables
OPENAI_API_KEY=
"""
        open(env_path, "wt").write(content)

    # check gitlab_cfg_path file
    # if not os.path.exists(gitlab_cfg_path):
    # content = f"""


# [global]
# default = spec
# ssl_verify = true
# timeout = 10

# [spec]
# url = https://git.spec-cibernos.com
# private_token = glpat-ZZ_TDbasg1CsyCsa4ihG
# api_version = 4

# [elsewhere]
# url = http://else.whe.re:8080
# private_token = helper: path/to/helper.sh
# timeout = 1
# """
# open(gitlab_cfg_path, "wt").write(content)


# ------------------------------------------------
# File and config helpers
# ------------------------------------------------
def replace(text):
    text = str(text)
    text = text.lower()
    text = text.replace("á", "a")
    text = text.replace("é", "e")
    text = text.replace("í", "i")
    text = text.replace("ó", "o")
    text = text.replace("ú", "u")
    return text


def expandpath(path):
    if path:
        path = os.path.expanduser(path)
        path = os.path.expandvars(path)
        path = os.path.abspath(path)
        while path[-1] == "/":
            path = path[:-1]
    return path


def load_config(env):
    """Merge config files"""
    cfg = env.__dict__
    for path in reversed(env.config_files):
        try:
            data = yaml.load(open(path, "rt"), Loader=yaml.Loader)
            # merge(cfg, data, inplace=True) # use any deep merge library or ...
            cfg.update(data)

        except FileNotFoundError:
            pass

    env.folders = {expandpath(p): None for p in env.folders}


def save_config(env):
    os.makedirs(os.path.dirname(env.config_file), exist_ok=True)
    yaml.dump(env.__dict__, open(env.config_file, "wt"))


# -----------------------------------------------------------
# URI handling
# -----------------------------------------------------------
reg_uri = re.compile(
    """(?imsx)
    (?P<fservice>
        (
            (?P<fscheme>
                (?P<direction>[<|>])?(?P<scheme>[^:/]*))
                ://
        )?
        (?P<xhost>
           (
                (?P<auth>
                   (?P<user>[^:@/]*?)
                   (:(?P<password>[^@/]*?))?
                )
            @)?
           (?P<host>[^@:/?]*)
           (:(?P<port>\d+))?
        )
    )?
    (?P<path>/[^?]*)?
    (\?(?P<query>[^#]*))?
    (\#(?P<fragment>.*))?
    """
)


def parse_uri(uri, bind=None, drop_nones=False, default=None, **kw):
    """Extended version for parsing uris:

    Return includes:

    - *query_*: dict with all query parameters splitted

    If `bind` is passed, *localhost* will be replace by argument.

    """

    m = reg_uri.match(uri)
    if m:
        for k, v in m.groupdict(default=default).items():
            if k not in kw or v is not None:
                kw[k] = v
        if bind:
            kw["host"] = kw["host"].replace("localhost", bind)
        if kw["port"]:
            kw["port"] = int(kw["port"])
            kw["address"] = tuple([kw["host"], kw["port"]])
        if kw["query"]:
            kw["query_"] = dict(parse.parse_qsl(kw["query"]))

        kw["uri"] = uri

    if drop_nones:
        kw = {k: v for k, v in kw.items() if v is not None}
    return kw


# --------------------------------------------------
#  Convert Base
# --------------------------------------------------
def build_uri(
    fscheme="",
    direction="",
    scheme="",
    xhost="",
    host="",
    port="",
    path="",
    query="",
    fragment="",
    query_={},
    **kw,
):
    """Generate a URI based on individual parameters"""
    uri = ""
    if fscheme:
        uri += fscheme or ""
    else:
        if not direction:
            uri += scheme or ""
        else:
            uri += f"{direction}{scheme or ''}"
    if uri:
        uri += "://"

    if xhost:
        uri += xhost
    else:
        host = host or f"{uuid.getnode():x}"
        uri += host
        if port:
            uri += f":{port}"

    if path:
        uri += f"{path}"

    if query_:
        # query_ overrides query if both are provided
        query = "&".join([f"{k}={v}" for k, v in query_.items()])

    elif isinstance(query, dict):
        query = "&".join([f"{k}={v}" for k, v in query.items()])

    if query:
        uri += f"?{query}"
    if fragment:
        uri += f"#{fragment}"

    return uri


# --------------------------------------------------
#  Convert Base
# --------------------------------------------------

# CHAR_LOOKUP = list(string.digits + string.ascii_letters)

#  avoid use of numbers (so can be used as regular attribute names with ".")
CHAR_LOOKUP = list(string.ascii_letters)
INV_LOOKUP = {c: i for i, c in enumerate(CHAR_LOOKUP)}


def convert_base(number, base, padding=-1, lookup=CHAR_LOOKUP):
    """Coding a number into a string in base 'base'

    results will be padded with '0' until minimal 'padding'
    length is reached.

    lookup is the char map available for coding.
    """
    if base < 2 or base > len(lookup):
        raise RuntimeError(f"base: {base} > coding map length: {len(lookup)}")
    mods = []
    while number > 0:
        mods.append(lookup[number % base])
        number //= base

    while len(mods) < padding:
        mods.append(lookup[0])

    mods.reverse()
    return "".join(mods)


def from_base(key, base, inv_lookup=INV_LOOKUP):
    """Convert a coded number in base 'base' to an integer."""
    number = 0
    keys = list(key)
    keys.reverse()
    w = 1
    for c in keys:
        number += INV_LOOKUP[c] * w
        w *= base
    return number


# def new_uid(base=50):
# number = uuid.uuid1()
# return convert_base(number.int, base)
SEED = 12345


def new_uid(base=50):
    global SEED
    SEED += 1
    return convert_base(SEED, base)


# from xml.sax.saxutils import escape
# ------------------------------------------------
# jinja2 filters
# ------------------------------------------------
def escape(text: str):
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    text = text.replace('"', "&quot;")
    text = text.replace("'", "&apos;")
    return text


def fmt(value, fmt=">40"):
    fmt = "{:" + fmt + "}"
    try:
        value = fmt.format(value)
    except:
        pass
    return value


# ------------------------------------------------
# glom extensions
# ------------------------------------------------
def setdefault(obj, path, val, missing=dict):
    current = glom(obj, path, default=None)
    if current is None:
        assign(obj, path, val, missing=missing)
        return val
    return current


# ------------------------------------------------
# Converter functions
# ------------------------------------------------
def I(x):
    return x


def INT(x):
    return int(x)


def FLOAT(x):
    return float(x)


def BOOL(x):
    return x.lower() in ("true", "yes")


def TEXT(x):
    return x.text


def DATE(x):  # TODO
    return parser.parse(x)


def DURATION(x):  # TODO
    return timedelta(days=float(x))


def COLOR(x):
    """Task color
    Ignore when if a "black" or "blue" color and let GP
    use default ones next time.
    """
    if x not in ("#8cb6ce", "#000000"):
        return x
    return x  # TODO: remove, this hack will remove default colors


def PRIORITY(x):
    """GanttProject PRIORITY.... (have not sense :) )"""
    return {
        "3": -2,  #  Lowest
        "0": -1,  #  Low
        None: 0,  #  Normal (missing)
        "2": 1,  #  High
        "4": 2,  #  Highest
    }.get(x, 0)


# ------------------------------------------------
# console
# ------------------------------------------------

GREEN = "\033[32;1;4m"
RESET = "\033[0m"


last_sepatator = 40


def banner(
    header,
    lines=None,
    spec=None,
    sort_by=None,
    sort_reverse=True,
    output=print,
    color=GREEN,
):
    global last_sepatator
    lines = lines or []
    # compute keys spaces
    m = 1 + max([len(k) for k in lines] or [0])
    if isinstance(lines, dict):
        if sort_by:
            idx = 0 if sort_by.lower().startswith("keys") else 1
            lines = dict(
                sorted(
                    lines.items(),
                    key=lambda item: item[idx],
                    reverse=sort_reverse,
                )
            )
        _lines = []
        for k, v in lines.items():
            if spec:
                try:
                    v = glom(v, spec)
                except:
                    v = getattr(v, spec)

            line = f"{k.ljust(m)}: {v}"
            _lines.append(line)
        lines = _lines

    if lines:
        m = max([len(l) for l in lines])
        last_sepatator = m
    elif last_sepatator:
        m = last_sepatator
    else:
        m = max([40, len(header)]) - len(header) + 1

    # m = max([len(l) for l in lines] or [40, len(header)]) - len(header) + 1
    output(f"{color}{header}{' ' * m}{RESET}")
    for line in lines:
        output(line)
