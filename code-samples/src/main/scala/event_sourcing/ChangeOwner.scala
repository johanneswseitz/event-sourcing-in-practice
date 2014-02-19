package event_sourcing

import java.util.UUID

// changeOwnerCommand
case class ChangeOwner(accountID: UUID, newOwner:String)
  extends Command

class BankAccountCommandHandler(repo:BankAccountRepository) {
  def handle(changeOwner:ChangeOwner) {
    val accountId = changeOwner.accountID
    val newOwner = changeOwner.newOwner
    val account = repo.getAccount(accountId)
    val modifiedAccount = account.changeOwner(newOwner)
    repo.saveAccount(modifiedAccount)
  }
}
// changeOwnerCommand
