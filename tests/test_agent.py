import unittest
from agent.run import target_path


class AgentPathTests(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(target_path("projects/example.py").name, "example.py")

    def test_rejected(self):
        for name in ("../x.py", "agent/run.py", "projects/../../x.py", "projects/script.sh"):
            with self.subTest(name=name):
                with self.assertRaises(ValueError):
                    target_path(name)


if __name__ == "__main__":
    unittest.main()
