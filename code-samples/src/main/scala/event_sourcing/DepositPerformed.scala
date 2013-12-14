package event_sourcing

import java.util.UUID

case class DepositPerformed(account:UUID, amount:MonetaryAmount)