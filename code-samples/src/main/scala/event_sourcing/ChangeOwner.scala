package event_sourcing

import java.util.UUID

// changeOwnerCommand
class BankAccountCommandHandler(bankAccountRepo:BankAccountRepository) {
  def handle(changeOwner:ChangeOwner) {
    val account = bankAccountRepo.getAccount(changeOwner.accountID)
    val modifiedAccount = account.changeOwner(changeOwner.newOwner)
    bankAccountRepo.saveAccount(modifiedAccount)
  }
}

case class ChangeOwner(accountID: UUID, newOwner:String) extends Command
// changeOwnerCommand
