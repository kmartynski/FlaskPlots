from flask import Flask
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import pandas as pd

app = (__name__)

@route('/')
def starting_page():
  return "Witaj w kreatorze wykresów"
  
if __name__ == "__main__":
  app.run(debug=True)
