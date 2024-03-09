if [ $# -eq 0 ]; then
    export PACKAGE=tompy
else
    export PACKAGE=$1
fi

isort $PACKAGE
black $PACKAGE
mypy $PACKAGE
pylint $PACKAGE
