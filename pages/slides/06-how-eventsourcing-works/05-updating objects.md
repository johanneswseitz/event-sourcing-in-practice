## Updating objects

~~~ {.scala}
var account = accountRepository.get(123)
var modifiedAccount = account.withdraw(new Euro(10))
accountRepository.save(modifiedAccount)
~~~

What will be persisted?

![Updating EventStream](static/img/eventstream-update.png)
{.slide}