#!/bin/sh

set -e

echo "mounts ===="
echo "==========="

cat /proc/1/mounts

echo '--------------------------------------------'

echo "pwd"
echo "==="
pwd

echo '--------------------------------------------'

echo "script arguments"
echo "================"
echo ${@}
