# Creates Draw.io diagrams using dynamic data
#
# Reads Draw.io diagram files containing Jinja2 templating language, renders them with Jinja2, and writes the rendered
# diagram file to disk
#
# Intended for use with mkdocs and the mkdocs-drawio-file plugin

# Standard Libraries
import logging
from pathlib import Path

# Third-party Libraries
from jinja2 import Environment
from jinja2 import FileSystemLoader


# =================================================================================================
#                                      Configurable Constants
# =================================================================================================

# The directory containing documentation source files
DOCS_DIR: Path = Path("docs")

# The directory containing diagram templates to be rendered
DIAGRAM_SRC_DIR: Path = DOCS_DIR / "_diagrams"


# =================================================================================================
#                                          Rendering Code
# =================================================================================================

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

environment = Environment(loader=FileSystemLoader(DIAGRAM_SRC_DIR), autoescape=True)


def get_context() -> dict[str, str]:
    # TODO: Look up dynamic info to use in the diagram (e.g., query cloud provider)
    context = {
        "proxy_fqdn": "proxy.example.com",
        "proxy_ip": "10.10.14.2",
        "web_server_fqdn": "web.example.com",
        "web_server_ip": "192.168.1.207",
    }

    return context


def render_diagram(template_name: str) -> str:
    logger.info(f"[*] Rendering '{template_name}'")

    return environment.get_template(template_name).render(get_context())


def write_diagram(filepath: Path, content: str) -> None:
    logger.info(f"[*] Writing '{filepath}'")

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)

    logger.info(f"[+] Finished writing '{filepath}'")


def write_diagrams() -> None:
    # Loop through all the diagrams
    for template in DIAGRAM_SRC_DIR.glob("*.drawio"):
        diagram_content: str = render_diagram(template.name)
        write_diagram(DOCS_DIR / template.name, diagram_content)


if __name__ == "__main__":
    write_diagrams()
