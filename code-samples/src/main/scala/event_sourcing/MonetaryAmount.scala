package event_sourcing

case class MonetaryAmount(amount:Long){
  def +(other:MonetaryAmount) = {
    MonetaryAmount(this.amount + other.amount)
  }

  def -(other:MonetaryAmount) = {
    MonetaryAmount(this.amount - other.amount)
  }

  def unary_- = {
    MonetaryAmount(-amount)
  }
}