#!/bin/bash
set -euo pipefail

container=""

# Let the container live at max 3600s (1 hour)
cmdline="sleep 3600"

function cleanup() {
	docker rm -f "${container}"
}
trap cleanup EXIT

container=$(docker run -d --env IEULER_SERVER_HOST=ieuler-server --env IEULER_SERVER_PORT=2718 --network interactive-project-euler_default liamcryan/ieuler bash -c "${cmdline}")

if [ -z "${container}" ]; then
	echo "Failed to obtain container ID"
	exit 1
fi

docker exec -ti "${container}" ./init.sh "$@"
