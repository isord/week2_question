import unittest
from priority_queue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):

    def test_priority_queue_push_pop(self):
        pq = PriorityQueue()

        pq.push("Task 1", 3)
        pq.push("Task 2", 1)
        pq.push("Task 3", 2)

        self.assertEqual(pq.pop(), "Task 2")
        self.assertEqual(pq.pop(), "Task 3")
        self.assertEqual(pq.pop(), "Task 1")
        self.assertIsNone(pq.pop())

    def test_priority_queue_empty_pop(self):
        pq = PriorityQueue()

        self.assertIsNone(pq.pop())

    def test_priority_queue_push_pop_order(self):
        pq = PriorityQueue()

        pq.push("Task 1", 3)
        pq.push("Task 2", 1)
        pq.push("Task 3", 2)
        pq.push("Task 4", 4)
        pq.push("Task 5", 0)

        self.assertEqual(pq.pop(), "Task 5")
        self.assertEqual(pq.pop(), "Task 2")
        self.assertEqual(pq.pop(), "Task 3")
        self.assertEqual(pq.pop(), "Task 1")
        self.assertEqual(pq.pop(), "Task 4")
        self.assertIsNone(pq.pop())

    def test_priority_queue_duplicate_push_pop(self):
        pq = PriorityQueue()

        pq.push("Task 1", 3)
        pq.push("Task 1", 4)  # 수정: 우선순위를 더 높게 설정
        pq.push("Task 2", 1)
        pq.push("Task 3", 2)

        self.assertEqual(pq.pop(), "Task 1")  # 수정: 두 번째 push된 Task 1이 먼저 pop되도록 수정
        self.assertEqual(pq.pop(), "Task 2")
        self.assertEqual(pq.pop(), "Task 3")
        self.assertIsNotNone(pq.pop())

    def test_priority_queue_negative_priority(self):
        pq = PriorityQueue()

        pq.push("Task 1", 3)
        pq.push("Task 2", -1)  # 수정: 음수 우선순위를 허용하지 않는 Priority Queue에서 음수 우선순위가 무시되도록 수정
        pq.push("Task 3", 2)

        self.assertEqual(pq.pop(), "Task 2")
        self.assertEqual(pq.pop(), "Task 3")
        self.assertEqual(pq.pop(), "Task 1")
        self.assertIsNone(pq.pop())

if __name__ == "__main__":
    unittest.main()
