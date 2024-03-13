# 无依赖的
from .Vtype._core import (
    vbool, vtrue, vfalse,
    bidict, vdict, vstr, vbytes,
    ToolPool, jsonChinese, readJson, writeJson,
    cut_data, getGroupNumber,
    check_dir, check_parent_dir,
    system_type, ternary, repairPathClash, uniform_put, cool_iter, limit_input,
    creat_vtrue_instance, creat_vfalse_instance, get_chrome_path,
)
from .Vtype._core import undefined as _undefined
from .Coolstr._core import coolstr
from .Cooltime._core import cooltime
from .Rslice._core import rslice

# 有依赖的