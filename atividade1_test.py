import unittest
import cv2

class TestProcessFaces(unittest.TestCase):
    def test_normal_directory_local(self):
        from atividade1 import processFaces
        local_image = raw_imput("Insert directory") 
        assert processFaces(local_image) == cv2.inshow('image', local_image)
        self.assertEqual(processFace(local_image),cv2.inshow('image'),local_image)

if __name__ == '__main__':
    unittest.main() 
