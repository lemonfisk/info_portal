DOCKER_IMAGE_NAME:=info_portal
DOCKER_TAG_NAME:=latest

.PHONY: build
build:
    docker build -t ${DOCKER_IMAGE_NAME}:${DOCKER_TAG_NAME} .



.PHONY: run
run:
    docker run ${DOCKER_IMAGE_NAME}:${DOCKER_TAG_NAME}