import unittest
import cv2

class TestProcessFaces(unittest.TestCase):
    def test_normal_directory_local(self):
        from atividade1 import processFaces
        local_image = raw_input("Insert directory") 
        assert processFaces(local_image) == cv2.waitKey()
        self.assertEqual(processFaces(local_image),cv2.waitKey())

if __name__ == '__main__':
    unittest.main()
