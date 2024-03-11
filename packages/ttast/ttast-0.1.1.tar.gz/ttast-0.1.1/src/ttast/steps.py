
import yaml
import sys
import re
import glob

from .util import *
from . import pipeline

def get_handler_class(step_type):
    validate(isinstance(step_type, str), "Invalid step_type passed to get_handler")

    if step_type == "config":
        return PipelineStepConfig

    elif step_type == "import":
        return PipelineStepImport

    elif step_type == "stdin":
        return PipelineStepStdin

    elif step_type == "stdin_yaml":
        return PipelineStepStdinYaml

    elif step_type == "meta":
        return PipelineStepMeta

    elif step_type == "stdout":
        return PipelineStepStdout

    elif step_type == "replace":
        return PipelineStepReplace

    elif step_type == "template":
        return PipelineStepTemplate

    else:
        raise PipelineRunException(f"Invalid step type in step {step_type}")

class PipelineStepConfig:
    """
    """
    def __init__(self, step_instance):
        validate(isinstance(step_instance, pipeline.PipelineStepInstance), "Invalid step_instance passed to PipelineStepConfig")

        self.step_instance = step_instance
        self.pipeline = self.step_instance.pipeline
        self.block = step_instance.block

        # Read the content from the file and use _process_config_content to do the work
        config_file = pop_property(step_instance.step_def, "file", template_map=self.step_instance.vars)
        validate(isinstance(config_file, str) or config_file is None, "Step 'config_file' must be a string or absent")
        validate(not isinstance(config_file, str) or config_file != "", "Step 'config_file' cannot be empty")
        self.config_file = config_file

        # Extract the content var, which can be either a dict or yaml string
        config_content = pop_property(step_instance.step_def, "content", template_map=self.step_instance.vars)
        validate(isinstance(config_content, (str, dict)) or config_content is None, "Step 'config_content' must be a string, dict or absent")
        self.config_content = config_content

        # Extract stdin bool, indicating whether to read config from stdin
        stdin = pop_property(step_instance.step_def, "stdin", template_map=self.step_instance.vars, default=False)
        validate(isinstance(stdin, (bool, str)), "Step 'stdin' must be a bool, bool like string or absent")
        stdin = parse_bool(stdin)
        self.stdin = stdin

    def per_block():
        return False

    def process(self):
        if self.config_file is not None:
            logger.debug(f"config: including config from file {self.config_file}")
            with open(self.config_file, "r", encoding='utf-8') as file:
                content = file.read()

            self._process_config_content(content)

        # Call _process_config_content, which can determine whether to process as string or dict
        if self.config_content is not None:
            logger.debug(f"config: including inline config")
            self._process_config_content(self.config_content)

        if self.stdin:
            # Read configuration from stdin
            logger.debug(f"config: including stdin config")
            stdin_content = sys.stdin.read()
            self._process_config_content(stdin_content)

    def _process_config_content(self, content):
        validate(isinstance(content, (str, dict)), "Included configuration must be a string or dictionary")

        # Parse yaml if it is a string
        if isinstance(content, str):
            content = yaml.safe_load(content)

        validate(isinstance(content, dict), "Parsed configuration is not a dictionary")

        # Extract vars from the config
        config_vars = pop_property(content, "vars", template_map=self.step_instance.vars, default={})
        validate(isinstance(config_vars, dict), "Config 'vars' is not a dictionary")

        for config_var_name in config_vars:
            self.pipeline.vars[config_var_name] = config_vars[config_var_name]

        # Extract pipeline steps from the config
        config_pipeline = pop_property(content, "pipeline", template_map=None, default=[])
        validate(isinstance(config_pipeline, list), "Config 'pipeline' is not a list")

        for step in config_pipeline:
            validate(isinstance(step, dict), "Pipeline entry is not a dictionary")

            self.pipeline.add_step(step)

        # Validate config has no other properties
        validate(len(content.keys()) == 0, f"Found unknown properties in configuration: {content.keys()}")


