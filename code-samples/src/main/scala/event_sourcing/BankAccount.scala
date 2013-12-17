package event_sourcing

case class BankAccount(owner:String, private var postings :Seq[MonetaryAmount] = Seq.empty) {
  def balance = {
    var balance = MonetaryAmount(0)
    for (posting <- postings){
      balance += posting
    }
    balance
  }

  def deposit(amount:MonetaryAmount) = {
    postings :+= amount
  }

  def withdraw(amount:MonetaryAmount) = {
    postings :+= -amount
  }

  def changeOwner(newOwner:String) = {
    this.copy(owner = newOwner)
  }
}
