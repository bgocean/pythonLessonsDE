import datetime
import pandas as pd

from Utils.utils1 import Human as h

from Utils.global_config import USER_NAME


# d_one = datetime.datetime.utcnow()
d_one = datetime.datetime.now()

print(d_one)
print(type(d_one))


one_human = h()
one_human.say_hello()

df1 = pd.DataFrame()