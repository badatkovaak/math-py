import unittest as ut
import sys
import math

sys.path.insert(0, '/home/badatkovaak/pr/code/py')
#fmt: off
import math_py.src.general.genericFunctions as gf
#fmt: on


class GeneralTest(ut.TestCase):
    def testFactorial(self):
        self.assertEqual(gf.factorial(1), 1, '1!')
        self.assertEqual(gf.factorial(5), 120, '5!')
        self.assertEqual(gf.factorial(7), 5040, '7!')
        self.assertEqual(gf.factorial(10), 3628800, '10!')
        self.assertEqual(gf.factorial(12), 479001600, '12!')
        self.assertEqual(gf.factorial(15), 1307674368000, '15!')
        self.assertEqual(gf.factorial(20), 2432902008176640000, '20!')

    def testExponent(self):
        figures = 10
        self.assertEqual(gf.exp(0), 1)
        self.assertAlmostEqual(gf.exp(1), 2.71828182845904523536, figures)
        self.assertAlmostEqual(gf.exp(2), 7.3890560989306502272, figures)
        self.assertAlmostEqual(gf.exp(3), 20.085536923187667741, figures)
        self.assertAlmostEqual(gf.exp(5), 148.41315910257660342, figures)
        self.assertAlmostEqual(gf.exp(10), 22026.465794806716517, figures)
        self.assertAlmostEqual(gf.exp(17), 24154952.753575298215, figures-2)
        self.assertAlmostEqual(gf.exp(22), 3584912846.1315915617, delta=0.1)
        self.assertAlmostEqual(
            gf.exp(-1), 0.367879441171442321595523770161, figures)
        self.assertAlmostEqual(
            gf.exp(-2), 0.135335283236612691893999494972, figures)
        self.assertAlmostEqual(
            gf.exp(-3), 0.0497870683678639429793424156501, figures)

    def testSqrt(self):
        figures = 12
        self.assertAlmostEqual(gf.sqrt(-1), -1, figures)
        self.assertAlmostEqual(gf.sqrt(0), -1, figures)
        self.assertAlmostEqual(gf.sqrt(2), math.sqrt(2), figures)
        self.assertAlmostEqual(gf.sqrt(3), math.sqrt(3), figures)
        self.assertAlmostEqual(gf.sqrt(5), math.sqrt(5), figures)
        self.assertAlmostEqual(gf.sqrt(10), math.sqrt(10), figures)
        self.assertAlmostEqual(gf.sqrt(97), math.sqrt(97), figures)
        self.assertAlmostEqual(gf.sqrt(291), math.sqrt(291), figures)
        self.assertAlmostEqual(gf.sqrt(6320), math.sqrt(6320), figures)
        self.assertAlmostEqual(gf.sqrt(3628800), math.sqrt(3628800), figures)
        self.assertAlmostEqual(gf.sqrt(2653148729),
                               math.sqrt(2653148729), figures)
        self.assertAlmostEqual(gf.sqrt(2653148729315),
                               math.sqrt(2653148729315), figures)

    def testAGM(self):
        d = 25
        self.assertAlmostEqual(gf.AGM(1, math.sqrt(2)),
                               1.19814023473559220743992249228, d)
        self.assertAlmostEqual(gf.AGM(1, 2),
                               1.45679103104690686918643238326, d)
        self.assertAlmostEqual(gf.AGM(24, 6),
                               13.4581714817256154207668131569, d)

    def testIntegration(self):
        d = 10
        self.assertAlmostEqual(gf.integrate1(
            lambda x: x*x, 0, 300), 9000000, delta=0.00001)
        self.assertAlmostEqual(gf.integrate1(
            lambda x: x*x*x, 0, 10), 2500, delta=0.00001)
        self.assertAlmostEqual(gf.integrate(
            lambda x: math.sin(x), 0, 2*math.pi), 0, delta=0.00001)

        pass


if __name__ == '__main__':
    ut.main()
