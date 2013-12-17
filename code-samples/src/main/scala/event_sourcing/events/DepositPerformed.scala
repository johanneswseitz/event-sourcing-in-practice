package event_sourcing.events

import java.util.UUID
import event_sourcing.MonetaryAmount

// depositEvent
case class DepositPerformed(account:UUID, amount:MonetaryAmount) extends DomainEvent
// depositEvent
