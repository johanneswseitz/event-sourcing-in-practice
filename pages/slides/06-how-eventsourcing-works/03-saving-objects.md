## Saving objects


#includeCode(code-samples/src/main/scala/event_sourcing/DepositPerformed.scala)

~~~ {.scala}
case class DepositPerformed(accountID:UUID, amount:MonetaryAmount)
~~~
