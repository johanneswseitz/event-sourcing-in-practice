## Should I be doing Event Sourcing?

Event Sourcing is probably a good fit when ...

- you're building rich object-oriented domain models (e.g. DDD) 
- you have a lot of behaviour that isn't CRUD
- accountability/debugability is critical
- you need version control/undo for data (e. G. Wikis, Google Docs)
- your business derives value or competitive advantage from event data
- your domain is inherently event driven (e. G. basketball game tracking)
- you're building a scaleable system based on the CQRS pattern
