#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square


class Test_square_instantiation(unittest.TestCase):
    """Testing instantiation of the Square class."""

    def test_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_rectangle_instance(self):
        self.assertIsInstance(Square(10), Square)

    def test_zero_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_arg(self):
        sqr1 = Square(10)
        sqr2 = Square(11)
        self.assertEqual(sqr1.id, sqr2.id - 1)

    def test_args_two(self):
        sqr1 = Square(10, 2)
        sqr2 = Square(2, 10)
        self.assertEqual(sqr1.id, sqr2.id - 1)

    def test_args_three(self):
        sqr1 = Square(10, 2, 2)
        sqr2 = Square(2, 2, 10)
        self.assertEqual(sqr1.id, sqr2.id - 1)

    def test_args_four(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_five(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter(self):
        sqr1 = Square(4, 1, 9, 2)
        sqr1.size = 8
        self.assertEqual(8, sqr1.size)

    def test_width_getter(self):
        sqr1 = Square(4, 1, 9, 2)
        sqr1.size = 8
        self.assertEqual(8, sqr1.width)

    def test_height_getter(self):
        sqr = Square(4, 1, 9, 2)
        sqr.height = 8
        self.assertEqual(8, sqr.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(10).y)


class Test_square_size(unittest.TestCase):
    """Testing size initialization of the Square class."""

    def test_zero_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_size_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("name")

    def test_size_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def test_size_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2}, 2)

    def test_size_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 2, 3)

    def test_size_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)

    def test_size_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2, 3)

    def test_size_range(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(5))

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)


class Test_square_x(unittest.TestCase):
    """UnitTest_s for testing initialization of Square x attribute."""

    def test_zero_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "name")

    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 5.5)

    def test_x_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"a": 1, "b": 2}, 2)

    def test_x_bool(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, True)

    def test_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3])

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1, 2, 3})

    def test_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (1, 2, 3))

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0)

    def test_x_range(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, range(5))


class Test_square_y(unittest.TestCase):
    """Testing initialization of Square y attribute."""

    def test_zero_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, None)

    def test_y_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "invalid")

    def test_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, 5.5)

    def test_y_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {"a": 1, "b": 2})

    def test_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, [1, 2, 3])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {1, 2, 3})

    def test_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, (1, 2, 3))

    def test_y_range(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, range(5))


class Test_square_area(unittest.TestCase):
    """Testing the area method of the Square class."""

    def test_area(self):
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def test_larger_area(self):
        sqr = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, sqr.area())

    def test_changed_attributes(self):
        sqr = Square(2, 0, 0, 1)
        sqr.size = 7
        self.assertEqual(49, sqr.area())

    def test_area_arg(self):
        sqr = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            sqr.area(1)


class Test_square_update_args(unittest.TestCase):
    """Testing update args method of the Square class."""

    def test_update(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(sqr))

    def test_update_arg(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(sqr))

    def test_update_two(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(sqr))

    def test_update_three(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(sqr))

    def test_update_four(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(sqr))

    def test_update_five(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(sqr))


class Test_square_to_dictionary(unittest.TestCase):
    """UnitTest_s for testing to_dictionary method of the Square class."""

    def test_to_dictionary(self):
        sqr = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, sqr.to_dictionary())

    def test_to_dictionary_args(self):
        sqr = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            sqr.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
