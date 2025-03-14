import yaml


text="""
firstname: Lucas
lastname: ALLAIN
"""

import io 

stream = io.StringIO(text)
newDico = yaml.load(stream)

