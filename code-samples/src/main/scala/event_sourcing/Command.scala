package event_sourcing

trait Command[T] {
  def execute(someObject:T) : T
}
