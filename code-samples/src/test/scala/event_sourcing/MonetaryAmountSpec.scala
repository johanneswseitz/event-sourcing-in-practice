package event_sourcing


import event_sourcing.MonetaryAmount
import org.specs2.mutable._
import org.specs2.runner.JUnitRunner
import org.junit.runner.RunWith

@RunWith(classOf[JUnitRunner])
class MonetaryAmountSpec extends Specification {

  "The MonetaryAmount" should {
    "support the sum operator" in {
      MonetaryAmount(10) + MonetaryAmount(10) mustEqual MonetaryAmount(20)
    }

    "support the subtration operator" in {
      MonetaryAmount(10) - MonetaryAmount(10) mustEqual MonetaryAmount(0)
    }

    "support the unary subtration operator" in {
      - MonetaryAmount(10) mustEqual MonetaryAmount(-10)
    }
  }
}