class PipelineStepImport:
    """
    """
    def __init__(self, step_instance):
        validate(isinstance(step_instance, pipeline.PipelineStepInstance), "Invalid step_instance passed to PipelineStepImport")

        self.step_instance = step_instance
        self.pipeline = self.step_instance.pipeline
        self.block = step_instance.block

        import_files = pop_property(step_instance.step_def, "files", template_map=self.step_instance.vars)
        validate(isinstance(import_files, list), "Step 'files' must be a list of strings")
        validate(all(isinstance(x, str) for x in import_files), "Step 'files' must be a list of strings")
        self.import_files = import_files

        recursive = pop_property(step_instance.step_def, "recursive", template_map=self.step_instance.vars)
        validate(isinstance(recursive, (bool, str)), "Step 'recursive' must be a bool or bool like string")
        recursive = parse_bool(recursive)
        self.recursive = recursive

    def per_block():
        return False

    def process(self):
        filenames = set()
        for import_file in self.import_files:
            logger.debug(f"import: processing file glob: {import_file}")
            matches = glob.glob(import_file, recursive=self.recursive)
            for match in matches:
                filenames.add(match)

        # Ensure consistency for load order
        filenames = list(filenames)
        filenames.sort()

        for filename in filenames:
            logger.debug(f"import: reading file {filename}")
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()
                new_block = pipeline.TextBlock(content, tags=self.step_instance.apply_tags)
                new_block.meta["filename"] = filename
                self.pipeline.blocks.append(new_block)


class PipelineStepMeta:
    """
    """
    def __init__(self, step_instance):
        validate(isinstance(step_instance, pipeline.PipelineStepInstance), "Invalid step_instance passed to PipelineStepMeta")

        self.step_instance = step_instance
        self.pipeline = self.step_instance.pipeline
        self.block = step_instance.block

        vars = pop_property(step_instance.step_def, "vars", template_map=self.step_instance.vars)
        validate(isinstance(vars, dict), "Step 'vars' must be a dictionary of strings")
        validate(all(isinstance(x, str) for x in vars), "Step 'vars' must be a dictionary of strings")
        self.vars = vars

    def per_block():
        return True

    def process(self):
        logger.debug(f"meta: document tags: {self.block.tags}")
        logger.debug(f"meta: document meta: {self.block.meta}")

        for key in self.vars:
            self.block.meta[key] = self.vars[key]


class PipelineStepReplace:
    """
    """
    def __init__(self, step_instance):
        validate(isinstance(step_instance, pipeline.PipelineStepInstance), "Invalid step_instance passed to PipelineStepReplace")

        self.step_instance = step_instance
        self.pipeline = self.step_instance.pipeline
        self.block = step_instance.block

        replace = pop_property(step_instance.step_def, "replace", template_map=self.step_instance.vars, default={})
        validate(isinstance(replace, list), "Step 'replace' must be a list")
        validate(all(isinstance(x, dict) for x in replace), "Step 'replace' items must be dictionaries")
        for item in replace:
            validate('key' in item and isinstance(item['key'], str), "Step 'replace' items must contain a string 'key' property")
            validate('value' in item and isinstance(item['value'], str), "Step 'replace' items must contain a string 'value' property")
        self.replace = replace

        regex = pop_property(step_instance.step_def, "regex", template_map=self.step_instance.vars, default=False)
        validate(isinstance(regex, (bool, str)), "Step 'regex' must be a bool, bool like string or absent")
        regex = parse_bool(regex)
        self.regex = regex

    def per_block():
        return True

    def process(self):
        logger.debug(f"replace: document tags: {self.block.tags}")
        logger.debug(f"replace: document meta: {self.block.meta}")

        for replace_item in self.replace:
            # Copy the dictionary as we'll change it when removing values
            replace_item = replace_item.copy()

            replace_key = replace_item['key']
            replace_value = replace_item['value']

            replace_regex = pop_property(replace_item, "regex", template_map=self.step_instance.vars, default=False)
            validate(isinstance(replace_regex, (bool, str)), "Replace item 'regex' must be a bool, bool like string or absent")
            replace_regex = parse_bool(replace_regex)

            # replace_value isn't templated by pop_property as it is a list of dictionaries, so it
            # needs to be manually done here
            replace_value = template_if_string(replace_value, self.step_instance.vars)

            logger.debug(f"replace: replacing regex({self.regex or replace_regex}): {replace_key} -> {replace_value}")

            if self.regex or replace_regex:
                self.block.block = re.sub(replace_key, replace_value, self.block.block)
            else:
                self.block.block = self.block.block.replace(replace_key, replace_value)


