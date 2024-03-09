#!/usr/bin/env python3

from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(name="SATELLiTES", 
          version="1.0.6",
          packages=find_packages(),
          entry_points = {
        'console_scripts': ['SATELLiTES=SATELLiTES:run_SATELLiTES'],
        }
        #   scripts=["src/runSATELLiTES"],
          )
