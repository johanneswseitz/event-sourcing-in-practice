## Separating behaviour and state

Operations split into pure functions:

* Executing commands on an Objects produces events.
	(Command, Object) => Events
* Applying events causes state to change
	(Events, Object) => Object'