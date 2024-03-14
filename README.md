# mkdocs_draw.io_templates

Populate a Draw.io diagram template with dynamic data and embed it in a mkdocs site

This is a proof-of-concept for generating infrastructure diagrams for project documentation using cloud provider data.

---

## Pre-requisites

- [Draw.io](https://app.diagrams.net/)
- Docker and Docker Compose

---

## Usage

1. Create a [Draw.io](https://www.drawio.com/) diagram using Jinja2 syntax for applicable labels

2. Save the diagram to `docs/_diagrams` in the XML-based `.drawio` format

3. Use [`mkdocs-drawio-file`](https://pypi.org/project/mkdocs-drawio-file/) to reference your diagram in a Markdown file in `docs/`

    ```text
    ![](<DIAGRAM_NAME>.drawio)
    ```

4. Modify the `get_context()` function in `render_diagrams.py` to fetch your desired dynamic data

5. Build the Docker image

    ```bash
    # Using Docker CLI
    docker build --tag docs .

    # Using Docker Compose
    docker-compose build
    ```

6. Start the container

    ```bash
    # Docker CLI
    docker run --name docs --detach --restart unless-stopped --publish 8000:80 docs:latest

    # Docker Compose
    docker-compose up -d
    ```

7. Navigate to [`http://localhost:8000`](http://localhost:8000) in your browser
