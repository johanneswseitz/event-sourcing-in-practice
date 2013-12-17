package event_sourcing

import event_sourcing.events.DomainEvent

object EventBus {
  var eventStream = Seq.empty[DomainEvent]

  def publishEvent(event:DomainEvent) : Unit = {
    eventStream :+= event
    print(event + " published")
  }
}
