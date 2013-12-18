package event_sourcing


import org.specs2.mutable._
import org.specs2.runner.JUnitRunner
import org.junit.runner.RunWith

@RunWith(classOf[JUnitRunner])
class BankAccountSpec extends Specification {
  isolated

  "the Bank Account" should {
      val bankAccount = new BankAccount(owner="John Doe")

    "start out with a balance of 0" in {
      bankAccount.balance mustEqual MonetaryAmount(0)
    }

    "have a way to deposit money" in {
      bankAccount.deposit(MonetaryAmount(10))

      bankAccount.balance mustEqual MonetaryAmount(10)
    }

    "have a way to withdraw money" in {
      bankAccount.deposit(MonetaryAmount(20))
      bankAccount.withdraw(MonetaryAmount(10))

      bankAccount.balance mustEqual MonetaryAmount(10)
    }

    "have a way to change the owner" in {
      val newOwner = "Jane Doe"
      val modifiedBankAccount = bankAccount.changeOwner(newOwner)

      modifiedBankAccount.owner mustEqual newOwner
    }
  }
}
