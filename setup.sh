#! /usr/bin/env bash

# download required files
git clone https://github.com/rambasnet/course-container.git
rm -rf course-container/.git
rm course-container/README.md
rm course-container/setup.sh
rm course-container/.gitignore
rm course-container/LICENSE
rm -rf course-container/hello
rm -rf course-container/cold
cp -r course-container/. ./
rm -rf course-container
git config core.hooksPath .githooks
echo "Downloaded required files"
