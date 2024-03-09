#!/usr/bin/env python3

from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(name="SATELLiTES", 
          version="1.0.5",
          packages=find_packages(),
          scripts=["src/runSATELLiTES"],
          )
