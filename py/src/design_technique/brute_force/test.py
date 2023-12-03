import unittest
from chapter_exercises import exercise33 ,exercise34


class TestExercise33(unittest.TestCase):
    def test_max_difference(self):
        # テスト対象の関数を呼び出し
        exercise33()

        # テスト対象の関数がエラーをスローしないことを確認
        self.assertTrue(True)  # 何もしない場合の例

class TestExercise34(unittest.TestCase):
    def test_max_difference(self):
        # テスト対象の関数を呼び出し
        exercise34()

        # テスト対象の関数がエラーをスローしないことを確認
        self.assertTrue(True)  # 何もしない場合の例

if __name__ == '__main__':
    unittest.main()
