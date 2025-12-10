# This file is for your convenience while developing.
# It runs your draw_plot() function and then runs the tests.

import sea_level_predictor
import unittest

# Draw the plot (this will also save sea_level_plot.png)
sea_level_predictor.draw_plot()

# Run unit tests automatically
print("Running unit tests...")
loader = unittest.TestLoader()
tests = loader.discover('.', pattern='test_module.py')
testRunner = unittest.TextTestRunner(verbosity=2)
testRunner.run(tests)
