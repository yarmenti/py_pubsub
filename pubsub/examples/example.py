
from pubsub import Subscriber, Publisher

if __name__ == "__main__":
    from typing import Sequence, Any

    print("Use of the sub/sub pattern.")
    print("Inheritance of the Publisher and Subscriber classes.")

    class MockPublisher(Publisher):
        @property
        def triggerable_messages(self) -> Sequence[str]:
            return ["test"]

    class MockSubscriber(Subscriber):
        def on_message(self, message: str, arg: Any) -> Any:
            print(message)
            print(arg)

    print("Instanciation of a publisher-subscriber pair.")
    pub = MockPublisher()
    sub = MockSubscriber()

    print("Attach the subscriber to the publisher.")
    pub.attach(sub, "test")

    print("Publisher triggering 'test' with argument 'Hello' of type str.")
    print("Should print 'test' and 'Hello'")
    pub.trigger("test", "Hello")

    print("Detach the subscriber of the publisher.")
    pub.detach(sub, "test")

    print(
        "Shouldn't print anything as the subsriber"
        "is detached from the publisher."
    )
    pub.trigger("test", "World")

    try:
        pub.attach(sub, "not in messages")
    except Exception as e:
        print(e)
        pass
