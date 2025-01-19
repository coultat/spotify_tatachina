from pathlib import Path
import environ

ENV_FILE = Path(__file__).parent.parent.parent / "default.env"
env = environ.Env()
environ.Env.read_env(ENV_FILE)
