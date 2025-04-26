import os
from pathlib import Path
__all__ = ["_find_cli"]
class ThinkCellCliNotFound(LookupError): pass

DEFAULT_PPTTC_PATHS = [
    r"C:\Program Files (x86)\think-cell\ppttc.exe",
    r"C:\Program Files\think-cell\ppttc.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\think-cell\ppttc.exe")
]

def _find_cli()-> Path:
    if (env_path := os.environ.get("PPTTC_PATH")) and os.path.isfile(env_path):
        return Path(env_path)
    
    for path in DEFAULT_PPTTC_PATHS:
        if os.path.isfile(path):
            return Path(path)

    raise ThinkCellCliNotFound("Environment Variable: PPTTC_PATH, not set for the CLI path and thinkcell cli not found in:\n" +
                      "\n".join(DEFAULT_PPTTC_PATHS))