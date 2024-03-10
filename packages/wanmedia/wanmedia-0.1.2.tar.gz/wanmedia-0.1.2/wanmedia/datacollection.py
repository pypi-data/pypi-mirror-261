import numpy as np
import pandas as pd

def getlink(shareurl):
  return 'https://docs.google.com/uc?export=download&id='+shareurl.split('/')[-2]

def econnews():
  url = getlink("https://drive.google.com/file/d/1nfuhwK_hjqPsfbp7ybXgZOUWZkgPqyDe/view?usp=drive_link")
  return  pd.read_csv(url, index_col=0).drop_duplicates()


def stocknews():
  url = getlink("https://drive.google.com/file/d/1WZyAEmqSf0Lskx4_-qJq3rz4PEdGkQVA/view?usp=drive_link")
  return  pd.read_csv(url, index_col=0).drop_duplicates()

def yelprating():
  url = getlink("https://drive.google.com/file/d/1KR4rA1AlteQv1QEKHbWkdKhTRHcrr6oD/view?usp=drive_link")
  return  pd.read_csv(url, index_col=0).drop_duplicates()

def twitter():
  url = getlink("://drive.google.com/file/d/1frox8TLvzsK94rSu43dBVrwpvu8JL9Si/view?usp=sharing")
  return  pd.read_csv(url, index_col=0).drop_duplicates()

def eurusd():
  url = getlink("https://drive.google.com/file/d/1YJTJyklVqWKbHLVCUez-VMm3msOq-Dse/view?usp=share_link")
  return  pd.read_csv(url, index_col=0).drop_duplicates()