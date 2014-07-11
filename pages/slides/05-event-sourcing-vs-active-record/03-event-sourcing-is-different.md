## Event Sourcing is different

- Don't save the **current state** of objects
- Save the **events** that lead to the current state

<div class="slide" markdown="1">
- **Event**: Something that happend *in the past*.
- E.G. ![Deposit Performed Event in UML](static/img/deposit-performed-event-v1.png)

<!-- http://www.yuml.me/diagram/scruffy;/class/edit/[DepositPerformed|amount;accountNumber] -->
</div>