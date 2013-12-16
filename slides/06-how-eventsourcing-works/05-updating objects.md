## Updating Objects

~~~ {.scala}
val account = accountRepository.get(123)
val modifiedAccount = account.withdraw(new Euro(10))
accountRepository.save(modifiedAccount)
~~~

What should be persisted?

![Updating EventStream](static/img/eventstream-update.png)
{.slide}