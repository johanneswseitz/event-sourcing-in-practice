## Solution 1: Separate side-effect and state change

* Execute command on object. This triggers side-effects produces events

    `Command -> Object -> Events`

* Applying Events causes state to change

    `Object -> Event -> Changed Object`

**Only the event (=state change) is being replayed.**
