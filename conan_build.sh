#!/bin/bash
conan install . --build=missing -s build_type=RelWithDebInfo
conan install . --build=missing -s build_type=Debug
conan build . -s build_type=RelWithDebInfo
conan build . -s build_type=Debug