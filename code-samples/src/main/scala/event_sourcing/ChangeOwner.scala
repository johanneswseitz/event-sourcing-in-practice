package event_sourcing

// changeOwnerCommand
class ChangeOwner(newOwner:String) extends Command[BankAccount] {
  def execute(bankAccount:BankAccount): BankAccount = {
    bankAccount.changeOwner(newOwner)
  }
}
// changeOwnerCommand
