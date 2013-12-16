package event_sourcing


import event_sourcing.{BankAccount, ChangeOwner}
import org.specs2.mutable._
import org.specs2.runner.JUnitRunner
import org.junit.runner.RunWith

@RunWith(classOf[JUnitRunner])
class ChangeOwnerSpec extends Specification {

  "The Change Owner Command" should {
    "change the owner of a bank account, when executed" in {
      val originalBankAccount = new BankAccount("John Doe")
      val newOwner = "Jane Doe"
      val changeOwner = new ChangeOwner(newOwner)

      val modifiedBankAccount = changeOwner.execute(originalBankAccount)

      modifiedBankAccount.owner mustEqual newOwner
    }
  }

}
