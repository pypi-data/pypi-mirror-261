# Set this to true to override the builtin `source` command and enable
# sourcing python files directly in addition to regular shell scripts.
: ${SOURCEPY_OVERLOAD_SOURCE:=true}

# Set this to true to override the builtin `which` command and enable
# retrieving the original python function definition rather than the
# shell wrapper function definition.
: ${SOURCEPY_OVERLOAD_WHICH:=true}

# Override the sourcepy installation directory
: ${SOURCEPY_DIR:="$(dirname ${BASH_SOURCE[0]:-${(%):-%x}})/../src"}

####### script start


sourcepy() {
    local _python3=${PYTHONEXECUTABLE:-$(which python3)}
    #local module_wrapper=$($_python3 -m sourcepy.source $1)
    #builtin source $module_wrapper
    source <( PYTHONPATH="${SOURCEPY_DIR}" $_python3 -m sourcepy.source $1 )
}

if $SOURCEPY_OVERLOAD_SOURCE
then
    source() {
        for sourcefile in "$@"
        do
            local extension="${sourcefile##*.}"
            if [[ "$extension" == "py" ]]
            then
                sourcepy $sourcefile
            else
                builtin source $sourcefile
            fi
        done
    }

    alias .=source
fi


if $SOURCEPY_OVERLOAD_WHICH
then
    which() {
        for bin in "$@"
        do
            local which_out=$(builtin which $bin)
            if [[ $which_out == *"sourcepy_run"* ]]
            then
                SOURCEPY_WHICH=1 $bin
            else
                echo $which_out
            fi
        done
    }
fi
