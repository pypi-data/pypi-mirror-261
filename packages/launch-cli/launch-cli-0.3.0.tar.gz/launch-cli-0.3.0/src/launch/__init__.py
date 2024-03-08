from semver import Version

VERSION = "0.3.0"

SEMANTIC_VERSION = Version.parse(VERSION)
GITHUB_ORG_NAME = "nexient-llc"
GITHUB_REPO_NAME = "launch-cli"
SERVICE_SKELETON = "https://github.com/nexient-llc/launch-terragrunt-skeleton.git"
SKELETON_BRANCH = "main"
MAIN_BRANCH = "main"
INIT_BRANCH = "feature/init"
DISCOVERY_FORBIDDEN_DIRECTORIES = [
    ".git",
    "components",
    ".repo",
    "__pycache__",
    ".venv",
    ".terraform",
    ".terragrunt-cache",
]
