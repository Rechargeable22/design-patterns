"""Ensures a class has only one instance and provides a global access point"""
import threading


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating the instance")
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class SingletonThreadSafe:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                print("Creating the instance")
                cls._instance = super(SingletonThreadSafe, cls).__new__(cls)
            return cls._instance


def test_singleton_thread():
    singleton = SingletonThreadSafe()
    print(f"Instance ID: {id(singleton)}")


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2)

    thread_1 = threading.Thread(target=test_singleton_thread)
    thread_2 = threading.Thread(target=test_singleton_thread)
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()