# vetica

At some point in your research career you may be asked for your matplotlib plots to use Helvetica.

The following code may work for you:

```
import matplotlib
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = 'Helvetica'
```

If it doesnt try this package.

To install:

```
pip install -e git+https://github.com/amcpherson/vetica.git#egg=vetica
```

To have matplotlib use Helvetica for fonts:

```
import vetica.mpl
```
