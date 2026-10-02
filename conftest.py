"""Present so pytest adds the project root to sys.path, letting the tests
import ``cli``, ``stats``, ``report``, and ``io_utils`` directly.

Run pytest from this directory. From anywhere else the imports fail with
``ModuleNotFoundError``.
"""
