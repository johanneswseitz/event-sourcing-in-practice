present: build
	open -a "Google Chrome" .build/index.html

start: build
	cactus serve

build: 
	cactus build

test-code:
	(cd code-samples && sbt test)

clean:
	rm -rf .build
	(cd code-samples && sbt clean)
