import unittest
from calculate_score import calculate_engagement_score


class TestCalculateScore(unittest.TestCase):
    total_lectures = 33
    total_labs = 22
    total_support_sessions = 44
    total_canvas_expected = 55

    # test for zero attendance
    def test_zero_attendance(self):
        self.assertEqual(calculate_engagement_score(), "0.00")

    # test for all attendance
    def test_all_attendance(self):
        self.assertEqual(
            calculate_engagement_score(
                total_attendance_lectures=self.total_lectures,
                total_attendance_lab=self.total_labs,
                total_attendance_support=self.total_support_sessions,
                total_canvas_activity=self.total_canvas_expected,
            ),
            "100.00",
        )

    # test for half attendance
    def test_half_attendance(self):
        self.assertEqual(calculate_engagement_score(
            total_attendance_lectures=self.total_lectures/2, 
            total_attendance_lab=self.total_labs/2, 
            total_attendance_support=self.total_support_sessions/2, 
            total_canvas_activity=self.total_canvas_expected/2
            ), 
            "50.00")

    # test for negative attendance
    def test_negative_attendance(self):
        self.assertEqual(calculate_engagement_score(-1, -1, -1, -1), "0.00")

    # test for invalid attendance(should return error)
    def test_invalid_attendance(self):
        self.assertEqual(calculate_engagement_score("one", "two", "three", "four").startswith("Error"), True)


if __name__ == "__main__":
    unittest.main()