class PipelineStepStdinYaml:
    """
    """
    def __init__(self, step_instance):
        validate(isinstance(step_instance, pipeline.PipelineStepInstance), "Invalid step_instance passed to PipelineStepStdinYaml")

        self.step_instance = step_instance
        self.pipeline = self.step_instance.pipeline
        self.block = step_instance.block

        strip = pop_property(step_instance.step_def, "strip", template_map=self.step_instance.vars, default=False)
        validate(isinstance(strip, (bool, str)), "Step 'strip' must be a bool or str value")
        strip = parse_bool(strip)
        self.strip = strip

    def per_block():
        return False

    def process(self):
        # Read content from stdin
        logger.debug("stdin_yaml: reading yaml document from stdin")
        stdin_lines = sys.stdin.read().splitlines()

        documents = []
        current = []

        for line in stdin_lines:

            # Determine if we have the beginning of a yaml document
            if line == "---" and len(current) > 0:
                documents.append("\n".join(current))
                current = []

            current.append(line)

        documents.append("\n".join(current))

        # Strip each document, if required
        if self.strip:
            documents = [x.strip() for x in documents]

        # Add all documents to the pipeline text block list
        for item in documents:
            self.pipeline.blocks.append(pipeline.TextBlock(item, tags=self.step_instance.apply_tags))


class PipelineStepStdin:
    """
    """
    def __init__(self, step_instance):
        validate(isinstance(step_instance, pipeline.PipelineStepInstance), "Invalid step_instance passed to PipelineStepStdin")

        self.step_instance = step_instance
        self.pipeline = self.step_instance.pipeline
        self.block = step_instance.block

        split = pop_property(step_instance.step_def, "split", template_map=self.step_instance.vars)
        validate(isinstance(split, str) or split is None, "Step 'split' must be a string")
        self.split = split

        strip = pop_property(step_instance.step_def, "strip", template_map=self.step_instance.vars, default=False)
        validate(isinstance(strip, (bool, str)), "Step 'strip' must be a bool or str value")
        strip = parse_bool(strip)
        self.strip = strip

    def per_block():
        return False

    def process(self):
        # Read content from stdin
        logger.debug("stdin: reading document from stdin")
        stdin_content = sys.stdin.read()

        # Split if required and convert to a list of documents
        if self.split is not None and self.split != "":
            stdin_items = stdin_content.split(self.split)
        else:
            stdin_items = [stdin_content]

        # strip leading and trailing whitespace, if required
        if self.strip:
            stdin_items = [x.strip() for x in stdin_items]

        # Add the stdin items to the list of text blocks
        for item in stdin_items:
            self.pipeline.blocks.append(pipeline.TextBlock(item, tags=self.step_instance.apply_tags))


class PipelineStepStdout:
    """
    """
    def __init__(self, step_instance):
        validate(isinstance(step_instance, pipeline.PipelineStepInstance), "Invalid step_instance passed to PipelineStepStdout")

        self.step_instance = step_instance
        self.pipeline = self.step_instance.pipeline
        self.block = step_instance.block

        prefix = pop_property(step_instance.step_def, "prefix", template_map=self.step_instance.vars)
        validate(isinstance(prefix, str) or prefix is None, "Step 'prefix' must be a string")
        self.prefix = prefix

        suffix = pop_property(step_instance.step_def, "suffix", template_map=self.step_instance.vars)
        validate(isinstance(suffix, str) or suffix is None, "Step 'suffix' must be a string")
        self.suffix = suffix

    def per_block():
        return True

    def process(self):
        logger.debug(f"stdout: document tags: {self.block.tags}")
        logger.debug(f"stdout: document meta: {self.block.meta}")

        if self.prefix is not None:
            print(self.prefix)

        print(self.block.block)

        if self.suffix is not None:
            print(self.suffix)


class PipelineStepTemplate:
    """
    """
    def __init__(self, step_instance):
        validate(isinstance(step_instance, pipeline.PipelineStepInstance), "Invalid step_instance passed to PipelineStepTemplate")

        self.step_instance = step_instance
        self.pipeline = self.step_instance.pipeline
        self.block = step_instance.block

        vars = pop_property(step_instance.step_def, "vars", template_map=self.step_instance.vars)
        validate(isinstance(vars, dict) or vars is None, "Step 'vars' must be a dictionary or absent")
        self.vars = vars

        merge_vars = pop_property(step_instance.step_def, "merge_vars", template_map=self.step_instance.vars, default=True)
        validate(isinstance(merge_vars, (str, bool)), "Step 'merge_vars' must be a bool, bool like string or absent")
        merge_vars = parse_bool(merge_vars)
        self.merge_vars = merge_vars

    def per_block():
        return True

    def process(self):
        template_vars = self.step_instance.vars.copy()

        if self.vars is not None:
            for key in self.vars:
                template_vars[key] = self.vars[key]

        environment = jinja2.Environment()

        logger.debug(f"template: document tags: {self.block.tags}")
        logger.debug(f"template: document meta: {self.block.meta}")

        template = environment.from_string(self.block.block)
        self.block.block = template.render(template_vars)
