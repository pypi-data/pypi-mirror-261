import contextlib
import os
import sys
import textwrap
from pathlib import Path

from sourcepy.casters import cast_to_shell, get_typedef
from sourcepy.loaders import load_path, module_definitions



if sourcepy_dir := os.environ.get('SOURCEPY_DIR'):
    SOURCEPY_DIR = Path(sourcepy_dir).resolve()
else:
    SOURCEPY_DIR = Path(__file__).resolve().parent.parent


def make_var(name: str, value: object) -> str:
    typedef = get_typedef(value)
    value = cast_to_shell(value)
    var_def = textwrap.dedent(f"""\
        declare {('-g ' + typedef).strip()} {name}
        {name}={value}
    """)
    return var_def


def make_fn(name: str, runner_name: str) -> str:
    fn_def = textwrap.dedent(f"""\
        {name}() {{
            {runner_name} {name} "$@" \\
                | while IFS='' read -r line ; do
                    if [[ "$line" == "CMD::"* ]]; then
                        eval "${{line#'CMD::'}}"
                        continue
                    fi
                    echo "$line"
                done
        }}
    """)
    return fn_def


def make_runner(runner_name: str, module_path: Path) -> str:
    runner = textwrap.dedent(f"""\
        {runner_name}() {{
            PYTHONPATH={SOURCEPY_DIR} \
                {sys.executable} -m sourcepy.run \
                {module_path} "$@"
        }}
    """)
    return runner


def make_wrapper_name(path: Path) -> str:
    """Return an escaped filename to be used in source wrappers.
    Reverses the order of parts from the original filepath for
    easier readability
    """
    escaped = '_'.join(reversed(path.parts))
    for char in '. /':
        escaped = escaped.replace(char, '_')
    return escaped + '.sh'


def build_wrapper(module_path: Path) -> str:
    wrapper_contents = []

    module = load_path(module_path)
    wrapper_title = f'Sourcepy wrapper for {module.__name__} ({module_path})'
    wrapper_contents.append(textwrap.dedent(f"""\
        ######{"#" * len(wrapper_title)}######
        ##### {wrapper_title} #####
        ######{"#" * len(wrapper_title)}######
    """))

    runner_name = f'_sourcepy_run_{hash(module)}'
    runner = make_runner(runner_name, module_path)
    wrapper_contents.append('# Sourcepy runner')
    wrapper_contents.append(runner)

    wrapper_contents.append('\n# Definitions')
    for obj_definition in module_definitions(module):
        name = obj_definition['name']
        if obj_definition['type'] == 'function':
            fn_def = make_fn(name, runner_name)
            wrapper_contents.append(fn_def)
        elif obj_definition['type'] == 'variable':
            var_def = make_var(name, obj_definition['value'])
            wrapper_contents.append(var_def)
    wrapper = '\n'.join(wrapper_contents)
    return wrapper


def source(path: str) -> None:
    with contextlib.redirect_stdout(sys.stderr):
        module_path = Path(path).resolve()
        wrapper_contents = build_wrapper(module_path)
        wrapper_name = make_wrapper_name(module_path)
    print(wrapper_contents)


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("sourcepy.source: not enough arguments")
    source(sys.argv[1])


if __name__ == '__main__':
    main()
