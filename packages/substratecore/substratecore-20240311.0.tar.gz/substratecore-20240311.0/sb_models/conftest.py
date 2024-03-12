import os
import sys

sb_models = os.path.abspath(os.path.dirname(__file__))
tests_dir = sb_models + "/tests"

sys.path.insert(0, sb_models)
sys.path.insert(0, tests_dir)
