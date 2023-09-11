DOCKER_IMAGE_NAME:=info_portal
DOCKER_TAG_NAME:=latest

version:
		$(eval FULL_IMAGE_NAME:=${DOCKER_IMAGE_NAME}:${DOCKER_TAG_NAME})
		@echo ${FULL_IMAGE_NAME}

.PHONY: build
build: version
		docker build -t ${FULL_IMAGE_NAME} .

.PHONY: run
run: version
		docker run -p 8080:8000 -d ${FULL_IMAGE_NAME}


