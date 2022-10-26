import unittest
from dm_formatter import reformat_for_bgnn


DM_INPUT_METADATA = {
  "SOME-FISH-1234": {
    "fish_count": 1,
    "fish": [ {
       "pixel_analysis_failed": False,
       "bbox": [1,2,3,4],
       "has_eye": True,
       "eye_center": [50, 50],
       "side": "left",
       "foreground": {
          "mean": 100.1111111,
        },
        "background": {
          "mean": 200.1111111,
        }
       }
    ],
    "has_ruler": True,
    "ruler_bbox": [
      5,
      6,
      7,
      8
    ],
  }
}

BGNN_EXPECTED_METADATA = {
   'base_name': 'SOME-FISH-1234',
   'fish': {'angle_degree': 'None',
            'background_mean': 200.11,
            'bbox': [1, 2, 3, 4],
            'eye_bbox': 'None',
            'eye_center': [50, 50],
            'eye_direction': 'left',
            'fish_num': 1,
            'foreground_mean': 100.11,
            'pixel_analysis': True,
            'rescale': 'None'},
   'ruler': {'bbox': [5, 6, 7, 8], 'scale': 'None', 'unit': 'None'},
   'version': 'from drexel'
}


class TestFormatter(unittest.TestCase):
    def test_reformat_for_bgnn(self):
        result = reformat_for_bgnn(DM_INPUT_METADATA)
        self.assertEqual(result, BGNN_EXPECTED_METADATA)



if __name__ == '__main__':
    unittest.main()
