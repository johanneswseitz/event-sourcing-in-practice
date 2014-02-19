package event_sourcing

import java.util.UUID
import event_sourcing.events.DomainEvent

abstract class Order
case class BuyOrder(amount:MonetaryAmount, isin:String) extends Order
case class PerformBuyOrder(orderBookId:UUID, order:BuyOrder) extends Command
case class OrderConfirmation(orderId:UUID, order:BuyOrder)
case class OrderSentToBank(orderId:UUID, order:BuyOrder) extends DomainEvent
object OrderSentToBank {
  def from(orderConfirmation:OrderConfirmation) = {
    OrderSentToBank(orderConfirmation.orderId, orderConfirmation.order)
  }
}

// dealingWithSideEffects

class BrokerCommandHandler(bank:BankInterface,
                           repo:OrderBookRepository) {
  def handle(buyCommand:PerformBuyOrder) = {
    var orderBook = repo.load(buyCommand.orderBookId)
    val validationResult = bank.validate(buyCommand.order)
    if (!validationResult.succeeded)
      throw new InvalidOrderException(validationResult)

    val confirmation = bank.perform(buyCommand.order)
    val orderDoneEvent = OrderSentToBank.from(confirmation)
    orderBook = orderBook.handle(orderDoneEvent)
    repo.save(orderBook)
  }
}
// dealingWithSideEffects

case class OrderBook(orders:Seq[Order] = Seq.empty) {
  def handle(orderSentToBank:OrderSentToBank) : OrderBook = {
    this.copy(orders :+ orderSentToBank.order)
  }
}


trait BankInterface {
  def validate(order:BuyOrder) : ValidationResult
  def perform(order:BuyOrder) : OrderConfirmation
}

class InvalidOrderException(validationResult:ValidationResult) extends RuntimeException(validationResult.toString)

case class ValidationResult(succeeded:Boolean)
case class OrderFailedEvent(validationResult:ValidationResult) extends DomainEvent

trait OrderBookRepository {
  def load(orderBookID:UUID) : OrderBook
  def save(orderBook:OrderBook)
}