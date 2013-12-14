package event_sourcing

import java.util.UUID

// depositEvent
case class DepositPerformed(account:UUID, amount:MonetaryAmount)
// depositEvent
