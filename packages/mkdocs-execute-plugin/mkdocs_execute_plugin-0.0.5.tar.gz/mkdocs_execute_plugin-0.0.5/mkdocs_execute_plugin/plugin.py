import os
import uuid
from pathlib import Path

import jupytext
import mkdocs
import nbconvert
from mkdocs.config import config_options as c
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import File, Files
from nbconvert.preprocessors import ExtractOutputPreprocessor
from traitlets.config import Config

from . import utils

# Based on https://gitlab.kwant-project.org/solidstate/lectures/-/blob/b424707f5aeba31f276bfd0495f82a852750a2d2/execute.py

output_extractor = ExtractOutputPreprocessor()
output_extractor.extract_output_types = output_extractor.extract_output_types | {
    "application/vnd.plotly.v1+json"
}


class AlreadySavedFile(File):
    def copy_file(self, dirty=False):
        pass


exporter = nbconvert.TemplateExporter(
    config=Config(
        dict(
            TemplateExporter=dict(
                preprocessors=[
                    nbconvert.preprocessors.ExecutePreprocessor,
                    output_extractor,
                ],
                exclude_input=False,
                template_file="markdown/index.md.j2",
            ),
            NbConvertBase=dict(
                display_data_priority=[
                    "application/vnd.plotly.v1+json",
                    "text/html",
                    "text/markdown",
                    "image/svg+xml",
                    "text/latex",
                    "image/png",
                    "image/jpeg",
                    "text/plain",
                ]
            ),
        )
    )
)


class ExecutableFile(File):
    """A file that should be executed. This is a wrapper around the mkdocs File"""

    # Based on https://github.com/danielfrg/mkdocs-jupyter/blob/93bb183544dc024b4de2a0c9341328ae7317e3db/src/mkdocs_jupyter/plugin.py#L15

    def __init__(self, file, use_directory_urls, site_dir, **kwargs):
        self.file = file
        self.dest_path = self._get_dest_path(use_directory_urls)
        self.abs_dest_path = str((Path(site_dir) / self.dest_path).resolve())
        self.url = self._get_url(use_directory_urls)

    def __getattr__(self, item):
        return self.file.__getattribute__(item)

    def is_documentation_page(self) -> bool:
        return True


class ExecuteConfig(mkdocs.config.base.Config):
    include = c.ListOfItems(c.PathSpec(), default=["*.py", "*.md"])
    exclude = c.ListOfItems(c.PathSpec(), default=[])
    execute_tag_name = c.Type(str, default="execute")
    execute_without_tag = c.ListOfItems(c.PathSpec(), default=["*.py"])


class ExecutePlugin(BasePlugin[ExecuteConfig]):
    def __init__(self):
        self.output_map = {}
        # TODO: Is this the right place to configure this?
        os.environ["PLOTLY_RENDERER"] = "plotly_mimetype"

    def on_files(self, files, config):
        return Files(
            [
                ExecutableFile(file, **config) if self._should_execute(file) else file
                for file in files
            ]
        )

    def on_page_read_source(self, page, config, **kwargs):
        if not isinstance(page.file, ExecutableFile):
            return

        abs_src_path = Path(page.file.abs_src_path)
        with abs_src_path.open("r") as notebook_file:
            notebook = jupytext.read(notebook_file)

        src_dir = Path(page.file.src_path).parent
        build_directory = Path(config.site_dir) / src_dir
        output, resources = exporter.from_notebook_node(
            notebook,
            resources={
                "unique_key": abs_src_path.name,
                # Compute the relative URL
                "output_files_dir": "_execute_outputs",
                "metadata": {"path": abs_src_path.parent},
            },
        )
        temporary_file_name = f"{str(uuid.uuid4())}.md"
        nbconvert.writers.FilesWriter(build_directory=str(build_directory)).write(
            output, resources, temporary_file_name
        )
        temporary_file_path = build_directory / temporary_file_name
        source = temporary_file_path.read_text()
        temporary_file_path.unlink()
        self.output_map[str(abs_src_path)] = list(
            src_dir / output for output in resources["outputs"].keys()
        )
        return source

    def on_page_markdown(self, markdown, page, config, files):
        src_path = page.file.abs_src_path
        if src_path not in self.output_map:
            return

        for file in self.output_map.pop(src_path):
            files.append(
                AlreadySavedFile(
                    str(file),
                    config.docs_dir,
                    config.site_dir,
                    config.use_directory_urls,
                )
            )

    def _should_execute(self, file: File):
        src_path = Path(file.src_path)

        def matches_any(globs):
            for glob in globs:
                if glob.match_file(src_path):
                    return True

        if not matches_any(self.config.include):
            return False

        if matches_any(self.config.exclude):
            return False

        if utils.is_markdown_file(file.src_path):
            # Jupytext does not preserve markdown metadata, so we extract from markdown directly
            extract_tag = utils.extract_tag_markdown
        else:
            extract_tag = utils.extract_tag_jupytext

        has_execute_tag, execute_tag_value = extract_tag(
            file.abs_src_path, self.config.execute_tag_name
        )

        if not has_execute_tag and matches_any(self.config.execute_without_tag):
            return True

        return has_execute_tag and utils.is_truthy(execute_tag_value)
