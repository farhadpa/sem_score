import unittest
import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
    
    def test_zero_attendance(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], "0.00")

    def test_all_attendance(self):
        response = self.app.get('/?lecture_attendance=33&lab_attendance=22&support_attendance=44&canvas_activity=55')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], "100.00")

    def test_half_attendance(self):
        response = self.app.get('/?lecture_attendance=16.5&lab_attendance=11&support_attendance=22&canvas_activity=27.5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], "50.00")

    def test_negative_attendance(self):
        response = self.app.get('/?lecture_attendance=-1&lab_attendance=-1&support_attendance=-1&canvas_activity=-1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], "0.00")
    
    def test_invalid_attendance(self):
        response = self.app.get('/?lecture_attendance=one&lab_attendance=two&support_attendance=three&canvas_activity=four')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], "0.00")
        
    

if __name__ == '__main__':
    unittest.main()