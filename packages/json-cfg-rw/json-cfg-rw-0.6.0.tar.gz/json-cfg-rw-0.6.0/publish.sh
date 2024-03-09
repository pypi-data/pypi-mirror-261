#!/usr/bin/env bash

PACKAGE="json-cfg-rw"

set -o nounset
set -o errexit
#set -x

if [ -n "$(git status --porcelain)" ]; then
    echo "There are uncommitted changes, please make sure all changes are committed" >&2
    exit 1
fi

if ! [ -f "pyproject.toml" ]
then
    echo "publish.sh must be run in the directory where setup.py is" >&2
    exit 1
fi

VER="${1:?You must pass a version of the format 0.0.0 as the only argument}"

if git tag | grep -q "${VER}"
then
    echo "Git tag for version ${VER} already exists." >&2
    exit 1
fi

echo "Setting version to $VER"

# Update the package version
sed -i "s;^version = .*;version = \"${VER}\";" pyproject.toml

rm -f dist/*

# Upload to test pypi
python -m build --sdist

#
twine upload dist/*.tar.gz

# Reset the commit, we don't want versions in the commit
git commit -a -m "Updated to version ${VER}"

git tag ${VER}
git push
git push --tags

