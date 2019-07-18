import matplotlib.pyplot as plt
import csv
import numpy as np
from functools import reduce

def plotBarDiagram(x, y, vertical):
    range = np.arange(len(x))
    plt.bar(range, x.astype(float))
    plt.xticks(range, y)
    if vertical == True:
        plt.xticks(rotation='vertical')
    plt.show()
    
def normalize(column):
    sum = reduce((lambda x, y: x + y), column)
    return [i/sum for i in column]
    
def getNormalizedGeometricMean(column):
    norm = normalize(column)
    product = reduce((lambda x, y: x * y), norm)
    gM = math.pow(product, 1/preferenceCount)
    return gM

def getJsonByUrl(url):
#     requirements = [i['title'] for i in getJsonByUrl("http://ipe-cerberus12.fzi.de/api/requirements/read")]
#     print(requirements)
    import requests
    r = requests.get(url).json()
    return r