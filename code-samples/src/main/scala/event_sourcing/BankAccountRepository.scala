package event_sourcing

import java.util.UUID

trait BankAccountRepository {
  def getAccount(id:UUID) : BankAccount
  def saveAccount(account:BankAccount)
}
