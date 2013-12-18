package event_sourcing

import java.util.UUID

// changeOwnerCommand
case class ChangeOwner(accountID: UUID, newOwner:String)
  extends Command

class BankAccountCommandHandler
     (bankAccountRepo:BankAccountRepository) {
  def handle(changeOwner:ChangeOwner) {
    val accountId = changeOwner.accountID
    val newOwner = changeOwner.newOwner
    val account = bankAccountRepo.getAccount(accountId)
    val modifiedAccount = account.changeOwner(newOwner)
    bankAccountRepo.saveAccount(modifiedAccount)
  }
}
// changeOwnerCommand
