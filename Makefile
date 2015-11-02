OS := $(shell uname)

present: build
ifeq ($(OS), Darwin)
	open -a "Google Chrome" .build/index.html
else 
	firefox ./.build/index.html
endif

start: build
	cactus serve

build: 
	cactus build

test-code:
	(cd code-samples && sbt test)

clean:
	rm -rf .build
	(cd code-samples && sbt clean)
